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
        from collections import deque
        
        self.num_of_hits = 0 # record the total hits
        self.time_hits = deque()  # record the hits sequence
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not self.time_hits or self.time_hits[-1][0] != timestamp:
            # for the hit which is the first hit in the current timestamp
            self.time_hits.append([timestamp, 1])
        else:
            # for the hit which is not the first hit in the current timestamp
            self.time_hits[-1][1] += 1
        
        # Add this hit to the total hits
        self.num_of_hits += 1
                
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.time_hits and self.time_hits[0][0] <= timestamp - 300:
            # If the timestamp is less than the current timestamp -300, remove
            self.num_of_hits -= self.time_hits.popleft()[1]

        # We always leave the number of hits in the latest 5 mins
        return self.num_of_hits 


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)