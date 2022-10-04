class Student:
        def __init__(self, name="아무나", age = 20):
            self._name = name
            self._age = age


        def showInfo(self) :
            print(self._name, self._age)

s1 = Student()
s2 = Student('이기기')
s3 = Student(age = 30)
s4 = Student('이최박', 40)


s1.showInfo()
s2.showInfo()
s3.showInfo()
s4.showInfo()