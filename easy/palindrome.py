class Solution:
    def isPalindrome(self, x):
        # handle negative numbers
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # handle single digits
        if x < 10:
            return True
        
        reversed_num = 0
        while x > reversed_num:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x = x // 10
            
        return x == reversed_num or x == reversed_num // 10
        