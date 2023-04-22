from mentor import Mentor
from mentorando import Mentorando

class Mentoria:
    def __init__(self, mentor: Mentor, mentorando: Mentorando, data: str, id = None):
        self.id = id
        self.mentor = mentor
        self.mentorando = mentorando
        self.data = data