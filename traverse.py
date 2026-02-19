class Solution:
    def spirallyTraverse(self, mat):
        res = []
        top, bottom = 0, len(mat) - 1
        left, right = 0, len(mat[0]) - 1
        while top <= bottom and left <= right:
            res += mat[top][left:right+1]
            top += 1
            for i in range(top, bottom+1):
                res.append(mat[i][right])
            right -= 1
            if top <= bottom:
                res += mat[bottom][left:right+1][::-1]
                bottom -= 1
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(mat[i][left])
                left += 1
        return res
