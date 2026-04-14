class Solution:
    def search(self, currentMatrix: List[int], target: int) -> bool:
        l, r = 0, len(currentMatrix) - 1
        while l <= r:
            m = (l+r) // 2
            if currentMatrix[m] == target:
                return True
            elif currentMatrix[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        matrixL, matrixR = 0, len(matrix) - 1

        while matrixL <= matrixR:

            matrixMiddle = (matrixR + matrixL) // 2 

            if matrix[matrixMiddle][-1] < target:
                matrixL = matrixMiddle + 1

            elif matrix[matrixMiddle][0] > target:
                matrixR = matrixMiddle - 1

            else:
                return self.search(matrix[matrixMiddle], target)

        return False
