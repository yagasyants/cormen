from sorting import min_heap


def _create_paired_holder(list_ints, index):
    el = list_ints[index]
    list_index = list_ints, index
    return min_heap.PairHolder(el, list_index)

def merge_sorted(list_of_sorted_lists):
    merged_list = []
    heap = min_heap.MinHeap()
    for list_ints in list_of_sorted_lists:
        paired_holder = _create_paired_holder(list_ints, 0)
        heap.insert(paired_holder)
    
    while heap.size() > 0 :
        paired_holder = heap.extract_min()
        el = paired_holder.val
        list_index = paired_holder.holded_val

        list_ints = list_index[0]
        index = list_index[1]
        
        merged_list.append(el)
        
        if index < len(list_ints) - 1:
            index +=1
            heap.insert(_create_paired_holder(list_ints, index))
    
    return merged_list
