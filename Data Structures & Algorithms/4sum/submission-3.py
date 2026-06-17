from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []

        def kSum(k, start, target):
            # Base Case: When we've boiled it down to a 2Sum problem
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    current_sum = nums[l] + nums[r]
                    if current_sum < target:
                        l += 1
                    elif current_sum > target:
                        r -= 1
                    else:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                return  # Safely exit the 2Sum frame

            # Recursive Case: Fix one number, reduce to (k-1)Sum
            for i in range(start, len(nums) - k + 1):
                # Fix: Skip duplicate values for the current position 'i'
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()  # Backtrack
            
            # The function naturally returns here after checking ALL 'i' values

        kSum(4, 0, target)
        return res