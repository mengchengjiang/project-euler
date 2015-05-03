year = 1900
month = 0
which_day = 0

num_sunday = 0

def num_day(year,month):
	if month in [0,2,4,6,7,9,11]:
		return 31
	elif month in [3,5,8,10]:
		return 30
	else:
		if year%100 == 0:
			if year%400 == 0:
				return 29
			else:
				return 28
		elif year%4 == 0 :
			return 29
		else:
			return 28

while year != 2001 :
	for month in range(12):
		count_day = num_day(year,month)
		if which_day == 6 and year >= 1901:
			num_sunday += 1
		for i in range(count_day):
			which_day = (which_day+1)%7
	year += 1

print (num_sunday,which_day)

