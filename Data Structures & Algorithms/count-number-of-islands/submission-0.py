class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        island_set=set()

        for i, row in enumerate(grid):
            for j , num in enumerate(row):
                if num == "1" and (i,j) not in island_set:
                    count +=1
                    stack = [(i,j)]
                    island_set.add((i,j))

                    while stack:
                        r,c = stack.pop()
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nr, nc = r + dr, c + dc
                            if(nr in range(len(grid)) 
                            and nc in range(len(row)) 
                            and grid[nr][nc] == "1" 
                            and (nr,nc) not in island_set):
                                island_set.add((nr,nc))
                                stack.append((nr,nc))
                    



        return count
        