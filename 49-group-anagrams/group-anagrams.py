class Solution(object):
    def groupAnagrams(self, strs):
        grp={}
        for i in strs:
            key="".join(sorted(i))
            if key not in grp:
                grp[key]=[]
            grp[key].append(i)
        return grp.values()