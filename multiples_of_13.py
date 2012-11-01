zoo = ["monkey","tiger","lion",'parrot']
print "The zoo has the following animals: ", zoo

num = input("Which number of anmals would you like to delete?\
Input the number: ")
if  0 <= num <len(zoo):
    del zoo[num]
    print"Now, the animals in the zoo are \t",zoo
else:
    print"the number is out of range!"
    print "The zoo has the following animals :\t", zoo

new_animal = raw_input("Which animal would you like to remove?\
input the name of the animal\n")
if new_animal in zoo:
    zoo.remove(new_animal)
    print "new_animal", new_animal, " was removed from the zoo\n"
    print "Now the following animals are in the zoo:\n",zoo
else:
    print "no such animal in the zoo"

