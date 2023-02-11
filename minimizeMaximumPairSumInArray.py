class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair = []
        while not nums == []:
                max_pair.append(nums.pop(0) + nums.pop(-1))
        return max(max_pair)
