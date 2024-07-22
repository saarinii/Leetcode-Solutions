#169. Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        
        # Count the occurrences of each element
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        # Find the element with the maximum count
        majority_element = max(counts, key=counts.get)
        
        return majority_element