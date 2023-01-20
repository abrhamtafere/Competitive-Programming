#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        min_index = i
        for j in range(i, len(arr)-1):
            if arr[j+1] < arr[min_index]:
                min_index = j+1
        return min_index
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min_index = self.select(arr, i)
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
