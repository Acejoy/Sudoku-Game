import copy

import puzzles


class SudokuGame:

    def __init__(self, puzzle):
        #pass
        self.puzzle = puzzle
        #self.puzzle = puzzles.test.get(3)

    def print_puzzle(self,grid):
        for row in grid:
            print('\t\t', end='')
            for val in row:
                print(val, end=' ')                
            print()
    
    def possible(self, grid, row, col, val):
        # valid in the sub-grid
        sub_grid_index = (row//3, col//3)

        for i in range(3):
            for j in range(3):
                if grid[sub_grid_index[0]*3 +i][sub_grid_index[1]*3 +j] == val :
                    #print('1!')
                    return False

        # valid in the row
        for i in range(9):
            if grid[row][i] == val:
                #print('2@')
                return False

        # valid in the col
        for i in range(9):
            if grid[i][col] == val:
                #print('3#')
                return False
    
        return True

    def find_next_empty_cell(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return i,j

        return None

    def get_possible_values(self, grid, row, col):
        possible_values = []
        
        for val in range(1,10):
            if self.possible(grid, row, col, val):
                possible_values.append(val)

        return possible_values

    def solve(self, grid):
        cur_cell = self.find_next_empty_cell(grid)
        #print(f'current cell is: {cur_cell}', end='')
        if cur_cell is None:
            return grid
        
        possible_values = self.get_possible_values(grid, cur_cell[0], cur_cell[1])
        #print('possible values are:', possible_values)
        if len(possible_values) == 0:
            return None
        else:
            for val in possible_values:
                # print(f'current cell is: {cur_cell}', end='')
                # print('possible values are:', possible_values, end='')
                # print('val used :', val)
                new_grid = copy.deepcopy(grid)
                new_grid[cur_cell[0]][cur_cell[1]] = val
                res = self.solve(new_grid)
                if res:
                    return res
            
            


if __name__ == "__main__":
    
    mode = input('Enter the mode{easy, medium, hard, test}:').lower()
    #mode = 'easy'
    if mode not in ['easy', 'medium', 'hard', 'test']:
        print('Enter correct mode')
    else:
        game = SudokuGame(puzzles.puzzles.get(mode))
        game.print_puzzle(game.puzzle)
        #print(game.possible(0,3))
        res = game.solve(game.puzzle)
        if not res:
            print('Puzzle is not solvable!')
        else:
            print()
            game.print_puzzle(res)
