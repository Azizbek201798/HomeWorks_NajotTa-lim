def magicdice(n):
    numerator = 2 ** n * (1 - 1 / (2 ** n)) ** 2 + (1 - 1 / (2 ** n)) ** 3
    denominator = (2 ** n) ** 2
    return (numerator, denominator)