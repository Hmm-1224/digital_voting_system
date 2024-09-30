import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/voting_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

