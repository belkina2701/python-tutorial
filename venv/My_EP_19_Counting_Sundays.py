''' Counting Sundays - Problem 19

INPUT:
Information:
- 01/12/1900 was a Monday.
- April, June, September and November - 30 days
- All the rest have - 31 days
- February - 28 days
Leap year
- February - 29 days
- Leap year if % 4 == 0
- ХХ00 if % 400 == 0

PROBLEM:
How many Sundays fell on the first of the month during the twentieth century (01/01/1901 to 31/12/2000)?

OUTPUT: 171

DOCSTRING:
'''

def count_sunday_1900_to_n(N):
    count = 0
    rest = 0
    for year in range(1900, N+1):
        months = ('January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December')
        month_30 = ('April', 'June', 'September', 'November')
        for i in months:
            if i == 'February':

                if year % 100 == 0:
                    if year % 400 == 0:
                        feb = 29
                    else:
                        feb = 28
                elif year % 4 == 0:
                    feb = 29
                else:
                    feb = 28

                if rest == 6:
                    count += 1
                    # print(f'{count = } {year = }  , February')
                days = feb + rest
                rest = days % 7
            elif i in month_30:
                if rest == 6:
                    count += 1
                    # print(f'{count = } {year = }  , {i}')
                days = 30 + rest
                rest = days % 7
            else:
                if rest == 6:
                    count += 1
                    # print(f'{count = } {year = }  , {i}')
                days = 31 + rest
                rest = days % 7
    return count

start_year = 1900
finish_year = 2000

start = count_sunday_1900_to_n(start_year)
finish = count_sunday_1900_to_n(finish_year)
print(start, finish)

resalt = finish - start
print(resalt)
