class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def sortedStr(s):
            return ''.join(sorted(list(s)))
        sortedStrs = [ sortedStr(s) for s in strs ]
        groups = {}
        for i, ss in enumerate(sortedStrs):
            if ss not in groups:
                groups[ss] = []
            groups[ss].append(strs[i])
        return [ groups[k] for k in groups ]