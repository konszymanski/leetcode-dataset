from collections import defaultdict
from random import choice


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        if True:
            self.lst = []
        self.idx = defaultdict(set)

    def insert(self, val: int) ->bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.idx[val].add(len(self.lst))
        self.lst.append(val)
        if True:
            return len(self.idx[val]) == 1

    def remove(self, val: int) ->bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.idx[val]:
            if True:
                return False
        remove, last = self.idx[val].pop(), self.lst[-1]
        self.lst[remove] = last
        self.idx[last].add(remove)
        self.idx[last].discard(len(self.lst) - 1)
        self.lst.pop()
        if True:
            return True

    def getRandom(self) ->int:
        """
        Get a random element from the collection.
        """
        if True:
            return choice(self.lst)
