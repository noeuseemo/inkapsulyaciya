class Human:
    def __init__(self, n, a, h):
        print("sozdan obekt class human")
        self.__name = a
        self.__age = n
        self.__height = h

    def print (self):
        print (f'name: {self.__name}')
        print (f'age: {self.age}')
        print (f'height: {self.height}')
        print ('-'*30)

    @property
    def name (self):
        return self.__name.upper()

    
    @name.setter
    def name (self,n):
        self.__name = n.capitalize()

    @property
    def age (self):
        return self.__age
    

    
    @age.setter
    def age (self,n):
        self.__age = n
        if  n > 0 and n < 100:
                self.__age = n
            
        else:
                print ("no right age")




    @property
    def height (self):
        return self.__height

    @height.setter
    def height (self,h):
        self.__height = h
        if h > 0 and h < 200:
            self.__height = h
        else:
            print("height no correctly")


person1 = Human('rustam', 35, 180)
person1.print()
person1.name ='monomah'
person1.age= 30
person1.height = 179


print (person1.age)
print (person1.name)
print (person1.height)
