#!/usr/bin/env python

import random

r = random.randint(1,100)

nums = range(10)

print nums
# what we are looking for 
key = 4
#initialize the whole list is to be searched
lo = 0
hi = len(nums)
#main loop: keep going while there are options available
while lo < hi:
    #find the middle item
    mididx = (lo + hi) / 2
    mid = nums[mididx]
    
    print "mididx = ", mididx
    #compare the middle item to the list
    if (mid == key):
        print "hooray found it", (mid)
    elif (mid > key):
        lo = mididx + 1
    else:
        hi = mididx 
 