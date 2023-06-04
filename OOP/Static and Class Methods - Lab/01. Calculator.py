class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        total = 1
        for x in args:
            total *= x
        return total

    @staticmethod
    def divide(*args):
        total = args[0]
        for x in args[1:]:
            total /= x
        return total

    @staticmethod
    def subtract(*args):
        total = args[0]
        for x in args[1:]:
            total -= x
        return total
