class Counter:
    def __init__(self):
        self.count = 0

    def add_one(self):
        self.count += 1

c = Counter()        # step 1: build the real thing (only once)
c.add_one()          # step 2: use it
c.add_one()
print(c.count)       # 2