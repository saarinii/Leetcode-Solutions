#55. Jump Game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for index, jump_length in enumerate(nums):
            if m < index:
                return False
            m = max(m, index+jump_length)
        return True