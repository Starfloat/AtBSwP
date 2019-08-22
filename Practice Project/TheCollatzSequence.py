def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number//2
    if number % 2 == 1:
        print(3*number+1)
        return 3*number+1

while True:
    try:
        number = int(input('Enter a number: '))
        if type(number) is int:
            break
        else:
            raise ValueError
    except ValueError:
        print('Please enter an integer.')

while number > 1:
    number = collatz(number)
