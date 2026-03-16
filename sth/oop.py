class human():
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def drink(self):
        if self.name == "York":
            print("York can't drink")
        else:
            print("drank")

york = human(17, "York")
york.drink()

york.name = "Koala"
york.drink()