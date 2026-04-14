'''

choices: All choices, all subsets of given nums 

constraints: cant input same subset twice

Base Case: if subset == size of initial nums 

Backtracking step: 

'''


class Solution:
    def subsets(self, nums: List[int]) -> List[int]:
        res = []

        def backtrack(index, path):
            #base case
            if index == len(nums):
                res.append(path[:])
                return
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            backtrack(index + 1, path)
        backtrack(0, [])
        return res
