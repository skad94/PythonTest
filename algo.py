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
                if len(nums) - (k + 1) == i:
                    return len(nums) -(k + 1), nums
                else:
                    nums[i] = nums[-(k + 1)]
                    nums[-(k + 1)] = 94
                    k=k+1
        return len(nums) - (k + 1), nums
            
        
def SkMergeTwo(v1,v2):
    res = []
    while len(v1) != 0 and len(v2) != 0:
        if v1[0] < v2[0]:
            res.append[v1[0]]
            v1.pop(0)
        else:
            res.append[v2[0]] 
            v2.pop(0)
    res += v1 + v2 # one array is empty but then we don't have to add a if
    return res


def SkTri(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Output the array inputted sorted via a merge sort
        """
        if len(nums) <= 1:
            return nums
        else:
            return SkMergeTwo(SkTri(nums[0:len(nums)//2]),SkTri(nums[len(nums)//2:len(nums)-1]))