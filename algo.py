class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] > target:
            return 0
        if nums[len(nums) - 1] < target:
            return len(nums)
        begin = 0
        end = len(nums) - 1
        while end - begin > 1:
            median = (end - begin + 1) // 2
            if target == nums[median]:
                return median
            if target < nums[median]:
                end = median
            else:
                begin = median
        return begin
            
        
def SKcompare(self, target,begin, end):
    """
    Just to know whether I'm above, below or equal to the median
    """  
    median = (end-begin)/2
    if target == median:
        return -94, median