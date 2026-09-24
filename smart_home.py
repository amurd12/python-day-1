'''
task: convert c to f
name: c_to_f
input: degrees_c
side effects: none
return: degrees_f
'''

def c_to_f(degrees_c):
    degrees_f = (degrees_c * 9/5 + 32)
    return degrees_f

'''
task: tell user current temp
name: prtint_temp
input: temp_in_f
side effects: "The tempature is: x"
return: none
'''

def print_temp(temp_in_f):
    print("The tempature is: ", temp_in_f)
    return None

def main():
    temp_in_c = input("what is temp in C") # ask for temp in c
    f_degrees = c_to_f(temp_in_c) # converts it to f
    print_temp(f_degrees) # calls the fn to tell the user the temp

    