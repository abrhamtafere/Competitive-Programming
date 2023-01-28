class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        simstack = []
        n = len(popped)
        i = 0
        for j in pushed:
            simstack.append(j)
            while simstack and i<n and simstack[-1]==popped[i]:
                i+=1
                simstack.pop()
        return simstack==[]
