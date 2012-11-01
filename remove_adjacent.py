# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  # +++your code here+++
  return list(set(nums))



# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    result = []
    while len(list1) and len(list2):
        if  list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    
        
  # +++your code here++li+
  
    return result
