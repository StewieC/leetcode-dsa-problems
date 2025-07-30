def romanToInt(s: str) -> int:
    # Dictionary mapping Roman numerals to values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    for i in range(len(s)):
        # If current symbol is less than next, subtract current value
        if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
            result -= roman_values[s[i]]
        # Otherwise, add current value
        else:
            result += roman_values[s[i]]
    
    return result

"""
Explanation: 
we initialze result = 0 and a  roman values dictionary.

lets use 'MCMXCIV as an example to work with to show iteration

we then iterate through the string s. the iteration is done by:
    index 0: M(1000). Next is C(100). Since 1000 > 100, add 1000. result = 1000
    
    index 1: C(100). Next is M(1000). Since 100 < 1000, subtract 100(for CM = 900). result = 900
    
    index 2: M(1000). Next is X(10). since 1000 > 10, add 1000. result = 1900
    
    index 3: X(10). next is C(100). since 10 < 100, subtract 10(for XC = 90). result = 1810
    
    index 4: C(100). next is I(1). since 100 > 1, add 100. result = 1910
    
    index 5: I(1). next is V(5). since 1 < 5, subtract 1(for IV = 4). result = 1909
    
    index 6: V(5). no next, so add 5. result = 1994
    
    result = 1994
"""

# Example usage:
if __name__ == "__main__":
    print(romanToInt("MCMXCIV"))  # Output: 1994
    print(romanToInt("III"))       # Output: 3
    print(romanToInt("IV"))        # Output: 4
    print(romanToInt("IX"))        # Output: 9
    print(romanToInt("MCXIIV"))     
    print(romanToInt("XLII"))      # Output: 42