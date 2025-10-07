class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge cases
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        
        # Slide window and compare
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        
        return -1