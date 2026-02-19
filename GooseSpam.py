class GooseSpam:
    def __iter__(self):
        pass

if __name__ == "__main__":
    from collections import abc
    print(issubclass(GooseSpam, abc.Iterable))

    goose_spam_can = GooseSpam()
    print(isinstance(goose_spam_can, abc.Iterable))