"""Q2. Shuffle the Array

Objective: Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
Example 2:

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
Example 3:

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
 
Constraints:

1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        length_of_list=len(nums)
        half_point = length_of_list/2
        half_point = int(half_point)
        first_half_of_list = nums[0:half_point]
        second_half_of_list = nums[half_point:]
        new_list = []
        for i in range(len(first_half_of_list)):
            new_list.append(first_half_of_list[i])
            new_list.append(second_half_of_list[i])
        return new_list
