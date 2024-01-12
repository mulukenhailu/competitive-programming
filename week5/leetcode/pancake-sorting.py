class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        def flip(arr, k: int) -> None:
            left = 0
            while left < k:
                arr[left], arr[k] = arr[k], arr[left]
                k -= 1
                left += 1

        def max_index(arr, k: int) -> int:
            index = 0
            for i in range(k):
                if arr[i] > arr[index]:
                    index = i
            return index

        def pancake_sort(arr) -> None:
            n = len(arr)
            while n > 1:
                maxdex = arr.index(n)
                if maxdex != n - 1:
                    if maxdex != 0:
                        ans.append(maxdex+1)
                        flip(arr, maxdex)
                    ans.append(n)
                    flip(arr, n - 1)
                n -= 1

        
        pancake_sort(arr)
        print(arr)

        return ans





        