import abc
from abc import abstractmethod

"""
Factory Pattern is also a Creational Pattern. The term factory means that a class is responsible for creating object of 
other types. There is a class that acts as a factory which has objects and methods associated with it. The client 
creates an object by calling the methods with certain parameters and factory create the object of the desired type and
return it to the client.
"""


class Music(abc.ABC):

    @abstractmethod
    def pay(self):
        pass


class Mp3(Music):

    def pay(self):
        print("Playing .mp3 music.")


class Mp4(Music):

    def pay(self):
        print("Playing .ogg music.")


class MusicFactory:

    @staticmethod
    def pay_sound(object_type):
        return eval(object_type)().pay()


if __name__ == '__main__':
    music = input("Which music you want to pay Mp3 or Mp4")
    MusicFactory.pay_sound(music)
