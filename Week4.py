def bubble_sort(my_list):
    for index in range(len(my_list) - 1):
        counter = index
        for number in my_list:
            if my_list[counter] > my_list[counter + 1]:
                my_list[counter], my_list[counter + 1] = my_list[counter + 1], my_list[counter]
                
                
    print(my_list)
d = [54,26,93,17,77,31]
print(bubble_sort(d)) 