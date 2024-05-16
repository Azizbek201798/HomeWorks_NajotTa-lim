# CodeWars_Medium_2 => DONE BY Azizbek;

# Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.

# Examples
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7Test"        -->  "app7_test"
# 1                 -->  "1"

def to_underscore(string):

    result = ""

    if type (string) == int:
        return str(string)

    for i in str(string):

        if i.isupper():
            result += "_"
            result += i.lower()
        else:
            result += i.lower()
    
    result = result[1:]

    return result
