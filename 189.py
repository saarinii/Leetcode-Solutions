#189. Rotate Array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k != 0:
            nums.insert(0, nums[-1])
            nums.pop()
            k -= 1
        """
        Do not return anything, modify nums in-place instead.
        """
        