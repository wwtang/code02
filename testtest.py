a_dict = {1:11,2:22,3:33,4:44,5:55,6:66,7:77,8:88,9:99}
count = 0
for item in a_dict:
    print item
    count +=1
    while count==3:
        print "*"*10
        count = 0
