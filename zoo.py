zoo = ['lion','tiger','leapard','leopard','eagle','phoenix','peacock','dragon']
new_animal = raw_input("Check the animal in the zoo by name, animla name: \t" )
if new_animal in zoo:
    print new_animal, " is in the zoo\n"
else:
    print"add ",new_animal, " into the zoo."
    zoo.append(new_animal)
    print zoo
    
zoo.reverse()
new_zoo=zoo[:]
zoo.sort()
print new_zoo, "\n", zoo
for animals in zoo:
    print animals,"*\n"
