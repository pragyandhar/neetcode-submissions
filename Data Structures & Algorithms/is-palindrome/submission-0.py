class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''.join(char for char in s if char.isalnum()).lower()
        i = 0
        j = len(st) - 1

        flag = True

        while (i < j) :
            if st[i] != st[j]:
                flag = False
                break
            i += 1
            j -= 1
        
        return flag