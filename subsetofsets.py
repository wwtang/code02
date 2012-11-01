"""
find all the subsets of a set
input a list of integer
output a list of list
"""

def updatelist(pre_list,n):
    for item in pre_list:  #update the new elem for each subset of the sub_list
        item.append(n)
    return pre_list
        
def allSubset(n):
    subset_list = []
    if n==0: #empty set
        subset_list.append([])
        return subset_list
    else:
        cache_list = []
        pre_list = allSubset(n-1)#cache the prior sub_list
        cache_list = pre_list[:]

        #update the pre_list with new element
        updated_list = updatelist(pre_list,n)

        # consist the new subset_list
        subset_list = updated_list + allSubset(n-1)
    return sorted(subset_list)

def test(got, expected):
    if got == expected:
        print "OK"
    else:
        print "No"
        print "got: ",got, " but expected: ", expected
def main():
    test(allSubset(0),[[]])
    test(allSubset(1),[[],[1]])
    test(allSubset(2),[[],[1],[1,2],[2]])
    test(allSubset(3),[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]])

if __name__=="__main__":
    main()
    
