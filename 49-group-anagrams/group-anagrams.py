class Solution(object):
    def groupAnagrams(self, strs):
        grp=defaultdict(list)
        result=[]
        for s in (strs):
            sorteds=tuple(sorted(s))
            grp[sorteds].append(s)
        for value in grp.values():
            result.append(value)
        return result
