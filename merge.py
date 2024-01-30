#Two sorted list are entered into the function and pointer to the first elements of the list then it moves forward and compares.

def merge(my_list1, my_list2):
    combined = []
    i = 0
    j =0

    while i < len(my_list1) and j < len(my_list2):
        if my_list1[i] < my_list2[j]:
            combined.append(my_list1[i])
            i +=1
        else:
            combined.append(my_list2[j])
            j +=1
    
    while i < len(my_list1):
        combined.append(my_list1[i])
        i +=1

    while j < len(my_list2):
        combined.append(my_list1[i])
        j+=1
    return combined


print(merge([1,5,9], [2,3]))




 