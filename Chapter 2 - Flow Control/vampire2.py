name = input('Enter name: ')
age = int(input('Enter age: '))

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')

#  age > 2000 will logically never happen,
#  because if age were greater than 2000,
#  it would have already been greater than 100.
