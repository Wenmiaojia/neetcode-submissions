class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            # If the current number matches the candidate, boost its count.
            # Otherwise, decrement the count (canceling it out).
            count += 1 if num == candidate else -1
            
        return candidate