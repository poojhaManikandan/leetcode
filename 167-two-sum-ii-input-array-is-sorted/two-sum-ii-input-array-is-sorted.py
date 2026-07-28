class Solution(object):
    def twoSum(self, numbers, target):
        m=0
        n=len(numbers)-1
        while m<n:
            if numbers[m]+numbers[n]==target:
                return m+1,n+1
            elif numbers[m]+numbers[n]<target:
                m+=1
            else:
                n-=1

        