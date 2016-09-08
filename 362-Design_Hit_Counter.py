"""
* Ref: https://discuss.leetcode.com/topic/48788/48ms-python-concise-solution
* Key points: 
* Explain your thought:
* Compute complexity:
  - Time complexity:
  - Space complexity: O(n)
"""
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not len(self.hits) or timestamp != self.hits[-1][0]:
            self.hits.append([timestamp, 1])
        else:
            self.hits[-1][1] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        sum = 0
        for i in xrange(len(self.hits)-1, -1, -1):
            if self.hits[i][0] + 300 <= timestamp: break
            sum += self.hits[i][1]
        return sum


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)