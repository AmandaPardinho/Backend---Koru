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