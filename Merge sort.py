import random
lis = [[random.randint(0,100)] for i in range(10)] # List of numbers to sort
length = len(lis)
print(lis)

def even(lis,temp1,c): # sorts and even number of arrays in 2d array lis
    c = 0 # array number
    for i in range(len(lis)//2):
        temp = []    # used as placeholder for sorted elements
        a = len(lis[c]) + len(lis[c+1]) 
        while len(temp) != a:
            if lis[c] != [] and lis[c+1] != []: # check empty
                if lis[c][0] <= lis[c+1][0]:     # actual sorting
                    temp.append(lis[c][0])
                    del lis[c][0]
                else :
                    temp.append(lis[c+1][0])
                    del lis[c+1][0]
            else:
                # Make it possible to append to temp as integers without generators
                if lis[c] == []:   # if empty add to temp
                    for i in lis[c+1]:
                        temp.append(i)
                else:
                    for i in lis[c]:
                        temp.append(i)
        temp1.append(temp)
        c = c + 2
    return temp1

while len(lis) != 1:
    c = 0
    temp1 = [] # Placeholder for lis while sorting
    if len(lis) % 2 == 0 : # even
        temp1 = even(lis,temp1,c)
    else: # odd
        a = lis[0]   # removes first array to make it even 
        del lis[0] 
        temp1 = even(lis,temp1,c)
        temp1.append(a)
    lis = temp1[:] 
    print(lis)
print(lis)
            
