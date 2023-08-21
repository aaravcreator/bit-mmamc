



def mero_function(a,b):
    print(a/b)
 # **args collects any additional positional arguments in dictionary
 # **kwargs collects any additional keyword arguments in dictionary
def naya_function(*args,num=None,den=None,**kwargs):
    print(num/den)
    print(args)
    print('whole')
    print(kwargs['whole'])
    # print('prime')
    # print(kwargs['prime'])

# mero_function(25,5)
naya_function(1,22,den=55,num=110,whole=1)

""" 
Class IN python 
"""
# MaleFrog

class Animal:
    def __init__(self,name=None,color=None,gender=None):
        self.name = name
        self.color = color
        self.gender = gender

    def iam(self):
        if self.name is not None:
            print(f"I am {self.name}")
        else:
            print("MERO NARAN BHAKO CHAINA")

    def mygender(self):
        print(f"I am a {self.gender} animal")
    def mycolor(self):
        print(f"I am {self.color} in color , i love {self.color}")

    def short_intro(self):
        print(f" Hello its me  {self.name}, i am {self.gender} and i am {self.color} in color")

    def __str__(self):
        return f"I m OBJECT OF animal {self.name}"
new_animal = Animal(color="WHITE",gender="FEMALE",name="MILKY WHITE")
print(new_animal)
new_animal.iam()
new_animal.short_intro()