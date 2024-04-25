class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Output the hypothetical rank of the target
        if it would have been inserted in the inputted array
        """
        if nums[0] >= target:
            return 0
        if nums[len(nums) - 1] == target:
            return len(nums) - 1
        if nums[len(nums) - 1] < target:
            return len(nums)
        begin = 0
        end = len(nums) - 1
        while end - begin > 1:
            median = (end + begin) // 2
            if target == nums[median]:
                return median
            if target < nums[median]:
                 end = median
            else:
                begin = median
        if nums[begin] < target:
            return end
        if nums[begin] == target:
            return begin
            
        
def SkMergeTwo(v1,v2):
    res = []
    while len(v1) != 0 or len(v2) != 0:
        if v1[0] < v2[0]:
            res.append[v1[0]]
            v1.pop(0)
        else:
            res.append[v2[0]] 
            v2.pop(0)
    return res


def SkTri(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Output the array inputted sorted via a merge sort
        """
        if len(nums) == 1:
            return nums
        