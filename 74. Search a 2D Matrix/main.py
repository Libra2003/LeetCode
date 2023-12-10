class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        u, d = 0, len(matrix) - 1
        r_m = 0

        while u <= d:
            r_m = u + ((d - u) // 2)
            if target < matrix[r_m][0]:
                d = r_m - 1
            elif target > matrix[r_m][-1]:
                u = r_m + 1
            else:
                break
        if not (u<=d):
            return False

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if target < matrix[r_m][mid]:
                r = mid - 1
            elif target > matrix[r_m][mid]:
                l = mid + 1
            else:
                return True
        return False

# Example usage:
sol = Solution()
res = sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
print(res)  # Output: False
