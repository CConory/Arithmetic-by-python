# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b 
    """
    def aplusb_1(self, a, b):
        # write your code here
        
        return (a^b)+((a&b)<<1);
    def aplusb_2(self, a, b):
        # write your code here
        
        return a+b;
gg=Solution()
print(gg.aplusb_1(2**64,2**64))