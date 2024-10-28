'''def namepls():
    name=input("What's your name?")
    print(f"Hello {name}! How are you? Have a nice day!")'''


#namepls()

#Creating a student class 
class student:
    #Constructor function
    def __init__(self,name,grade,age,house,teacher):
        self.name=name
        self.grade=grade
        self.age=age
        self.house=house
        self.teacher=teacher
        self.school="Newbury Primary School"
    def details(self):
        print(f"Name of the student is {self.name}")
        print(f"Grade of the student is {self.grade}")
        print(f"Age of the student is {self.age}")
        print(f"House of the student is {self.house}")
        print(f"Teacher of student is {self.teacher}")
        print(f"School of student is {self.school}")
S1=student("Darshika","6D","12","Gilmore","Mrs Tuiopa")
S1.details()