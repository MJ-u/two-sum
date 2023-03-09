from typing import List

class Go:
    def __init__(self, nums: List[int], target: int):
        self.nums = nums
        self.target = target
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = 0 #찾을 숫자
        index = 0
        found = False
        sizeofnums = len(self.nums)
        while ((not found) and (index < sizeofnums)) :
            num1 = index
            temp = self.target - self.nums[index]
            for j in range (index+1, sizeofnums) :
                if (self.nums[j] == temp) :
                    found = True
                    num2 = j
            index += 1

        # YOUR ANSWER
        return [num1, num2]