class Solution(object):
    def majorityElement(self, nums):
        dict={}
        for i in nums:
            if i in dict:
                dict[i]=dict[i]+1
            else:
                dict[i]=1
        return max(dict,key=dict.get)
