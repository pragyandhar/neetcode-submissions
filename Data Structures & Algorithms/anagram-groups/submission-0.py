class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for i in range(0, len(strs)):
            sorted_strs = ''.join(sorted(strs[i]))
            
            if sorted_strs in anagram:
                anagram[sorted_strs].append(strs[i])
            else:
                anagram[sorted_strs] = [strs[i]]

        return list(anagram.values())