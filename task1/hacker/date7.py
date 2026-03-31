import calendar

month, day, year = map(int, input().split())
day_index = calendar.weekday(year, month, day)

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

print(days[day_index])