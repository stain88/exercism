NORTH = "north"
EAST = "east"
SOUTH = "south"
WEST = "west"
class Robot():
	def __init__(self, bearing = NORTH, x = 0, y = 0):
		self.bearing = bearing
		self.coordinates = (x, y)

	def turn_right(self):
		if self.bearing == NORTH:
			self.bearing = EAST
		elif self.bearing == EAST:
			self.bearing = SOUTH
		elif self.bearing == SOUTH:
			self.bearing = WEST
		elif self.bearing == WEST:
			self.bearing = NORTH

	def turn_left(self):
		if self.bearing == NORTH:
			self.bearing = WEST
		elif self.bearing == WEST:
			self.bearing = SOUTH
		elif self.bearing == SOUTH:
			self.bearing = EAST
		elif self.bearing == EAST:
			self.bearing = NORTH

	def advance(self):
		if self.bearing == NORTH:
			self.coordinates = (self.coordinates[0],self.coordinates[1] + 1)
		elif self.bearing == EAST:
			self.coordinates = (self.coordinates[0] + 1,self.coordinates[1])
		elif self.bearing == SOUTH:
			self.coordinates = (self.coordinates[0],self.coordinates[1] - 1)
		elif self.bearing == WEST:
			self.coordinates = (self.coordinates[0] - 1,self.coordinates[1])

	def simulate(self, commands):
		for cmd in commands:
			if cmd == "A":
				self.advance()
			elif cmd == "R":
				self.turn_right()
			elif cmd == "L":
				self.turn_left()
