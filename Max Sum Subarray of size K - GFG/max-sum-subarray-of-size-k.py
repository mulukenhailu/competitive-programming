#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        res = 0
        for i in range(K):
            res += Arr[i]
        curr_sum = res
        for i in range(K, N):
            curr_sum += Arr[i] - Arr[i - K]

            res = max(res, curr_sum)

        return res








#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends