def reverse(str):
    """
    Reverse a given String
    Don't use reversed
    :type str: String
    :rtype: String
    """
    ans=''
    for i in range(len(str)-1, -1, -1):
        ans+= str[i]
    return ans

print reverse("apple")
print reverse("jack")
