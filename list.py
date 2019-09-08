import numpy as np

class Student:
    def __init__(self , ID , firstname , lastname , phone , gender , birthdate):
        self.__GRADE_LETTERS = ["D", "C", "B", "A", "A"]
        self.ID = ID
        self.fullname = firstname + " " + lastname
        self.email = firstname + " " + lastname + "@aua.am"
        self.phone = phone
        self.gender = gender
        self.birthdate = birthdate
        self.grade = -1
        self.gradeLetter = "N/A"

    def setGrade(self, grade):
        if grade > 100 or grade < 0:
            print("Error: wrong grade value")
            return
        elif grade < 60:
            self.gradeLetter = " F "
        else:
            gradeLetterIndex = np.floor((grade - 60)/10)
            self.gradeLetter = self.__GRADE_LETTERS[int(gradeLetterIndex)]
        self.grade = grade

    def getGradeLetter(self):
        return self.gradeLetter


    def printPersonalInfo(self):
        print("ID: ", self.ID)
        print("Name: ", self.fullname)
        print("Email: ", self.email)
        print("Gender: ", self.gender)
        print("Birth Date: ", self.birthdate)
        print("Grade: ", self.grade)
        print("GradeLetter: ", self.gradeLetter)

    def getCurrentGrade(self):
        return self.grade

if __name__ == '__main__':
    st1 = Student("AUS123", "Gor", "Isoyan", 123456, "M", "01/01/2019")
    st2 = Student("AUS123", "Anna", "Saroyan", 465798, "F", "09/09/2010")

    st2.setGrade(81)

    st2.printPersonalInfo()
    