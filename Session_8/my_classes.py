
# always write class: this tells python we're defining our own type. 
# want to store: 
# name, age, race, subjects, grades. 
class Student:
    def __init__(self, name: str, age: int):
        # these are attributes:
        self.name = name.capitalize()
        self.age = age

    # set the course the student is studying:
    def set_course(self, course_name: str): 
        self.course = course_name
        return None

    # storing nationality:
    def set_nationality(self, nationality: str):
        self.nationality = nationality 
        return None
    
    def set_a_level_grades(self, grades: list):
        self.a_level_grades = grades
        return None
    
    def set_module_scores(self, module_scores: dict):
        self.module_scores = module_scores
        return None
    
    def add_module_score(self, module_name: str, score: int):
        self.module_scores[module_name] = score
        return None
    
    # here we define how python should print the class: 
    def __repr__(self):
        return f"Students Name is {self.name} and their Age is: {self.age}"