   return swaps
        class Solution:
    def minSwaps(self, s1, s2):
        n = len(s1)
        
        count01 = 0  # s1[i] = 0, s2[i] = 1
        count10 = 0  # s1[i] = 1, s2[i] = 0
        
        for i in range(n):
            if s1[i] != s2[i]:
                if s1[i] == '0':
                    count01 += 1
                else:
                    count10 += 1
        
        if (count01 + count10) % 2 != 0:
            return -1
        
        swaps = (count01 // 2) + (count10 // 2)
        
        if count01 % 2 == 1:
            swaps += 2
