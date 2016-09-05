def selectionSort(nums, reverse=False):
    length = len(nums)
    if length <= 1: return
    for i in xrange(length):
        mx = i # mx is min index or max index based on reverse
        for j in xrange(i+1,length):
            diff = nums[j] - nums[mx] if not reverse else nums[mx] - nums[j]
            if diff < 0: mx = j
        nums[i], nums[mx] = nums[mx], nums[i]

nums = [8, 0, 2, 4, 5,5,1]
selectionSort(nums, False)
print nums