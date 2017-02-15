class Clock(object):
	def __init__(self, hrs, mins):
		self.mins = mins % 60
		self.hrs = (hrs + mins//60) % 24

	def __str__(self):
		return self.to_hours(self.hrs)+":"+self.to_minutes(self.mins)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	def to_hours(self, hours):
		reduced = hours % 24
		return "0"+str(reduced) if reduced < 10 else str(reduced)

	def to_minutes(self, minutes):
		reduced = minutes % 60
		return "0"+str(reduced) if reduced < 10 else str(reduced)

	def add(self, minutes):
		new_minutes = minutes % 60
		new_hours = (self.mins + minutes)//60
		return self.to_hours(self.hrs + new_hours)+":"+self.to_minutes(self.mins+ new_minutes)