class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        for v in nums2:
            while(stack and stack[-1] < v):
                k =stack.pop()
                dic[k]=v
            stack.append(v)
        return [dic.get(v,-1) for v in nums1]
