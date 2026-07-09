class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        
        low = 1
        high = x
        ans = 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if mid <= x // mid:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans