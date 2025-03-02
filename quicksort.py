def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    greater_items = []
    lower_items = []

    for item in sequence:
        if item > pivot:
            greater_items.append(item)
        else:
            lower_items.append(item)

    return quick_sort(greater_items)+[pivot]+quick_sort(lower_items)





