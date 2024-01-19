# # a = 4
# # b = 5
# # sum_result = a+b
# # print(sum_result)


# # #function to calculate perimeter and area of a square

# # def square_area(side):
# #     total_square_area = side*side
# #     return total_square_area

# # side = 10
# # result = square_area(side)
# # print(f"The area of the square with the side measurement of {side}cm is {result}")

# # def square_perimeter(side):
# #     total_square_perimeter = side*4
# #     return total_square_perimeter

# # side = 10
# # result = square_perimeter(side)
# # print(f"The perimeter of the square with the side measurement of {side}cm is {result}")

# # print(f"The area of the square with the side measurement of {side}cm is {result}")






# def square_measurements(side):      
#     area_sq = side*side
#     peri_sq = side*4
#     print(f"The area of a square with a side of {side} is {area_sq}, while its perimeter is {peri_sq}.")

# print (square_measurements(8))

# #void function is also a fruitless function because it does not return anything that can be used in another part of the program

# def square_measurements(side):# header: has the name of the function and the parameters      
#      #side = 8
#      area_sq = side**2 # create a variable for the area of a square
#      peri_sq = side*4 # create a variable for the perimeter of a square
#      return area_sq, peri_sq # return the tuple: area and perimeter

# side = 8
# area_sq, peri_sq = square_measurements(side)# calling the function with the argument; uncoupling the tuple into two variables
# print (f"The area of a square with side {side} is {area_sq}, while its perimeter is {peri_sq}.")# variables are being printed and not the y
# #a fruthful function because it returns value

# #name = "Connie", "Lorenzo"
# #print (type(name))

def print_lyrics():
     print("Amazing grace")
     print("How sweet the sound")    

print_lyrics()

song = print_lyrics()
print(song)
# #print("Connie Maganda") #builtin function called the print function