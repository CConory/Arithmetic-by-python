# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 16:20:02 2019

@author: conory
"""

class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        nums.sort(reverse=True)
        return nums[n-1]
a=Solution()
#print(a.kthLargestElement(3,[9,3,2,4,8]))
def f(a):
    return a**2
a=[1,0,-1]
a.sort(key=f)
print(a)
