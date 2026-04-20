import datetime
day, month, year = map(int, input().split())
dt = datetime.date(year, month, day)
print(dt.strftime("%A").upper())

