numb = int(input("Enter a number between 3 and 9: "))


if numb <= 3 or numb >= 9:
    print("Please enter a valid number input. ")

else:

    for i in range(1, 2 * numb):
        if i <= numb:
            print('*' * i)
        else:
            print('*' * (2 * numb - i))