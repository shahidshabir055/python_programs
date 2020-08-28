def food():
    def __init__(self,fruit,color):
        self.fruit = fruit
        self.color = color
    def show(self):
        print("fruit is", self.fruit)
        print("color is", self.color)
    apple = food("apple",'red')
    grapes = food("grapes","black")
    print(apple.show())
    print(grapes.show())