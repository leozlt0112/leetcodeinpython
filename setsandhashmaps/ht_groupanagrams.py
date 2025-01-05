# WRITE GROUP_ANAGRAMS FUNCTION HERE #
#                                    #
#                                    #
#                                    #
#                                    #
######################################

def group_anagrams(strings):
    dictionary_sorted = {}
    for s in strings:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in dictionary_sorted:
            dictionary_sorted[sorted_s] = []
            dictionary_sorted[sorted_s].append(s)
        else:
            dictionary_sorted[sorted_s].append(s)
    return list(dictionary_sorted.values())


print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""