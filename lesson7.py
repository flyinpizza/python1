# #1
#
# class Matrix:
#     def __init__(self, matrix):
#         self.matrix = matrix
#     def __str__(self):
#         return '\n'.join('\t'.join([str(item) for item in line]) for line in self.matrix)
#     def __add__(self, other):
#         add_matrix = []
#         for i in range(len(self.matrix)):
#             add_matrix_item = []
#             for j in range(len(self.matrix[i])):
#                 new_item = self.matrix[i][j]+other.matrix[i][j]
#                 add_matrix_item.append(new_item)
#             add_matrix.append(add_matrix_item)
#         return add_matrix
#
# neo = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 0]])
# triniti = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
# morpheus = neo + triniti
# print(morpheus)

# #2
#
# from abc import ABC, abstractmethod
# class Clothes(ABC):
#     @abstractmethod
#     def fabric_use(self):
#         pass
#
# class Costume(Clothes):
#     def __init__(self, height):
#         self.height = height
#     def fabric_use(self):
#         fabric_use = 2 * self.height+0.3
#         return fabric_use
#
# class Coat(Clothes):
#     def __init__(self, size):
#         self.size = size
#     def fabric_use(self):
#         fabric_use = self.size / 6.5 + 0.5
#         return  fabric_use
#
# costume1 = Costume(1.8)
# coat1 = Coat(46)
# print(costume1.fabric_use())
# print(coat1.fabric_use())

# #3
#
# class Cell:
#     def __init__(self, number):
#         self.number = number
#     def __add__(self, other):
#         return self.number + other.number
#     def __sub__(self, other):
#         if self.number >= other.number:
#             return self.number - other.number
#         else:
#             return f"The number of result can't be less than zero"
#     def __mul__(self, other):
#         return self.number * other.number
#     def __floordiv__(self, other):
#         try:
#             return self.number // other.number
#         except ZeroDivisionError:
#             return "You're not allowed to divide by zero"
#     def make_order(self, symbol, sym_per_line):
#         line = ""
#         for i in range(1, self.number+1):
#             if i % sym_per_line == 0 and i >= sym_per_line:
#                 line += symbol + "\n"
#             else:
#                 line += symbol
#         return line
#
# green_cell = Cell(20)
# red_cell = Cell(3)
# add_cells = green_cell + red_cell
# sub_cells = green_cell - red_cell
# sub_cells_test = red_cell - green_cell
# mult_cells = green_cell * red_cell
# div_cells = green_cell // red_cell
# print(div_cells)
# print(mult_cells)
# print(sub_cells)
# print(sub_cells_test)
# print(add_cells)
# print(green_cell.make_order("@", 4))