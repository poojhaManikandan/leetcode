class Solution(object):
    def maxSubarrayLength(self, nums, k):
        freq = {}
        maxlen = 0
        i = 0

        for j in range(len(nums)):
            freq[nums[j]] = freq.get(nums[j], 0) + 1

            while freq[nums[j]] > k:
                freq[nums[i]] -= 1
                i += 1

            maxlen = max(maxlen, j - i + 1)

        return maxlen



            

        
        