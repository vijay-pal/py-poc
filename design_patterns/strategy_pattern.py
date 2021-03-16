"""It is use to define a family of algorithms, encapsulates each one, and make them interchangeable. <u>Strategy design
pattern lets an algorithm vary independently from clients that use it.</u>
"""
from types import MethodType


class Searching:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('name', None) or 'Searching'
        self.key = kwargs.pop('key', None)
        if kwargs.get('search'):
            self.search = MethodType(kwargs.pop('search', None), self)
        self.elements = args

    def search(self):
        """
        Moving functionality is a strategy, and is intended to be implemented separately by different types of vehicles.
        :return:
        """
        raise NotImplementedError(F"{self.__class__.__name__} should implement a search method.")


def linear_search(self):
    for idx, value in enumerate(self.elements):
        if self.key == value:
            return idx
    return -1


def binary_search(self):
    def search(l, h):
        if l < h and self.elements[l] <= self.key <= self.elements[h]:
            mid = (l + h) // 2
            if self.elements[mid] == self.key:
                return mid
            if self.elements[mid] > self.key:
                return search(l, mid)
            else:
                return search(mid, h)
        return -1

    return search(0, len(self.elements) - 1)


def interpolar_search(self):
    def search(l, h):
        if l < h and self.elements[l] <= self.key <= self.elements[h]:
            pos = l + ((h - l) // (self.elements[h] - self.elements[l]) * (self.key - self.elements[l]))
            if self.elements[pos] == self.key:
                return pos
            elif self.key > self.elements[pos]:
                return search(pos, h)
            else:
                return search(l, pos)
        return -1
    zip()

    return search(0, len(self.elements) - 1)


# generic_search = Searching()
# generic_search.search()
linear_search = Searching(*[1, 4, 13, 21, 5, 10, 30], name='Linear Search', key=10, search=linear_search)
binary_search = Searching(*[1, 3, 5, 9, 10, 15, 16, 20], name='Binary Search', key=10, search=binary_search)
interpolar_search = Searching(*[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], name='Interpolar Search,', key=7,
                              search=interpolar_search)
print(linear_search.search())
print(binary_search.search())
print(interpolar_search.search())
