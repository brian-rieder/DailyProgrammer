__author__ = 'Brian Rieder'

# Link: http://www.reddit.com/r/dailyprogrammer/comments/2vc5xq/20150209_challenge_201_easy_counting_the_days/
# Difficulty: Easy

# Sometimes you wonder. How many days I have left until.....Whatever date you are curious about. Maybe a holiday.
# Maybe a vacation. Maybe a special event like a birthday.
# So today let us do some calendar math. Given a date that is in the future how many days until that date from the
# current date?
# Input:
# The date you want to know about in 3 integers. I leave it to you to decide if you want to do yyyy mm dd or
# mm dd yyyy or whatever. For my examples I will be using yyyy mm dd. Your solution should have 1 comment saying what
# format you are using for people reading your code. (Note you will need to convert your inputs to your format from
# mine if not using yyyy mm dd)

# Output:
# The number of days until that date from today's date (the time you run the program)
# Example Input: 2015 2 14
# Example Output: 5 days from 2015 2 9 to 2015 2 14

# Challenge Inputs:
# 2015 7 4
# 2015 10 31
# 2015 12 24
# 2016 1 1
# 2016 2 9
# 2020 1 1
# 2020 2 9
# 2020 3 1
# 3015 2 9


from calendar import monthrange
from calendar import isleap
from datetime import date


class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def validate_date(self):
        _, num_days_in_month = monthrange(self.year, self.month)
        year_today, month_today, day_today = [int(x) for x in str(date.today()).split("-")]
        # Make sure we're not in the past
        if year_today > self.year:
            return False
        elif year_today == self.year and month_today > self.month:
            return False
        elif year_today == self.year and month_today == self.month and day_today > self.day:
            return False
        # Now make sure the date is real at all
        if num_days_in_month < self.day:
            return False
        return True

    def count_days(self):
        day_count = 0
        year_today, month_today, day_today = [int(x) for x in str(date.today()).split("-")]
        # Speed up the process by going by fours
        while self.year - year_today > 4:
            day_count += 1461  # 365 + 365 + 365 + 366
            year_today += 4
        # Find the year
        while self.year != year_today:
            if isleap(year_today):
                day_count += 366
            else:
                day_count += 365
            year_today += 1
        # Find the month
        while self.month != month_today:
            _, num_days_in_month = monthrange(year_today, month_today)
            if month_today < self.month:
                day_count += num_days_in_month
                month_today += 1
            else:
                day_count -= num_days_in_month
                month_today -= 1
        # Find the day
        while self.day != day_today:
            if day_today < self.day:
                day_count += 1
                day_today += 1
            else:
                day_count -= 1
                day_today -= 1
        return day_count


def main():
    month, day, year = [int(x) for x in (input("Enter the day you want to count to in mm/dd/yyyy format: ")).split("/")]
    till_when = Date(month, day, year)
    if till_when.validate_date():
        num_days = till_when.count_days()
        print("There are " + str(num_days) + " days until then.")


if __name__ == "__main__":
    main()
