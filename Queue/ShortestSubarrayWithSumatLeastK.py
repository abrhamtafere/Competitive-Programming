class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n= len(nums)
        cums = [0]*(n+1)
        for i in range(1,n+1):
            cums[i] = cums[i-1]+nums[i-1]
        res= float("inf")
        dq = deque()
        for i in range(n+1):
            while dq and cums[i]- cums[dq[0]] >=k:
                res = min(res,i-dq.popleft())
            while dq and cums[i] <= cums[dq[-1]]:
                dq.pop()
            dq.append(i)
        return -1 if res == float("inf") else res  
