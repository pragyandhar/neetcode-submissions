from math import ceil
class Solution:
    def is_possible(self, arr: List[int], speed: int, h: int) -> bool:
        hour = 0

        for banana in arr:
            hour += ceil(banana / speed)
        
        return hour <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high :
            mid = low + (high - low) // 2

            if self.is_possible(piles, mid, h):
                high = mid
            else:
                low = mid + 1
        
        return low