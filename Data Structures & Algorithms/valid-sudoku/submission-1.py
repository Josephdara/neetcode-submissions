class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sudo_dict = defaultdict(set)
        col_sudo_dict = defaultdict(set)
        sqr_sudo_dict = defaultdict(set)
        for i , sub in enumerate(board):
            for j, num in enumerate(sub):
                if num.isdigit() == False:
                    continue
                else:
                    key = (i//3,j//3)
                    if num in row_sudo_dict[i] or num in col_sudo_dict[j] or num in sqr_sudo_dict[key]:
                        return False
                row_sudo_dict[i].add(num)
                col_sudo_dict[j].add(num)
                sqr_sudo_dict[key].add(num)
   
    
        return True 
        