# You are given the following information, but you may prefer to do some research 
# for yourself.
# 
# * 1 Jan 1900 was a Monday.
# * Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
# * A leap year occurs on any year evenly divisible by 4, but not on a century 
#   unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century 
# (1 Jan 1901 to 31 Dec 2000)?

import datetime

# start = datetime.date(1901, 1,  1)
# end   = datetime.date(2000, 12, 31)

count = 0
for year in range(1901, 2001):
  for month in range(1, 13):
    if datetime.date(year, month, 1).strftime("%A") == 'Sunday':
      count += 1
      
print count      

# 171
#
# real	0m0.042s
# user	0m0.040s
# sys	0m0.010s

