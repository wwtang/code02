"""

Time class
"""

class Time(object):
	def __init__(self,hour=0,minute=0,second=0):
		self.hour = hour
		self.minute	= minute
		self.second = second

	#__str__
	def __str__(self):
		return "%.2d: %.2d: %.2d"%(self.hour, self.minute, self.second)

	def __add__(self,other):
		seconds  = self.timeToInt() + other.timeToInt()
		return int_to_time(seconds)

	#print
	def printTime(self):
		print  "%.2d: %.2d:  %.2d"%(self.hour, self.minute, self.second)
		
	# timeToInt()
	def timeToInt(self):
		"""
		convert time into seconds since midnight 
		"""
		mins = self.hour * 60
		seconds = (mins+self.minute)*60
		return self.second + seconds
	#add second
	def addSecond(self,sec):
		"""
		(Time, int) -->Time
		t is
		"""
		second = self.timeToInt()
		totalSec = second+sec
		
		t = int_to_time(totalSec)
		return t


	def printTime1(self):
		return str(self)

	

def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time



