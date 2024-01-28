#It startes with second element(index =1) then the second element gets compared to the first then third to the second
def insertion_sort(my_list):
    for i in range(1,len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp<  my_list[j] and j>-1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j-=1
    return my_list


print(insertion_sort([5,1,8,9,10]))