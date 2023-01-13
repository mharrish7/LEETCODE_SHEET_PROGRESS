class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:


        visited = set()

        i,j = 0,0
        di,dj = 0,1
        n = 0
        R = []
        while n < len(matrix)*len(matrix[0]):
            n+=1 
            R.append(matrix[i][j])
            visited.add((i,j))
            if i+di == len(matrix) or j+dj == len(matrix[0]) or i+di < 0 or j+dj < 0 or (i+di,j+dj) in visited:
                di,dj = dj,-di
            
            i,j = i+di,j+dj 
        
        return R
                