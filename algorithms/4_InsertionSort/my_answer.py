
def insertion_sort_median(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor
        lower_middle=(i)//2
        if i%2==1: #Even sorted list
            out=((elements[lower_middle]+elements[lower_middle+1])/2)
        else: #Odd sorted list
            out=elements[lower_middle]
        print(out)    
        x=0

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    insertion_sort_median(elements)
    print(elements)
    #
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        insertion_sort_median(elements)
        print(f'sorted array: {elements}')