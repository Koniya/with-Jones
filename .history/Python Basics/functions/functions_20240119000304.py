'''
a = 4
b = 5
sum_result = a+b
print(sum_result)


#function to calculate perimeter and area of a square

def square_area(side):
    total_square_area = side*side
    return total_square_area

side = 10
result = square_area(side)
print(f"The area of the square with the side measurement of {side}cm is {result}")

def square_perimeter(side):
    total_square_perimeter = side*4
    return total_square_perimeter

side = 10
result = square_perimeter(side)
print(f"The perimeter of the square with the side measurement of {side}cm is {result}")

print(f"The area of the square with the side measurement of {side}cm is {result}")
'''
def square_measurements(side):
    side = 8    
    area_sq = side*side
    peri_sq = side*4
    return area_sq, peri_sq

print (f"The area and perimeter of a square area {square_measurements()}")




