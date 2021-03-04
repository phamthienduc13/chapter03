month = int(input('Enter the month from 1 - 12: '))
day = int(input('Enter the day from 1 - 31: '))
year = int(input('Enter the year: '))
message = '' + format(month) + '/' \
          + format(day) + '/' \
          + format(year) + \
          ' IS '
if ((month * day) == year):
     message += 'magic.'
else:
    message += 'not magic.'
print(message, " ")