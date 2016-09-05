def bubbleSort(nums, reverse=False):
    if len(nums) <=1: return
    length = len(nums)
    for i in xrange(length): # the number of sub-arrays
        for j in xrange(length-i-1): # each sub array has length-i-1 pairs
            diff = nums[j] - nums[j+1] if not reverse else nums[j+1] - nums[j]
            if diff > 0:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            

nums = [5,4,6,3,1]
bubbleSort(nums, False)
print 'Ascending: ', nums
print '====='
bubbleSort(nums, True)
print 'Descending: ', nums
