class Product:

    def __init__(self):
        self.product = 1

    def increment(self):
        self.product = self.product + 1

    def showNumberOfObjects(self):
        print("Total Product Object: {}".format(self.product))


p1 = Product()
p2 = Product()
p3 = Product()
p4 = p1
p5 = p3

p1.increment()
p2.increment()
p3.increment()

p1.increment()
p2.increment()
p3.increment()

p5 = p3


p5.showNumberOfObjects()
# Total Product Object : 3