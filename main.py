# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def print(self):         # а здесь в аргументах не указываю name
        print("Hello, ", self.name)

    # геттер
    def get_age(self):
        print(self.age)

    # геттер
    # def get_age(self, age):   # здесь в аргументах указываю age
    #     print(age)

    # сеттер
    def set_age(self, age):
        if age < 0:
            print("error")
        else:
            print("that's good")
            return self.age

    # def older(self):
    #     if



