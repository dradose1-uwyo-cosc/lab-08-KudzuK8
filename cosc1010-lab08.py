# Nelia Koontz
# UWYO COSC 1010
# 11/07/2024
# Lab 08
# Lab Section: 15
# Sources, people worked with, help given to:
# Emmanuel gave a hint about the check_string function. I was going to 
# write it in a similar way to begin with, but I didn't realize you could do
# two variables this way with one except. His way broke when I put an float in, I suspect
# because the first var breaks so it moves on to except instead of trying again. So I made it two 
# try statements, then it kept turning the ints to floats, so I added a if "." is present statement
# to solve that. I didn't think of making the value itself False, which was an interesting concept.
# that didn't work in the second function because there are several vars.
# Google search "how to use return variable in python" gave me the idea to call the function
# in a variable (this was very exciting because I have been struggling with how in the heck you use
# return. This would have been very helpful for the last homework.). I also had to ask Daniel Radosevich
# how to unsquare a number for the square root. Google search "how to turn a number negative," which said
# time it by negative one (duh, my brain is slow today)


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them

def check_string(num):
    return_value = False
    try:
        if "." in num:
            return_value = (float(num))
    except:
        pass
    try:
        return_value = (int(num))
    except:
        pass
    return return_value

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, low_bound, up_bound):
    y_list = []
    if low_bound <= up_bound and low_bound == int(low_bound) and up_bound == int(up_bound):
        bounds_list = range(low_bound, (up_bound+1))
    else:
        return ("False")
    try:
        for bound in bounds_list:
            y = ((m*(bound)) + b)
            y_list.append(int(y))
        #print(y_list)
    except:
        pass
    return y_list

while True:
    m_in = input("Please enter a slope: (enter 'exit' to quit):")
    if m_in.lower()== 'exit':
        break
    else:
        m = check_string(m_in)
        
    b_in = input("Please enter an intercept: (enter 'exit' to quit)")
    if b_in.lower() == 'exit':
        break
    else:
        b = check_string(b_in)
        
    up_bound_in = input("Please enter an upper bound: (enter 'exit' to quit)")
    if up_bound_in.lower() == 'exit':
        break
    else:
         up_bound = (check_string(up_bound_in))
        
    low_bound_in = input("Please enter a lower bound: (enter 'exit' to quit)")
    if low_bound_in.lower() == 'exit':
        break
    else:
        low_bound= (check_string(low_bound_in))
    break

out_print = slope_intercept(m, b, low_bound, up_bound)
print(out_print)

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def quad_eq(sq_rt_num, a, b, c):
    """a function that calculates the quadratic equation"""
    num_out = []
    try:
        add_num = (((b * -1) + (sq_rt_num**(1/2))) / (2*a))
        num_out.append(add_num)
    except:
        return ("Can't divide by zero!") 
    try:
        sub_num = (((b * -1) - (sq_rt_num**(1/2))) / (2*a))
        num_out.append(sub_num)
    except:
        return ("Can't divide by zero!")
    else:
        return(num_out)
        
while True:
    a_in = input("Please input a value for a: (enter 'exit' to quit)")
    if a_in.lower() == 'exit':
        break
    else:
        a = check_string(a_in)
    b_in = input("Please enter a value for b: (enter 'exit' to quit):")
    if b_in.lower() == 'exit':
        break
    else:
        b = check_string(b_in)
    c_in = input("Please enter a value for c: (enter 'exit' to quit):")
    if c_in.lower() == 'exit':
        break
    else:
        c = check_string(c_in)
    break
#convert to int 
num_for_sq_rt = sq_root_op(a, b, c)
if num_for_sq_rt == 'null':
    print("null")
else:
    quad_eq_out = quad_eq(num_for_sq_rt, a, b, c)
    print(quad_eq_out)