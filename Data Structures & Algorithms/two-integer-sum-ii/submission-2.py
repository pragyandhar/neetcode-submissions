class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1

        SUM = 0
        ans = list()

        while (i < j):
            SUM = numbers[i] + numbers[j]
            if SUM == target:
                ans.append(i+1) 
                ans.append(j+1)
                break
            elif SUM > target:
                SUM -= numbers[j]
                j -= 1
            else:
                SUM -= numbers[i]
                i += 1
        
        return ans
