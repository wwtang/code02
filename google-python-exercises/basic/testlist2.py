def remove_adjacent(nums):
  dup_index = []
  for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
      dup_index.append(i)

  result =[]
  for i in range(len(nums)):
      if i not in dup_index:
        result.append(nums[i])
  # +++your code here+++
  return result


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  helper = []
  l1 = 0
  l2 = 0
  while l1 < len(list1) and l2 < len(list2):
    if list1[l1] <= list2[l2]:
      helper.append(list1[l1])
      l1 +=1
    else:
      helper.append(list2[l2])
      l2 +=1
  while l1 < len(list1):
    helper.append(list1[l1])
    l1+=1
  while l2 < len(list2):
    helper.append(list2[l2])
    l2 +=1

  # +++your code here+++
  return helper

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()