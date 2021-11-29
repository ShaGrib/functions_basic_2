def countDown(): #creating function called countDown
    val = [] #creating empty list to hold values of the countdown
    for i in range(5,-1,-1): #stepping backwards from 5 to 0
        val.append(i) #printing each number in the step
    return val

print(countDown()) #calling the function to run and print out the returned value

ml = [1,2] #establishing list with values of 1,2

def priRet(): #creating function called priRet
    print(ml[:1]) #printing all values before the 1st spot
    return(ml[1:]) #printing all values after the 1st spot

print(priRet()) #printing the result of the full function including the return

nl = [1,2,3,4,5] #establishing list with values 1,2,3,4,5

def firPluLi(): #creating function called firPluLi
    n = nl[0] #establishing variable n with the value of nl index of 0 which is 1
    return (n+len(nl)) #returning the value of n plus the length of nl which is a total of 1+5=6(6 is the output)

print(firPluLi()) #printing the result of the full function including the return

def get_list_greater(gl): #creating function called get_list_greater and telling it to take parameter gl
    if len(gl) <2: #checking if the items in the list are less than 2
        return False #returning false if items less than 2
    ngl =[] #establishing ngl empty list
    for g in range(len(gl)): #stepping through each in the length of gl list
        if gl[g] > gl[1]: #checking if the current spot is great than the value of the item in index 1(2nd place)
            ngl.append(gl[g]) #appending the current value to the new list
    print(len(ngl)) #printing length of the new list
    return ngl #returning the values inside the new list

print(get_list_greater([5,2,3,2,1,4])) #offering arguments for the gl list (output will be 5,3,4)
print(get_list_greater([3])) #offering arguments for the gl list (output will be False)

def length_value(leg,val): #creating function ca;;ed length_value that accepts params leg and val
    newval = [] # establishing new  empty list called newval
    for n in range(leg): #stepping through each in the length of leg
        newval.append(val) #appending the value set by val each time to list newval
    return newval #returning the entire list of newval

print(length_value(4,8)) #printing thelength_value call with arguments 4 leg and 8 val
print(length_value(6,3)) #printing thelength_value call with arguments 6 leg and 3 val