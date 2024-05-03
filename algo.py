class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
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
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                while nums[-(k + 1)] == val and len(nums) - (k + 1) > i:
                    k=k+1
                if len(nums) - (k + 1) <= i:
                    rr = len(nums) -(k)
                    return rr, nums
                else:
                    nums[i] = nums[-(k + 1)]
                    nums[-(k + 1)] = 94
                    k=k+1
        rr = len(nums) -(k + 1)
        return rr, nums
            
        
def SKcompare(self, target,begin, end):
    """
    Just to know whether I'm above, below or equal to the median
    """  
    median = (end-begin)/2
    if target == median:
        return -94, median