class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i+1
            k = len(nums)-1

            while j < k:
                SUM = nums[i] + nums[j] + nums[k]
                if SUM == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif SUM < 0:
                    j += 1
                elif SUM > 0:
                    k -= 1
                else:
                    break
        
        return ans
                
                
