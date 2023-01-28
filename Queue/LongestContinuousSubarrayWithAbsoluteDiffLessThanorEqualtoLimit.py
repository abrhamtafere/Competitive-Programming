class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxm = []
        minm = []
        i = 0
        for j in range(len(nums)):
            while maxm and nums[j] > maxm[-1]:
                maxm.pop()
            while minm and nums[j] < minm[-1]:
                minm.pop()
            maxm.append(nums[j])
            minm.append(nums[j])
            if maxm[0] - minm[0] > limit:
                if maxm[0] == nums[i]:
                    maxm.pop(0)
                if minm[0] == nums[i]:
                    minm.pop(0)
                i += 1
        return j - i + 1
