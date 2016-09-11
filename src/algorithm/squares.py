
def isPerfectSquare(number):
    mid = (number + 1 )/ 2
    for i in range(mid, 0, -1):
        if i*i is number: return True
    return False

print isPerfectSquare(10)
print isPerfectSquare(100)
print isPerfectSquare(121)
print isPerfectSquare(11413)
print isPerfectSquare(1)
print isPerfectSquare(0)