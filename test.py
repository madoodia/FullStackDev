class Test(object):
    id = 13
    name = "madoodia"
    age = 35

    def __repr__(self):
        return f"{self.name} : {self.age}"


if __name__ == "__main__":
    t = Test(id=7, name="ryan", age=2)
    print(t)
