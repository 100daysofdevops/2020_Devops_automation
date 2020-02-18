**Problem**: Given an array of integers find the largest continious sum

**Solution**: Before we dive into the solution, some points to consider
1: If array consist of all postive integers then the largest continious sum is the sum of all numbers
2: Solution become challenging when we have negative integer in the array, as in that case we need to begin checking sequences

The approach we are going to follow is to start summing up the numbers and store the sum in a current sum variable. After adding each element , we check whether the current sum is larger than maximum sum encountered so far. If it's we will update the maximum sum. As long as the current sum is positive , we will keep on adding the number. When the current sum becomes negative we start with the new current sum. Remember negatvice sum will only decrease the sum of a future sequence.


**NOTE:** 
1: It's an array of integers it can be positive or negatives.
2: We are not going to reset the current sum to zero as array can contain all negative integers.

**Reference:** https://en.wikipedia.org/wiki/Maximum_subarray_problem
