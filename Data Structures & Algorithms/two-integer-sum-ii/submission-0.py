from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1. Corrected right pointer initialization
        l, r = 0, len(numbers) - 1
        
        # 2. Safe loop condition to prevent infinite loops
        while l < r:
            current_sum = numbers[l] + numbers[r]
            
            if current_sum == target:
                # 3. Returning 1-indexed positions
                return [l + 1, r + 1]
            elif current_sum > target:
                r -= 1
            else:
                l += 1
                
        return []  # Return empty if no pair is found