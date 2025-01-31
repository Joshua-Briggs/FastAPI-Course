from database import base
from sqlalchemy import Column, Integer, String


class QAA(base):
    __tablename__ = 'QAA'

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    answer = Column(String)

"""
INSIDE THE SQL DATABASE HERE IS THE EXACT DATA YOU WOULD WANT TO REPLICATE

DROP TABLE IF EXISTS QAA;

CREATE TABLE QAA (
	id SERIAL,
	question varchar(2000) DEFAULT NULL,
	answer varchar(2000) DEFAULT NULL,
	PRIMARY KEY (id)
);

"""