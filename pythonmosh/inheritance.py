class mammal:
    def walk(self):
        print("walk")


class dog(mammal):
    def bark(self):
        print("bark")


class cat(mammal):
    #pass
    def be_annoying(self):
        print("annoying")

dog1 = dog()
dog1.bark()

cat1 = cat()
cat1.be_annoying()