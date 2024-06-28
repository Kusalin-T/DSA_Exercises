# 1)Binary Search required ordered list

numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15 

def binary_search(elems, target, left_index, right_index):
    if right_index<left_index:
        return -1
    
    middle_index = (left_index + right_index)//2
    elem = elems[middle_index]

    if elem==target:
        return middle_index
    elif elem<target:
        return binary_search(elems, target, left_index, middle_index-1)
    else:
        return binary_search(elems, target, middle_index+1, right_index)
    
def find_all_occurances(elems, target):
    initial=binary_search(elems, target, 0, len(elems)-1)
    idxs=[initial]

    current=initial-1
    while current>0:
        if elems[current]==target:
            idxs.append(current)
            current-=1
        else:
            break    

    current=initial+1
    while current<len(elems):
        if elems[current]==target:
            idxs.append(current)
            current+=1
        else:
            break   

    return sorted(idxs)    

print(find_all_occurances(numbers, number_to_find))