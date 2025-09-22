class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l ,r, m = 0,0, len(nums)-1

        while m >= 0 and nums[m] == 2:
            m -= 1
        
        while l <= m:

            if nums[l] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            elif nums[l] == 1:
                l += 1
               
            elif nums[l] == 2:
                nums[l], nums[m] = nums[m], nums[l]
                m -= 1

        return nums