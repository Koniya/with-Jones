# a = 4
# b = 5
# sum_result = a+b
# print(sum_result)


# #function to calculate perimeter and area of a square

# def square_area(side):
#     total_square_area = side*side
#     return total_square_area

# side = 10
# result = square_area(side)
# print(f"The area of the square with the side measurement of {side}cm is {result}")

# def square_perimeter(side):
#     total_square_perimeter = side*4
#     return total_square_perimeter

# side = 10
# result = square_perimeter(side)
# print(f"The perimeter of the square with the side measurement of {side}cm is {result}")

# print(f"The area of the square with the side measurement of {side}cm is {result}")






# def square_measurements(side):      
#     area_sq = side*side
#     peri_sq = side*4
#     print(f"The area of a square with a side of {side} is {area_sq}, while its perimeter is {peri_sq}.")

# print (square_measurements(8))

def square_measurements(side):# header: has the name of the function and the parameters      
     #side = 8
     area_sq = side** # create a variable for the area of a square
     peri_sq = side*4 # create a variable for the p
     return area_sq, peri_sq

side = 8
area_sq, peri_sq = square_measurements(side)# calling the function with the argument
print (f"The area of a square with side {side} is {area_sq}, while its perimeter is {peri_sq}.")


#name = "Connie", "Lorenzo"
#print (type(name))



