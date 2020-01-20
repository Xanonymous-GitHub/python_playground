this_year = 2020
first_weekday_of_this_year = 3
nums_of_days = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month_names = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December')
weekday_title = 'Su Mo Tu We Th Fr Sa'


def print_month_calendar(month, weekday1):
    global weekday_title, month_names, nums_of_days
    print(" " * 6, month_names[month], "\n", weekday_title, sep="")
    day = 1
    week = list()
    for x in range(weekday1):
        week.append("  ")
    while day <= nums_of_days[month]:
        while len(week) < 7 and day <= nums_of_days[month]:
            week.append(f'{day:2d}')
            day += 1
        print(" ".join(week))
        week = []

    return (weekday1 + nums_of_days[month]) % 7


def main():
    global first_weekday_of_this_year
    weekday = first_weekday_of_this_year
    for m in range(12):
        weekday = print_month_calendar(m, weekday)


if __name__ == "__main__":
    main()
