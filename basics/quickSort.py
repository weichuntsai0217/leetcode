def quickSort(nums, reverse=False):
    def _quickSort(nums, left, right):
        if right > left:
            pivotIndex = left
            newPivotIndex = partition(nums, left, right, pivotIndex)
            _quickSort(nums, left, newPivotIndex-1)
            _quickSort(nums, newPivotIndex+1, right)

    def partition(nums, left, right, pivotIndex):
        pivot = nums[pivotIndex]
        nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
        storeIndex = left
        for i in xrange(left, right):
            diff = nums[i] - pivot if not reverse else pivot - nums[i]
            if diff <= 0:
                nums[storeIndex], nums[i] = nums[i], nums[storeIndex]
                storeIndex += 1
        nums[right], nums[storeIndex] = nums[storeIndex], nums[right]
        return storeIndex

    _quickSort(nums, 0, len(nums)-1)


nums = [8, 0, 2, 4, 5,5,1]
quickSort(nums, True)
print nums