x = int(input('Enter a year:'))
y = (x%100)
if y == 1:
    print(f'{x} is the first year of the century!')
else:
    print(f'{x} is not the first year of the century.')
