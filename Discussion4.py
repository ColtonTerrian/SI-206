import math
class Rectangle():
# Create the constructor "__init__" method
# YOUR CODE HERE
    def __init__(self, w, h):
        self.width = w
        self.height = h
# Create the "__str__" method
    def __str__(self):
        return "A rectangle with width " + str(self.width) + " and height " + str(self.height)

# YOUR CODE HERE
# Create the "area_calculator" method
    def area_calculator(self):
        return float(self.width) * self.height

# YOUR CODE HERE
# Create the "__eq__" method
    def __eq__(self, other):
        if other.width == self.width and other.height == self.height:
            return True
        else:
            return False
# Returns a boolean value
# YOUR CODE HERE
def main():
    r1 = Rectangle(10, 10)
# call the __str__ method
    print(r1)
# call the area_calculator method
    print("Area:", r1.area_calculator())
    r2 = Rectangle(10, 15)
    print(r2)
    print("Area:", r2.area_calculator())
# call the __eq__ method
    print(r1 == r2)
    print()
    r3 = Rectangle(10,10)
    print(r1 == r3)
# you can create additional rectangle objects to
# test your code or learn more about how the class behaves
    pass
if __name__ == "__main__": 
    main()

