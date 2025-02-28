class Person:
    def __init__(self, name , age ): # init allows to intialize diffrerent values in clas
        self.name = name 
        self.age = age
        pass # pass is used to bypass the error
    
name =input ('entyer the name ')
age= input('enter your age')
p2 = Person(name,age)       
p1 = Person('john',87)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)

