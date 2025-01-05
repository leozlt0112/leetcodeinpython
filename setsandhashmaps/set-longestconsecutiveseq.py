# WRITE LONGEST_CONSECUTIVE_SEQUENCE FUNCTION HERE #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
####################################################


def longest_consecutive_sequence(arr1):
    # Use a set to store unique elements for O(1) lookup
    num_set = set(arr1)
    longest_streak = 0
    for num in num_set:
        curr_seq = 0
        if num -1 not in num_set:
            curr_seq +=1
            num = num+1
            while num in num_set:
                curr_seq +=1
                num = num +1
            longest_streak = max(curr_seq,longest_streak)
        curr_seq = 1   
        longest_streak = max(curr_seq,longest_streak)
    return longest_streak    
print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""