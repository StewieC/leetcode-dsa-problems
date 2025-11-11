class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]a
        """
        for i in range(len(digits) - 1, -1, -1):
            digits[i]+=1
            if digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    # If carry reaches the front, add new digit
                    digits.insert(0, 1)
            else:
                # No carry, we’re done
                break
        return digits

        