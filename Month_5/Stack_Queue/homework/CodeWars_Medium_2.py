# CodeWars_Medium_2 => DONE BY Azizbek

# The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80 

# Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the same manner as in the drawing:

# alternative text

def perimeter(n):
    
    a,b = 1,2

    while n:
        a,b = b,a+b
        n -= 1
    
    return 4 * (b - 1)