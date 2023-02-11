class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        freq_sort = sorted(freq.items(),key = lambda x:x[1] , reverse = True)
        top_k = [i[0] for i in freq_sort[:k]]
        return top_k
