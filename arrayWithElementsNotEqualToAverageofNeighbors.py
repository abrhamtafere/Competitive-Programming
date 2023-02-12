class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        def check(nums):
            for i in range(1, len(nums)-1):
                if (nums[i-1] + nums[i+1]) / 2 == nums[i]:
                    return False
            return True
        while not check(nums):
            for i in range(1, len(nums)-1):
                if (nums[i-1] + nums[i+1]) / 2 == nums[i]:
                    swap(nums, i-1, i)
        return nums
