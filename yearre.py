import re
import sys

def year_pattern(filename):
#read the html file as input_file
    try:
        input_file = open(filename)
    except IOError:
        print "Could not open the file"
        sys.exit()
    
# set the re pattern
 
    pattern = re.compile("Popularity in (\d{4})")
    for line in input_file:
        popularity_year = pattern.search(line)
        if popularity_year:
            print popularity_year.group(1)
#Extract the names and rank numbers and just print them

def nameRankPattern(filename):
    try:
        input_file = open(filename)
    except IOError:
        print "Could not open the file"
        sys.exit()
    boyRank_dict = {}
    girlRank_dict = {}
#<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
#<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
#<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td    
       
    #rankPattern = re.compile("<td>(\d+)</td>")
    #namePattern = re.compile("<td>(\w+)</td><td>(\w+)</td>")
    for line in input_file:
        result = re.search("<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>",line)
        #rank = rankPattern.search(line)
        #name = namePattern.search(line)
        if result:
            #print "rank: ", result.group(1), "\t", "Boy's name: ", result.group(2),    "\t" , "Girls name: ", result.group(3)
            boyRank_dict[result.group(2)] = result.group(1)
            girlRank_dict[result.group(3)] = result.group(1)
    for boy in boyRank_dict:
        print boy, boyRank_dict[boy], "\n"
