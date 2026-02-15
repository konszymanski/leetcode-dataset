from itertools import chain
from typing import List, Optional


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.itr = iter(nestedList)

    def next(self) -> int:
        val = next(self.itr)

        if val.isInteger():
            return val.getInteger()

        # expanding iterator
        self.itr = chain(val.getList(), self.itr)

        return self.next()

    def hasNext(self) -> bool:
        val: Optional[NestedInteger] = next(self.itr, None)

        if val is None:  # no item in the iterator
            return False
        elif val.isInteger():  # we got an item
            self.itr = chain([val], self.itr)
            return True
        else:
            # expanding iterator
            self.itr = chain(val.getList(), self.itr)
            return self.hasNext()