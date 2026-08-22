class Solution:
    def trap(self, h: List[int]) -> int:
        i = 0 
        j = len(h) - 1

        left_max = 0
        right_max = 0
        ans = 0

        while (i < j) :
            if h[i] <= h[j]:
                if h[i] >= left_max:
                    left_max = h[i]
                else:
                    ans += left_max - h[i]
                i += 1
            else:
                if h[j] >= right_max:
                    right_max = h[j]
                else:
                    ans += right_max - h[j]
                j -= 1
                
        return ans
            
