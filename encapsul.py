class Example:
    def __init__(self):
        self.__private_variable = None

    @property
    def private_variable(self):
        return self.__private_variable

    @private_variable.setter
    def private_variable(self, value):
        if value > 0:
            self.__private_variable = value
        else:
            print("Invalid value")

obj = Example()
obj.private_variable = 42  # Accessing private variable through property setter
print(obj.private_variable)  # Accessing private variable through property getter
