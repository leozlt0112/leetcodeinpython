# WRITE SUBARRAY_SUM FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################

def subarray_sum(nums, target):
    curr_sum_array = {0:-1}
    # key current_Sum
    # value the index which the curr_Sum is 
    curr_sum=0
    for i, value in enumerate(nums):
        curr_sum +=value
        if (curr_sum- target) not in curr_sum_array:
            curr_sum_array[curr_sum] = i
        else:
            result = [curr_sum_array[curr_sum- target]+1,i]
            return result
    return []
            


nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
