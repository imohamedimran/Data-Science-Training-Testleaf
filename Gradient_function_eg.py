
#The gradient descent algorithm is applied to find a local minimum of the function f(x)=x4-3x3+2, with derivative #f'(x)=4x3-9x2. Here is an implementation in the Python programming language.

# From calculation, it is expected that the local minimum occurs at x=9/4

cur_x = 6 # The algorithm starts at x=6
gamma = 0.01 # step size multiplier - Learning rate
precision = 0.00001  #Difference
previous_step_size = 1 
max_iters = 100000 # maximum number of iterations
iters = 0 #iteration counter

df = lambda x: 4 * x**3 - 9 * x**2

while ((previous_step_size > precision) and (iters < max_iters)):
    prev_x = cur_x
    cur_x -= gamma * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    iters += 1
    print("cur_x",cur_x)
    print("gamma",gamma)
    print("prev_x",prev_x, '\n')
    

print("The local minimum occurs at", cur_x)
#The output for the above will be: ('The local minimum occurs at', 2.2499646074278457)