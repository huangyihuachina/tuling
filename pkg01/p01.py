class Student:
    def __init__(self, name="NoName", age=18):
        """

        :type age: object
        """
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))


def say_hello():
    print("Hi, 欢迎来到图灵学院!")


print("我是")
