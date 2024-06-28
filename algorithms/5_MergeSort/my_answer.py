def merge_sort(elements, key, descending=False):
    size=len(elements)
    if len(elements) <= 1:
        return elements
    left_sorted = merge_sort(elements[0:size//2], key, descending)
    right_sorted = merge_sort(elements[size//2:], key, descending)
    return merge(left_sorted, right_sorted, key, descending)

def merge(left_list, right_list, key, descending=False):
    merged=[]
    operator=lambda x,y,desc: x>=y if desc else x<=y
    while 0<len(left_list) and 0<len(right_list):
        if operator(left_list[0][key], right_list[0][key], descending):
            merged.append(left_list.pop(0))
        else:
            merged.append(right_list.pop(0))    
    merged.extend(left_list)
    merged.extend(right_list)        
    return merged        

if __name__ == '__main__':
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    sorted_list = merge_sort(elements, key='age', descending=True)
    for e in sorted_list:
        print(e)
