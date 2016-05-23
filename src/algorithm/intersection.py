import unittest

def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    s1 = set(nums1)
    s2 = set(nums2)
    return list(s1.intersection(s2))

class IntersectionTest(unittest.TestCase):

    def test_one_intersection(self):
        n1 = [1,2,3,4,5,6]
        n2 = [6,7,8,9]
        self.assertEquals([6], intersection(n1, n2))

    def test_no_intersection(self):
        n1 = [1,2,3]
        n2 = [4,5,6]
        self.assertEquals([], intersection(n1, n2))

if __name__ == '__main__':
    unittest.main()

