class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        if(total & 1 == 1): # odd
            return self.findK(nums1, nums2, 0, 0, int(total/2 + 1))
        else:
            return float(self.findK(nums1, nums2, 0, 0, int(total/2)) + self.findK(nums1, nums2, 0, 0, int(total/2 + 1)))/2

    def findK(self, nums1, nums2, pA, pB, k):
        if(pA>=len(nums1)):
            if(pB>=len(nums2)):
                return -1
            elif(k==1):
                return nums2[pB]
            else:
                return self.findK(nums1, nums2, pA, pB+1, k-1)
        elif(pB>=len(nums2)):
            if(k==1):
                return nums1[pA]
            else:
                return self.findK(nums1, nums2, pA+1, pB, k-1)
        else:
            if(k==1):
                return min(nums1[pA], nums2[pB])
            elif(nums1[pA]<nums2[pB]):
                return self.findK(nums1, nums2, pA+1, pB, k-1)
            else:
                return self.findK(nums1, nums2, pA, pB+1, k-1)

sol = Solution()
print(sol.findMedianSortedArrays([1,2],[3,4]))
