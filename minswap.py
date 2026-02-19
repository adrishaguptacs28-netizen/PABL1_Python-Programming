class Solution:
    def minSwap(self, arr, k):
        n = len(arr)
        count = sum(1 for num in arr if num <= k)
        bad = sum(1 for i in range(count) if arr[i] > k)
        ans = bad
        for i in range(n - count):
            if arr[i] > k:
                bad -= 1
            if arr[i + count] > k:
                bad += 1
            ans = min(ans, bad)
        
        return ans
