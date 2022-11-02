import math

d = [0,40,60,80,90,100]
def binary_search(my_list, test_num):
    
    first = 0
    last = len(my_list)-1
    medium = math.floor((first + last)/2)
    found = False

    while found == False:
        #for numbers in my_list:
            if (first <= last and found == False) :
                    if (test_num == d[medium]):
                        found = True
                        return True
                    if (test_num > d[medium]):
                        first = medium + 1
                        medium = math.floor((first + last)/2)
                        b_list = [range(first, last)]
                        if (test_num in b_list):
                            found = True
                            return True
                    if (test_num < d[medium]):
                        last = medium - 1
                        medium = math.floor((first + last)/2)
                        b_list = [range(first, last)]
                        if (test_num in b_list):
                            found = True
                            return True
            else:
                return False

print(binary_search(d, 90000))           
