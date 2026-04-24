class Solution:
    def countBalanced(self, arr):
        vowels = set('aeiou')
        
        values = []
        for s in arr:
            v = 0
            c = 0
            for ch in s:
                if ch in vowels:
                    v += 1
                else:
                    c += 1
            values.append(v - c)
        
        prefix_sum = 0
        count = 0
        freq = {0: 1}
        
        for val in values:
            prefix_sum += val
            
            if prefix_sum in freq:
                count += freq[prefix_sum]
            
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
        
        return count
