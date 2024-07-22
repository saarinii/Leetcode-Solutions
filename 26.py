#26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        s1 = len(nums)
        s2 = len(s)
        for i in range(s2):
            if nums[i] != s[i]:
                nums[i] = s[i]
        for i in range(s2, s1):
            if len(nums) != s2:
                nums.pop()


        
        