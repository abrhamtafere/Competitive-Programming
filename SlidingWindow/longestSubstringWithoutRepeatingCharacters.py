class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        dic = {}
        max_str_len = 0
        for i in range(len(s)):
            if s[i] in dic and start <= dic[s[i]]:
               start = dic[s[i]] + 1
            else:
                max_str_len = max(max_str_len, i - start + 1)
            dic[s[i]] = i
        return max_str_len
