class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # List of (value, symbol) pairs in descending order
        value_symbols = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        result = ""
        for value, symbol in value_symbols:
            # While num is greater than or equal to the current value
            while num >= value:
                result += symbol  # Append the symbol
                num -= value      # Subtract the value
        
        return result
    
solution = Solution()
test = 1994
result = solution.intToRoman(test)
print(result)  # Expected output: "MCMXCIV"