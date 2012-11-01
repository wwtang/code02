""" Find the path of the robot is to find the avaiable adjacnet spots"""

def isFree(x,y):
    return x>=0 and y>=0

def findPath(x,y):
    path_spots = []

    if x==0 and y==0:
        path_spots.append((0,0))
        return (0,0)
    
    if x >=0 and isFree(x-1,y):
        path_spots.append((x-1,y))
        return findPath(x-1,y)
    
    if y>=0 and isFree(x, y-1):
        path_spots.append((x,y-1))
        return findPath(x, y-1)
    
    return path_spots
    
def main():
    print  findPath(0,0)
    print findPath(1,1)

if __name__=="__main__":
    main()
