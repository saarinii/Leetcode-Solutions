#45. Jump Game II
class Solution:
    def jump(self, nums: List[int]) -> int:
        current_reach = next_reach = steps = 0
        for i, num in enumerate(nums[:-1]):
            next_reach = max(next_reach, i + num)
            if i == current_reach:
                current_reach = next_reach 
                steps += 1
        return steps
