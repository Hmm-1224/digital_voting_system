# Digital Voting System

This project is a secure digital voting application developed using Flask. It allows users to register, cast votes, and ensures the integrity and transparency of the voting process by employing a blockchain-like structure for vote storage.

## Features

- **User Registration**: Users can register with a unique username and password.
- **Vote Casting**: Users can cast their votes for candidates of their choice.
- **Vote Storage**: Votes are stored in a blockchain-like structure to ensure transparency and immutability.
- **PostgreSQL Database**: User data and vote records are stored using PostgreSQL and SQLAlchemy ORM.

## Technologies Used

- **Flask**: Web framework for building the application.
- **SQLAlchemy**: ORM for database interactions.
- **PostgreSQL**: Database for storing user data and votes.
- **Python**: Programming language used for the application.

## Installation

### Prerequisites

NOTE: Make sure uyou are working in a  virtual environment and have all libraries. Make sure you have installed  PostgreSQL and get a username and password
and then modify config.py with your user name and password.
You can run following commands:-
- For register a user -> curl -X POST http://127.0.0.1:5000/register -H "Content-Type: application/json" -d '{"username": "user1", "password": "password123"}'
- For casting a vote -> curl -X POST http://127.0.0.1:5000/vote -H "Content-Type: application/json" -d '{"username": "user1", "candidate": "Candidate A"}'
- Get all votes -> curl -X GET http://127.0.0.1:5000/votes
### Clone the Repository

```bash
git clone https://github.com/Hmm-1224/digital_voting_system.git
cd digital_voting_system

