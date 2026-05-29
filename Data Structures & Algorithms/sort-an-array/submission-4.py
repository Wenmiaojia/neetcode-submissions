class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # Base case: an array of size 0 or 1 is already sorted
        if len(nums) <= 1:
            return nums
        
        # 1. Divide: Find the midpoint and split the array
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        # 2 & 3. Conquer and Combine: Merge the two sorted halves
        return self.merge(left_half, right_half)
    
    def merge(self, left: list[int], right: list[int]) -> list[int]:
        sorted_array = []
        i = j = 0
        
        # Compare elements from both halves and push the smaller one
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
                
        # If there are remaining elements in left or right, append them
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])
        
        return sorted_array