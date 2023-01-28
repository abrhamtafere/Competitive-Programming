class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = len(height)-1
        j = 0
        area = 0
        s = []
        while i > j:   
            w = i - j
            res = w * min(height[i],height[j])
            area = max(area, res)
        
            if height[i]<height[j]:
                i-=1
            else:
                j+=1
        return area
