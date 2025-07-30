"""
we need to find the longest common prefix string among an array of strings.
if no common prefix exists, return an empty string.

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Handle edge case: if array is empty or has empty string
        if not strs or "" in strs:
            return ""
        
        # If only one string, return it
        if len(strs) == 1:
            return strs[0]
        
        # Use first string as reference
        for i in range(len(strs[0])):
            char = strs[0][i]  # Current character in first string
            # Check if char matches in same position for all other strings
            for other in strs[1:]:
                # If index exceeds length or characters don't match, return prefix up to i
                if i >= len(other) or other[i] != char:
                    return strs[0][:i]
        
        # If loop completes, first string is the prefix (or a prefix of it)
        return strs[0]

# Test harness for verification
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ["flower", "flow", "flight"],  # Expected: "fl"
        ["dog", "racecar", "car"],    # Expected: ""
        ["interspecies", "interstellar", "interstate"],  # Expected: "inter"
        ["prefix", "prefixes", "pre"],  # Expected: "pre"
        ["a"],                         # Expected: "a"
        ["", "test"],                  # Expected: ""
        ["abc", "abcd", "abce"]       # Expected: "abc"
    ]
    
    for test in test_cases:
        result = solution.longestCommonPrefix(test)
        print(f"Input: {test} -> Output: '{result}'")