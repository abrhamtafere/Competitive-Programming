class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for x in range(len(nums)):
            
            for j in range(len(nums)):
                if(j!=x):
                    if((nums[x]+nums[j])==target):
                        if(x not in ans):
                            ans.append(x)
                        if(j not in ans):
                            ans.append(j)
        return ans
