# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 12:11:33 2019

@author: conory
"""

class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        '''
        if n==0:
            return 1;
        else:
            sum=1
            while (n>=1):
                sum=n*sum
                n=n-1
            g=0;
            num=0;
            while 1:
                g=sum%10
                if g==0:
                    num+=1
                    sum=int(sum//10)
                else:
                    break;
        return num;
        '''
        if n==0:
            return 1;
        else :
            num=0;
            gg=n//5
            while gg!=0:
                num+=1
                gg=gg//5
            sum=0
            while num!=0:
                sum=sum+n//(5**num)
                num-=1
            return sum;
a=Solution()
print(a.trailingZeros(105))