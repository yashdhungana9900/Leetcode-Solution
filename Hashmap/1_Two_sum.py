#Leetcode : 1
#Hashmap
#easy

class Solution(object):
    def twoSum(self, nums, target):

          hash_map = {}

          for i in range(len(nums)):

            complement = target - nums[i]

            if complement in hash_map:
                return [hash_map[complement], i]

            hash_map[nums[i]] = i



