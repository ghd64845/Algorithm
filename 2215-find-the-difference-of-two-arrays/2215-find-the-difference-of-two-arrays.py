import numpy as np

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr1 = np.array(nums1)
        arr2 = np.array(nums2)
        
        return [np.setdiff1d(arr1, arr2), np.setdiff1d(arr2, arr1)]