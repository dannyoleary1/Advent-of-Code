import fileinput

lines = list(fileinput.input("input.txt"))
exactly_twice = 0 
exactly_thrice = 0

def check_counts():
    global exactly_twice
    global exactly_thrice
    for line in lines:
        test_string = line
        test_list = list(test_string)
        test_set = set(test_list)

        already_thrice = False
        already_twice = False
        for key in test_set:    
            if test_string.count(key) is 3 and already_thrice is False:
                exactly_thrice +=1
                already_thrice = True
            elif test_string.count(key) is 2 and already_twice is False:
                exactly_twice +=1
                already_twice = True



check_counts()
print (exactly_twice*exactly_thrice)
   
