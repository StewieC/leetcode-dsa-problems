class Solution:
    def longestCommonPrefix(self, strs: list[str]):
        
        # handling an empty array
        if not strs:
            return ""
        
        # find the shortest string length
        min_length = min(len(s) for s in strs)
        
        # compare characters across all strings
        for i in range(min_length):
            char = strs[0][i] #first string as reference
            for string in strs[1:]:
                if string[i] != char:
                    return strs[0][:i] # return prefix up to this point
                
        return strs[0][:min_length]