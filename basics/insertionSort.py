def insertionSort(nums, reverse=False):
    if len(nums) <= 1: return
    length = len(nums)
    for i in xrange(length-1):
        for j in xrange(i+1,0,-1):
            diff = nums[j-1] - nums[j] if not reverse else nums[j] - nums[j-1]
            if diff > 0:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            else:
                break

nums = [29,10,14,37,13]
insertionSort(nums, False)
print 'Ascending: ', nums
print '====='
insertionSort(nums, True)
print 'Descending: ', nums