from random import randint
import numpy as np


class sort:
    def partition(self, left, right, nums):
        pivot, ptr = nums[right], left
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        nums[ptr], nums[right] = nums[right], nums[ptr]
        return ptr

    def quicksort(self, left, right, nums):
        if len(nums) == 1:
            return nums
        if left < right:
            pi = self.partition(left, right, nums)
            self.quicksort(left, pi - 1, nums)
            self.quicksort(pi + 1, right, nums)
        return nums


obj = sort()
example = np.random.randint(-10, 20, size=20)
print("Unsorted: " + str(example))
print("Sorted: " + str(obj.quicksort(0, len(example) - 1, example)))

