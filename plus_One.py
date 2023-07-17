class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a=len(digits)
        carry=1
        for i in range(a-1,-1,-1):
            total=digits[i]+carry
            digits[i]=total%10
            carry=total/10
        if carry >0:
            digits.insert(0,carry)
        return digits

