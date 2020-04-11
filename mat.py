class matrices(object):
    
    def __init__(self, rows, cols):
        self.rows = int(rows)
        self.cols = int(cols)
        self.matrix = []
        i,j =0,0
        self.matrix = [[int(input(f'Enter element in index ({i}, {j})')) for i in range(self.rows)] for j in range(self.cols)]

    def size(self):
        return f"Number of rows = {self.rows}\n Number of columns = {self.columns} "

    def get_cell(self, row, col):
        return self.matrix[row][col]

    def set_cell(self, row, col, value):
        self.matrix[row][col] = value 

    def to_str(self):
        return str(self.matrix).strip('[]')

    def mult(self, val):
        new = []
        i,j =0,0
        new = [[val * self.matrix[i][j] for i in range(self.rows)] for j in range(self.cols)]
        return new

a = matrices(2 ,1)
a.to_str()
a.mult(2)