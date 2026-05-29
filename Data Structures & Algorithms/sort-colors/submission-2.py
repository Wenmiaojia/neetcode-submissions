class Solution:
    def sortColors(self, nums: list[int]) -> None:
        l = 0
        r = len(nums) - 1
        i = 0
        
        def swap(a, b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp

        while i <= r:  # Fixed: changed 'right' to 'r'
            if nums[i] == 0:
                swap(i, l)
                l += 1
                i += 1  # Explicitly move forward; we know what we swapped in
            elif nums[i] == 2:
                swap(i, r)
                r -= 1  # Do NOT touch i. Let the loop inspect the newly swapped element.
            else:
                # This is explicitly for nums[i] == 1
                i += 1  # Move forward because 1s belong in the middle