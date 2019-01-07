# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 15:07:12 2019

@author: conory
"""

class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber_1(self, n):
        # write your code here
        b=[1,1,1]
        a=[0,1]
        i=1
        while i<n:

            Min=min(a[b[0]]*2,a[b[1]]*3,a[b[2]]*5)
            
            if(a[b[0]]*2==Min):
                b[0]+=1;
            elif(a[b[1]]*3==Min):
                b[1]+=1;
            else:
                b[2]+=1;
            if(Min>a[i]):
               i+=1          
               a.append(Min)
        return a[-1];
    def nthUglyNumber_2(self, n):
        # write your code here
        b=[1,1,1]
        a=[0,1]
        i=1
        while i<n:

            Min=min(a[b[0]]*2,a[b[1]]*3,a[b[2]]*5)
            
            if(a[b[0]]*2==Min):
                b[0]+=1;
            if(a[b[1]]*3==Min):
                b[1]+=1;
            if(a[b[2]]*5==Min):
                b[2]+=1;
      
            a.append(Min)
            i+=1
        return a[-1];
            
                
                

a=Solution()
print(a.nthUglyNumber_2(7))