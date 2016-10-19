class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s) - len(t)) > 1 or s == t : return False
        if not s and not t: return False
        if not s and len(t) == 1: return True
        if not t and len(s) == 1: return True
        counts = 0
        if len(s) == len(t):
            for i, c in enumerate(s):
                if c != t[i]: counts += 1
                if counts > 1: return False
        else:
            lstr= s if len(s) > len(t) else t
            sstr = t if len(s) > len(t) else s
            for c in sstr:
                if c not in lstr: return False
            ic = chr(sum(map(ord,lstr)) - sum(map(ord,sstr)))
            for i in xrange(len(sstr)+1):
                res = ''
                if i != len(sstr):
                  res = sstr[0:i] + ic + sstr[i:]
                else:
                  res = sstr + ic
                if res == lstr: return True
            return False
        
        return True