import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_votes = []
        self.create_block(previous_hash='1')  # Initial block

    def create_block(self, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'votes': self.current_votes,
            'previous_hash': previous_hash,
            'timestamp': time()
        }
        self.current_votes = []  # Reset current votes
        self.chain.append(block)
        return block

    def add_vote(self, vote):
        self.current_votes.append(vote)

    def hash(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

