**Problem**: Given an integer array, output all the unique sum

So for the input

    ``` sum([2,4,6],10)

    would return
     4,6

    ```

** Approach 1 **: Take two index, one at the front and one at the back. After that move two index left or right till they become equal to the desired sum
** Approach 2 ** : Brute Force Approach(It take O(n^2) to solve the problem and hence not a good approach). Loop through the array and create all possible pairing.