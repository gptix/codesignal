def almostIncreasingSequence(sequence):
    
    def find_first_not_greater_than(ls):

        for i  in range(len(ls) - 1):
            if ls[i+1] <= ls[i]:
                return i+1
        return -1
    
    if len(sequence) == 2:
        return True
    
    s = sequence
    
    last_index = len(s) - 1
    
    last_index_lt = find_first_not_greater_than(s)
    
    if (last_index_lt == -1) or (last_index_lt >= last_index-1): # this means it got all the way through
        return True
        
    i = last_index_lt
    print(f'i: {i}')
    
    if s[i-1] < s[i+1]:
        return (find_first_not_greater_than(s[i]) == -1)

    else:
        return False
    
seek = [1, 2, 5, 3, 5]

foo = almostIncreasingSequence(seek)

print(foo)