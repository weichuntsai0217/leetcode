"""
* Ref: https://discuss.leetcode.com/topic/47843/1-line-ruby-2-lines-python
* Key points: Reflect the points by replacing every x with minX+maxX-x and
      then check whether you get the same points.
* Explain your thought:
  - Reflect the points by replacing every x with minX+maxX-x and then
    check whether you get the same points.
    Note: if p = (x,y) and p has a reflected point p' = (x', y'),
          assume x < x', then x - Xmin = Xmax - x' and y = y', and
          we can get that x' = Xmin + Xmax - x (or x = Xmin + Xmax - x' )
* Compute complexity:
  - Time complexity: O(n)
  - Space complexity: O(n)
"""
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        points = sorted(set(map(tuple, points)))

        # Replacing every x with minX+maxX-x, and
        # check if the set of points is the same
        return points == sorted((points[0][0] + points[-1][0] - x, y)
                                for x, y in points)
            