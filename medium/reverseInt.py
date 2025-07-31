class Solution:
    def reverse(self, x):
        
        if x == 0:
            return 0
        
        sign = 1 if x > 0 else -1
        x = abs(x)
        
        # to reverse digits
        reversed_num = 0
        while x > 0:
            digit = x % 10
            x //= 10
            
            # check for overflow
            if reversed_num > 2 **31 //10:
                return 0
            if reversed_num == 2 ** 31 // 10 and digit > (7 if sign == 1 else 8):
                return 0
            
            reversed_num = reversed_num * 10 + digit
        
            
        return sign * reversed_num
        
        
# # test harness for verification
# solution = Solution()
# test = 2574
# result = solution.reverse(test)
# print(result)

# Test harness for verification
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        123,          # Expected: 321
        -123,         # Expected: -321
        120,          # Expected: 21
        0,            # Expected: 0
        1534236469,   # Expected: 0 (overflow)
        -2147483648,  # Expected: 0 (overflow)
        5             # Expected: 5
    ]
    
    for test in test_cases:
        result = solution.reverse(test)
        print(f"Input: {test} -> Output: {result}")
    