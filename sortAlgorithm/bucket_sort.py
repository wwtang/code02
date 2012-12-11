""" bucket sort, distribute sort"""


def bucket_sort(arr):
    count = [0]*len(arr)
    for value in arr:
        count[value] +=1
    arr = []
    for nr, amout in enumerate(count):
        arr.extend([nr]* amount)
    return arr
