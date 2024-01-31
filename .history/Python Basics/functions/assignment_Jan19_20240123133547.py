# Write functions that do the following:
# 1. Returns area and perimeterof a circle.
'''
def measure_circle():
    pi = 3.1416
    area_circle = pi*r**2
    peri_circle = 2*pi*r
    return area_circle, peri_circle    

r = float(input("Enter a radius: "))
area_circle, peri_circle = (measure_circle())
print(f"The area of a circle with radius of {r} is {area_circle}, while its perimeter is {peri_circle}")
'''

# 2. Returns volume of a sphere.
# V = 4/3pir^3

'''
def measure_sphere():
    pi = 3.1416
    two_cones = 4/3
    vol_sphere = two_cones*pi*r**3
    return vol_sphere

r = float(input("Enter a radius: "))
vol_sphere = measure_sphere()
print(f"The volume of a sphere with radius of {r} is {vol_sphere}")
'''


#Combining item 1 and 2



def calculate_shapes():
    diameter = float(input("Enter a diameter: "))
    pi = 3.1416
    two_cones = 4/3
    r = diameter/2
    area_circle = pi*r**2
    peri_circle = 2*pi*r
    vol_sphere = two_cones*pi*r**3
    return area_circle, peri_circle, vol_sphere


area_circle, peri_circle, vol_sphere = calculate_shapes()
print(f"The area of a circle with radius of {r} is {area_circle}.\nThe perimeter of a circle with radius of {r} is {peri_circle}.\nThe volume of a sphere with radius of {r} is {vol_sphere}")

    
    



#3. Write a function to check whether a number is prime or not
#num = 37
'''
num = int(input("Enter a number: "))

if num == 1:
    print(f"{num} is not a prime number.")
if num == 2:
    print(f"{num} is a prime number.")
elif num > 1:
    for i in range(2, num):
        if(num%i)==0:
            print(f"{num} is not a prime number.")           
            break
        else:
            print(f"{num} is a prime number.")
            break
'''

'''
def is_prime(num):
    if num == 1:
        print(f"{num} is not a prime number")
    if num == 2:
       print(f"{num} is a prime number")

    elif num > 1:
        for i in range(2, num):
            if(num%i)==0:
                print(f"{num} is not a prime number.")
                break
            else:
                print(f"{num} is a prime number.")
                break

num = is_prime(int(input("Enter a number > 0: ")))
'''

#4. Write a function to check whether a number is odd or even
'''
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")
'''

'''
def even_or_odd(num):
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

num = even_or_odd(int(input("Enter a number: ")))
'''



#Combining item 3 and item 4
'''

num = int(input("Enter a number: "))

def classify_number():
    if num == 1:
        print(f"{num} is not a prime number.")
    if num == 2:
        print(f"{num} is a prime number.")

#Identify if a number is an even or odd number     
        
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

#Identify is a number is a prime number or not
        
    if num > 1:
        for i in range(2, num):
            if(num%i)==0:
                print(f"{num} is not a prime number.")
                break
            else:
                print(f"{num} is a prime number.")
                break
              
classify_number()             
'''           
       




   
