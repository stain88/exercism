from datetime import date, timedelta

def next_day(d, weekday):
	return d + timedelta((weekday - d.weekday()) % 7)

def previous_day(d, weekday):
	return d - timedelta((d.weekday() - weekday) % 7)

def last_day_of_month(year, month):
	next_month = date(year,month,28) + timedelta(days=4)
	return next_month - timedelta(days=next_month.day)

def get_day_num(day):
	if day == "Monday":
		return 0
	elif day == "Tuesday":
		return 1
	elif day == "Wednesday":
		return 2
	elif day == "Thursday":
		return 3
	elif day == "Friday":
		return 4
	elif day == "Saturday":
		return 5
	elif day == "Sunday":
		return 6

def meetup_day(year, month, day, when):
	tmp_day = get_day_num(day)
	if when == "1st":
		tmp_date = date(year,month,1)
		if tmp_date.weekday() == tmp_day:
			return tmp_date
		else:
			return next_day(tmp_date, tmp_day)
	elif when == "teenth":
		tmp_date = date(year,month,12)
		return next_day(tmp_date, tmp_day)
	elif when == "2nd":
		tmp_date = date(year,month,8)
		if tmp_date.weekday() == tmp_day:
			return tmp_date
		else:
			return next_day(tmp_date, tmp_day)
	elif when == "3rd":
		tmp_date = date(year,month,15)
		if tmp_date.weekday() == tmp_day:
			return tmp_date
		else:
			return next_day(tmp_date, tmp_day)
	elif when == "4th":
		tmp_date = date(year,month,22)
		if tmp_date.weekday() == tmp_day:
			return tmp_date
		else:
			return next_day(tmp_date, tmp_day)
	elif when == "5th":
		tmp_date = date(year,month,29)
		if tmp_date.weekday() == tmp_day:
			return tmp_date
		else:
			return next_day(tmp_date, tmp_day)
	elif when == "last":
		tmp_date = last_day_of_month(year, month)
		if tmp_date.weekday() == tmp_day:
			return tmp_date
		else:
			return previous_day(tmp_date, tmp_day)

