def merge_sort(array):
    if len(array) <= 1:
        return array
    
    median_index = len(array) // 2
    list_1 = array[:median_index]
    list_2 = array[median_index:]
    
    list_1.sort()
    list_2.sort()
    
    sorted_list = []
    i = j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            sorted_list.append(list_1[i])
            i += 1
        else:
            sorted_list.append(list_2[j])
            j += 1
    
    sorted_list.extend(list_1[i:])
    sorted_list.extend(list_2[j:])
    
    return sorted_list

array = [1, 5, 7, 8, 4, 9]
sorted_array = merge_sort(array)
print("Sorted Array:", sorted_array)
