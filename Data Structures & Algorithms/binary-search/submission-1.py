class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        ans = -1

        while (low <= high) :
            mid = low + (high - low) // 2

            if nums[mid] == target:
                ans = mid
                break
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return ans