#leetcode 643

class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum=0
        #first window
        for i in range(k):
            window_sum+=nums[i]
        max_sum=window_sum
        #slide the window
        for i in range(k,len(nums)):
            window_sum-=nums[i-k]
            window_sum+=nums[i]    
            max_sum=max(max_sum,window_sum)
        return max_sum / float(k)       

       
        