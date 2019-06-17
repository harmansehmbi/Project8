class Counter:

    def __init__(self):
        self.count = 1

    def incrementCount(self):
        self.count = self.count + 1

    def showCount(self):
        print("count is {}".format(self.count))

c1 = Counter()
c2 = Counter()
c3 = c1

c1.incrementCount()
c2.incrementCount()
c3.incrementCount()

c1.incrementCount()
c2.incrementCount()
c3.incrementCount()

c1.showCount()
c2.showCount()
c3.showCount()

