"""
* Ref: No
* Key points: 
* Explain your thought:
  - Initialize an array containing 0 to maxNumbers - 1
  - when we call get method,
    pop the 1st element of the array if the array is not empty.
  - when we call check method, just check if the number is in the array
  - when we call release,
    append the number into the array if this number is not in the array
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""

class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.nums = range(maxNumbers)

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if not len(self.nums): return -1
        return self.nums.pop()        

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.nums

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if number not in self.nums:
            self.nums.append(number)
        

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)