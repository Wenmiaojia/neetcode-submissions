class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range (len(strs[0])):
            ch = strs[0][i]
        
            for string in strs:
                if i == len(string) or string[i] != ch:
                    return strs[0][:i]

        return strs[0]

            