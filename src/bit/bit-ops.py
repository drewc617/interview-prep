def getBit(num, i):
  """
  Create a 00000100 integer AND with number. Compare that with 
  0, if it's zero then bit is not set. 
  :type num: Int
  :type i: ith bit of the binary representation of Integer num
  :rtype: boolean value {True,False} if bit is present
  """
  return num & (1 << i) != 0


# print getBit(5, 0) # True, bin(5) = 0b101
# print getBit(10, 0) # False, bin(10) = 0b1010

def setBit(num, i):
  """
  Create a 00000100 integer at bit i and OR with number
  :type num: Int
  :type i: ith bit of the binary representation of Integer num
  :rtype: Int value of the bit set
  """
  return num | (1 << i)

def clearBit(num, i):
  mask = ~ (1 << i)
  return num & mask

def numBitsSet(num):
  bString = bin(num)[2:]
  return bString.count('1')  

def binaryInt(num):
  """
  Create a String representation of an unsigned Integer
  :type: Unsigned integer
  :rtype: Binary String representation of an Integer
  """
  binaryString = []
  while num > 0:
    binaryString.append(num % 2)
    num = num / 2
  ans = ""
  for i in range(len(binaryString)-1, -1, -1):
    ans += str(binaryString[i])
  return ans

print binaryInt(10)
print binaryInt(1)
print binaryInt(0)
print binaryInt(7654)


