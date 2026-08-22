class Solution:
    def maxArea(self, h: List[int]) -> int:
        i = 0
        j = len(h)-1

        area = 0
        while (i < j) :
            breadth = j - i
            length = min(h[i], h[j])
            area = max(area, length * breadth)
            if (h[i] < h[j]) :
                i += 1
            else:
                j -= 1
        return area