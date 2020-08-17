class SeqList(object):
    def __init__(self, max=8):
        self.max = max
        self.num = 0
        self.date = [None] * self.max

    def is_empty(self):
        return self.num is 0

    def is_full(self):
        return self.num is self.max
