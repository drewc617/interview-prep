import random as r
def rand_list(length):
    """
    Randomly generate a list of integers
    :type length: int
    :rtype: List[int]
    """
    ans = []
    for x in range(length):
        ans.append(r.randrange(length))

    return ans


print rand_list(10)
print rand_list(11)
print rand_list(12)
