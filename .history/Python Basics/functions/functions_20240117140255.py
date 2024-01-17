'''
a = 4
b = 5
sum_result = a+b
print(sum_result)
'''

#function to calculate perimeter and area of a square

def square_area(side):
    total_square_area = side*side
    return total_square_area

side = 6
result = square_area(side)
print(f"The area of the square with the side measurement of {side}cm is {result})

def square_perimeter(side):
    total_square_perimeter = side*4
    return total_square_perimeter

side = 8
result = square_perimeter(side)
print(f"The perimeter of the square with the side measurement of {side}cm is {result})