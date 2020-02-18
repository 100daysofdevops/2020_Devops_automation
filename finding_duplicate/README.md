**Problem**: Finding Duplicate Values in a list in Python

Solution: There is multiple ways to solve this problem

1. Brute Force --> O(n^2) complexity -> Goes through each element of the array before finding out the duplicate value
2. Sorting --> 0(nlogn) Iterate through the array and check if the next element is same
3. Hash Table --> 0(1) we can perform lookup in constant time(tradeoff it takes lot of space in memory)