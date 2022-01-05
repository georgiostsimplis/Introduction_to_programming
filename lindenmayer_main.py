'''
Project II - Lindenmayer systems 
================================
Authors: Georgios Tsimplis (s200166), Viktor Törnblom (s200116)
(The both authors contributed equally)

'''
import math
import matplotlib.pyplot as plt
import numpy as np

# Koch triangle, replacement rules
def koch(char):
    if char == 'S':
        return 'SLSRSLS'
    elif char == 'L':
        return 'L'
    elif char == 'R':
        return 'R'

# Sierpinski triangle, replacement rules
def sierpinski(char):
    if char == 'A':
        return 'BRARB'
    elif char == 'B':
        return 'ALBLA'
    elif char == 'L':
        return 'L'
    elif char == 'R':
        return 'R'

# Dragon curve, replacement rules
def dragon(char):
    if char == 'F':
        return 'FMH'
    elif char == 'H':
        return 'FPH'
    elif char == 'M':
        return 'M'
    elif char == 'P':
        return 'P'

#Lindenmayer Iteration Function
def lind_iter(system, N):
    if system == 'Koch':
        lindenmayer_string = 'S'
        for i in range(N):
            temp_str = ''
            for b in lindenmayer_string:
                temp_str = temp_str + koch(b)
            lindenmayer_string = temp_str
    elif system == 'Sierpinski':
        lindenmayer_string = 'A'
        for i in range(N):
            temp_str = ''
            for b in lindenmayer_string:
                temp_str = temp_str + sierpinski(b)
            lindenmayer_string = temp_str
    elif system == 'Dragon':
        lindenmayer_string = 'F'
        for i in range(N):
            temp_str = ''
            for b in lindenmayer_string:
                temp_str = temp_str + dragon(b)
            lindenmayer_string = temp_str
    return lindenmayer_string

#Translation to turtle graphics commands
def turtle_graph(lindenmayer_string):
    turtle_commands = []
    for char in lindenmayer_string:
        # Koch curve
        if 'S' in lindenmayer_string:
            if char == 'S':
                l = 1/(3**N)
                turtle_commands.append(l)
            elif char == 'L':
                f = (math.pi)/3
                turtle_commands.append(f)
            elif char == 'R':
                f = -(2*math.pi)/3
                turtle_commands.append(f)
        # Sierpinski triangle
        elif 'A' in lindenmayer_string:
            if char in ('A', 'B'):
                l = 1/(2**N)
                turtle_commands.append(l)
            elif char == 'L':
                f = (math.pi)/3
                turtle_commands.append(f)
            elif char == 'R':
                f = -(math.pi)/3
                turtle_commands.append(f)
        # Dragon curve
        else:
            if char in ('F', 'H'):
                l = 1/(2**N)
                turtle_commands.append(l)
            elif char == 'P':
                f = (math.pi)/2
                turtle_commands.append(f)
            elif char == 'M':
                f = -(math.pi)/2
                turtle_commands.append(f)
    return turtle_commands


#Turtle graphics plot function
def turtle_plot(turtle_commands):
    #Initallize data
    x0 = np.array([0, 0])
    x = [x0]
    d = np.array([1, 0])
    x0 = turtle_commands[0]*d
    x.append(x0)
    #calculate the coordinates
    for i in range(0, len(turtle_commands)-1, 2):
        matrix = np.array([[math.cos(turtle_commands[i+1]),
                            -math.sin(turtle_commands[i+1])],
                           [math.sin(turtle_commands[i+1]),
                            math.cos(turtle_commands[i+1])]])
        d = np.dot(matrix, d)
        x0 = x0+turtle_commands[i]*d
        x.append(x0)
    #Divide the coordinates in x and y
    x1 = []
    x2 = []
    for j in range(len(x)):
        x1.append(x[j][0])
        x2.append(x[j][1])
    #Plot the curve
    plt.plot(x1, x2)
    plt.title('{}\n{} iterations'.format(plt_title, N))
    plt.show()
 #Function to calculate curve's length   
def curve_length(option1,N):
    length = 0
    if option1 == '1':
        curve = turtle_graph(lind_iter('Koch', N))
    elif option1 == '2':
        curve = turtle_graph(lind_iter('Sierpinski', N))
    else:
        curve = turtle_graph(lind_iter('Dragon', N))
    #choose every second element which corresponds to curve's unit
    for i in range(0,len(curve),2):
        length=length+curve[i]
    return length

# Main script----------------------------------------------------------
    #1st Menu Block
while True:
    print("\n\t\t ***WELCOME TO LINDENMYER SYSTEMS SOFTWARE*** ")
    print("\n==========================================================")
    print("Select one of the following Lindenmayer systems:\n \
    1. Koch Curve \n \
    2. Sierpinski Triangle\n \
    3. Dragon Curve\n \
    4. Quit\n")
    menu1_choices=['1','2','3']
    option1=input("Your choice is : ")
    if option1 == '4':
        print("\n \t\t\t ***  GOODBYE !!!  ***")
        break
    # Procced to ask for iterations & Manipulation of Errorneous inputs as iterations
    elif option1 in menu1_choices:
        while True:
            try:
                print("\nPlease choose the number of iterations\n*Choose an integer between [0-11]\n")
                N=int(input("Your choice is : "))
                if N<0:
                    print("\nInvalid nput! Please try again...")
                    print("\n==========================================================")
                elif N>11:
                    print("\n Please choose a reasonable number of Iterations!!!")
                    print('\n==========================================================')
                else:
                    break
            except ValueError:
                print("\nInvalid Input! Please try again...")
                print("\n==========================================================")
        
   #2nd Menu Block             
        while True:
            print("\n==========================================================")
            print("How do you want to proceed?\n \
    1. Display the Plot \n \
    2. Calculate Curve's Length \n \
    3. Go back")
            option2=input("Your choice is : ")
            if option2 == '1':
                if option1 == '1':
                    plt_title = "Koch Curve"
                    turtle_plot(turtle_graph(lind_iter('Koch', N)))
                elif option1 == '2':
                    plt_title = "Sierpinski triangle"
                    turtle_plot(turtle_graph(lind_iter('Sierpinski', N)))
                elif option1 == '3':
                    plt_title = "Dragon curve"
                    turtle_plot(turtle_graph(lind_iter('Dragon', N)))
            elif option2 == '2':
                print("Curve's Length is:",curve_length(option1,N))
            elif option2 == '3':
                break
            else:
                print("Invalid Input! Please try again... ")
                print("\n==========================================================")
                
    #Manipulate invalid input of 1st menu    
    else:
        print("\nInvalid Input! Please try again...\n")