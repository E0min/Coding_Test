def solution(nums):
    numberOfChoice = len(nums)//2
    snums = len(set(nums))
    return snums if numberOfChoice > snums else numberOfChoice
    