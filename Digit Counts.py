# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 14:18:23 2019

@author: conory
"""

class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts_1(self, k, n):
        # write your code here
        num=0;
        while (n>=0):
            a=n;
            while(a!=0):
                b=a%10;
                if b==k:
                    num+=1;
                a=(a-b)//10
            n=n-1;
        if k==0:
            num+=1;
        return num;
    def digitCounts_2(self, k, n):
        num=0;
        while(n>=0):
            a=str(n)
            for i in a:
                if i==str(k):
                    num+=1;
            n-=1;
        return num;
a=Solution()
print(a.digitCounts_2(1,11))

            
