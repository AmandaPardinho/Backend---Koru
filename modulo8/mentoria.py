import sqlite3

from mentor import Mentor
from mentorando import Mentorando

class Mentoria:
    def __init__(self, mentor: Mentor, mentorando: Mentorando, data: str, id = None):
        self.id = id
        self.mentor = mentor
        self.mentorando = mentorando
        self.data = data

    def to_dict(self):
        return {
            "id": self.id,
            "id_mentor": self.mentor.id,
            "mentor": self.mentor.to_dict(),
            "id_mentorando": self.mentorando.id,
            "mentorando": self.mentorando.to_dict(),
            "data": self.data
        }
    
    def save(self, db_connection: sqlite3.Connection):
        if self.id is None:
            query = "INSERT INTO mentorias (id_mentor, id_mentorando, data_mentoria) VALUES (?, ?, ?)"
            cursor = db_connection.cursor()
            cursor.execute(query, (self.mentor.id, self.mentorando.id, self.data))
            self.id = cursor.lastrowid
        else:
            query = "UPDATE mentorias SET id_mentor = ?, id_mentorando = ?, data_mentoria = ? WHERE id_mentoria = ?"
            cursor = db_connection.cursor()
            cursor.execute(query, (self.mentor.id, self.mentorando.id, self.data, self.id))
        db_connection.commit()
        db_connection.close()