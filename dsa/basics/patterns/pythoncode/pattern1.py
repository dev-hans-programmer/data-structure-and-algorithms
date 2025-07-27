def pattern1():
    """
    This is a pattern problem 1
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    """
    row = 5
    col = 5
    for i in range(1, row + 1):
        for col in range(1, col + 1):
            print("*", sep=" ", end=" ")
        print("")


if __name__ == '__main__':
    pattern1()