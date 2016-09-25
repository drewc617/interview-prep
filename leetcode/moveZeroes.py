def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    lastNonZeroIndex = -1
    for i in range(len(nums)):
        if nums[i] != 0:
            lastNonZeroIndex += 1
            nums[lastNonZeroIndex], nums[i] = nums[i], nums[lastNonZeroIndex]
        print nums

moveZeroes([0, 1, 3, 4, 0, 12, 0])
moveZeroes([1, 3, 4, 0, 0])
