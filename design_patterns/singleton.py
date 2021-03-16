"""SINGLETONS USING META-CLASS"""
from meta.meta_class import SingletonType


class Singleton(metaclass=SingletonType):
    """
    A Singleton is a pattern that restricts the instantiation of a class one instance/object.
    """
    a = 1


class SingletonWithoutMetaClass(object):
    """SINGLETONS WITHOUT META-CLASS"""
    a = 1

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingletonWithoutMetaClass, cls).__new__(cls)
        return cls._instance


if __name__ == '__main__':
    i = SingletonWithoutMetaClass()
    print(i.a, i)
    i.a = 2
    i2 = SingletonWithoutMetaClass()
    print(i2.a, i2)
