class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][len(matrix[mid])-1] < target:
                l = mid + 1
            else:
                l, r = 0, len(matrix[mid]) - 1
                while l <= r:
                    mid_mid = (l + r) // 2
                    if matrix[mid][mid_mid] > target:
                        r = mid_mid - 1
                    elif matrix[mid][mid_mid] < target:
                        l = mid_mid + 1
                    else:
                        return True


        return False
