class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zi = 0 #zero indicator
        for nzf in range(len(nums)): #nzf is non zero indicator
            if nums[zi] == 0 and nums[nzf]!=0:
                nums[zi] , nums[nzf] = nums[nzf], nums[zi]
                zi+=1
            elif nums[zi]!=0:
                zi+=1
