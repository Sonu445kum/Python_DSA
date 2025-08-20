try:
    x = int("str")  # This will cause ValueError
    
    #inverse
    inv = 1 / x
    
except ValueError:
    print("Not Valid!")
    
except ZeroDivisionError:
    print("Zero has no inverse!")



a = ["10", "twenty", 30]  # Mixed list of integers and strings
try:
    total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int
    
except (ValueError, TypeError) as e:
    print("Error", e)
    
except IndexError:
    print("Index out of range.")


try:
    # Simulate risky calculation: incorrect type operation
    res = "100" / 20
    
except ArithmeticError:
    print("Arithmetic problem.")
    
except:
    print("Something went wrong!")