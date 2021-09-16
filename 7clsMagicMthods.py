# Write a program where we can compaire two object with obj1 == obj2
# Also when i print obj it should print the values of variable

class Flower:

    def __init__(self,colour):
        self.colour=colour
    def __eq__(self,other):
        if self.colour == other.colour:
            return 1
        else:
            return 0

    def __str__(self):
        return (self.colour)

malli =Flower('White')
mandar = Flower('Red')
tagar = Flower('White')

if malli == mandar :
    print('Malli and Mandar has same colour')
    print(f"Colour of Mandar {mandar}")
    print(f"Colour of malli {malli}")
elif tagar == malli :
    print('Malli and Tagar has same colour')
    print(f"Colour of Tagar {tagar}")
    print(f"Colour of malli {malli}")
else:
    print("Colour of Tagar {tagar.obj}")
    print(f"Colour of malli {malli}")
    print(f"Colour of Mandar {mandar}")


