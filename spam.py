from collections import abc


class Spam:
    def __getitem__(self, i):
        print('->', i)
        raise IndexError()
    
if __name__ == "__main__":

    spam_can = Spam()
    print(iter(spam_can))
    print(list(spam_can))
    print(isinstance(spam_can, abc.Iterable))