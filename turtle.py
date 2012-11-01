from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()


def firstAction():
	fd(bob, 100)
	lt(bob)
	fd(bob, 100)
	lt(bob)
	fd(bob, 100)
	lt(bob)
	fd(bob, 100)


#wait_for_user()


def forwardAndTurnLeft():
	fd(bob, 100)
	lt(bob)


def main():
	for i in range(3):
		forwardAndTurnLeft()
	wait_for_user()

if __name__=="__main__":
	main()