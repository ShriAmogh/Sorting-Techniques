#In this sorting method the first element is compared to every element in the a list if it found an element less than it.
# Then it will swp its position.
def selection_sort(my_list):
    for i in range(0,len(my_list)-1,1):
        #0
        min_index = i
        for j in range(min_index,len(my_list)-1):
            if my_list[min_index]>my_list[j+1]:
                my_list[min_index], my_list[j+1]= my_list[j+1], my_list[min_index]
    return my_list


print(selection_sort([1,8,5,90,910]))


