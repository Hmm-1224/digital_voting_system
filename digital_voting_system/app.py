from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Vote
from config import Config
from blockchain import Blockchain

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
blockchain = Blockchain()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user.is_voted:
        return jsonify({'message': 'You have already voted!'}), 403

    new_vote = Vote(user_id=user.id, candidate=data['candidate'])
    db.session.add(new_vote)
    db.session.commit()

    # Add vote to blockchain
    blockchain.add_vote({'user_id': user.id, 'candidate': data['candidate']})
    blockchain.create_block(previous_hash=blockchain.hash(blockchain.chain[-1]))

    user.is_voted = True
    db.session.commit()

    return jsonify({'message': 'Vote cast successfully!'}), 200

@app.route('/votes', methods=['GET'])
def get_votes():
    votes = Vote.query.all()
    return jsonify([{'user_id': vote.user_id, 'candidate': vote.candidate} for vote in votes]), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)

