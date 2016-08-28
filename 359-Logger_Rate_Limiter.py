"""
* Ref:  https://discuss.leetcode.com/topic/48359/short-c-java-python-bit-different/2
* Key points:
* Explain your thought:
  - If the message should be printed, set a timeout limit for this message.
    When another message comes and its content is the same as 
    some printed message with some timeout limit,
    check if the current timestamp is smaller than the timeout limit.
    If yes, return False
* Compute complexity:
  - Time complexity: O(1) for each method called
  - Space complexity:
"""
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ok = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if timestamp < self.ok.get(message, 0):
            return False
        self.ok[message] = timestamp + 10
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)