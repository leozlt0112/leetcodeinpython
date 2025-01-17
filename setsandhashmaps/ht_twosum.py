# WRITE TWO_SUM FUNCTION HERE #
#                             #
#                             #
#                             #
#                             #
###############################
def two_sum(input_array, target):
    dict_two_sum={}
    for value in input_array:
        if (target - value) in dict_two_sum:
            return ([dict_two_sum[target - value],input_array.index(value)])
        else:
            dict_two_sum[value]=input_array.index(value)
    return []
    
    
print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 2,11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 4]
    [1, 3]
    [0, 3]
    [1, 3]
    []
    [2, 3]
    [0, 1]
    []

"""


