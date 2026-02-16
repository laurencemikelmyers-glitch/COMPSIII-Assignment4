class Student:
    def __init__(self, name, major, gpa_for_semesters):
        self.name = name
        self.major = major
        self.__gpa_for_semesters = gpa_for_semesters

    def __str__(self):
        return f"{self.name} is studying {self.major}."

    def get_gpa(self):
        return self.__gpa_for_semesters

    def set_gpa(self, new_value):
        self.__gpa_for_semesters = new_value

    def calculate_average_gpa(self):
        if len(self.__gpa_for_semesters) == 0:
            return 0
        return sum(self.__gpa_for_semesters) / len(self.__gpa_for_semesters)

    def is_in_good_standing(self):
        return f"{self.name} is a student."
class UndergraduateStudent(Student):

    def __str__(self):
        return f"{self.name} is an undergraduate student studying {self.major}."

    def is_in_good_standing(self):
        average = self.calculate_average_gpa()
        if average >= 2.5:
            return f"{self.name} is in good academic standing."
        return f"{self.name} is not in good academic standing."
class GraduateStudent(Student):

    def __str__(self):
        return f"{self.name} is a graduate student studying {self.major}."

    def is_in_good_standing(self):
        average = self.calculate_average_gpa()
        if average >= 3.0:
            return f"{self.name} is in good academic standing."
        return f"{self.name} is not in good academic standing."
