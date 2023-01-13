class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        l,r = 0,len(matrix)-1
        while l<r:
            for i in range(r-l):
                
                up,bot = l,r
                
                temp = matrix[up][l+i]
                
                matrix[up][l+i] = matrix[bot-i][l]

                matrix[bot-i][l] = matrix[bot][r-i]
                
                matrix[bot][r-i] = matrix[up+i][r]
                
                matrix[up+i][r] = temp
            l+=1
            r-=1