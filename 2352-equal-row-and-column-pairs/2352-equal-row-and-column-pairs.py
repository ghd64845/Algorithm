class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transposed_grid = []
        # transposed_grid = [list(col) for col in zip(*grid)]
        
        for col in zip(*grid):
            transposed_grid.append(list(col))
            
        equal_pair_cnt = 0 
        
        for row in grid:
            for transposed_row in transposed_grid:
                if row == transposed_row:
                    equal_pair_cnt += 1
    
        return equal_pair_cnt