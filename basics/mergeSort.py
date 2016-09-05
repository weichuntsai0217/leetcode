def mergeSort(nums, reverse=False):
    def merge(left, right):
        i, j = 0, 0
        res = []
        while i < len(left) and j < len(right):
            diff = left[i] - right[j] if not reverse else right[j] - left[i]
            item = None
            if diff < 0:
                item = left[i]
                i += 1
            else:
                item = right[j]
                j += 1
            res.append(item)
        if i < len(left): res += left[i:len(left)]
        if j < len(right): res += right[j:len(right)]
        return res
    if len(nums) <= 1: return nums
    midIdx = len(nums)/2
    left = mergeSort(nums[:midIdx], reverse)
    right = mergeSort(nums[midIdx:], reverse)
    return merge(left, right)

nums = [8, 0, 2, 4, 5,5,1]
nums = mergeSort(nums)
print nums