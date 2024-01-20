def remove_duplicates(sequence):
    #We use a set (seen) to keep track of unique elements encountered.
    seen = set()
    result = []

    for item in sequence:
        #If the item is not in the set, we add it to both the set and the result sequence.
        if item not in seen:
            seen.add(item)
            result.append(item)
#The result sequence will contain only the unique elements from the original sequence, maintaining their order.
    return result

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result) 