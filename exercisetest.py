"""ex.10.2

Write a method to sort an array of string so that all the anagrams are next to
each other

"""
arr = ["list",'post',"next","sitl","opts","netx","slit"]

assist_dict = {}

for item in arr:
    item_key = "".join(sorted(item))
    if item_key not in assist_dict:
        assist_dict[item_key] = [item]
    else:
        assist_dict[item_key].append(item)
      
result = [elem  for item in assist_dict.values() for elem in item]
print result   
