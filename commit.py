from fpylll import *
from sage.all import *

'''Reading selected parameter from txt file'''
def read_param(filename):
    param_file = open(filename,"r") #Read only access mode"
    param_vec = []
    # 0. p
    p = int(param_file.readline())
    param_vec.append(p)
    # 1. q
    q = int(param_file.readline())
    param_vec.append(q)
    # 2. r
    r = int(param_file.readline())
    param_vec.append(r)
    # 3. v
    v = int(param_file.readline())
    param_vec.append(v)
    # 4. N
    N = int(param_file.readline())
    param_vec.append(N)
    # 5. B
    B = int(param_file.readline())
    param_vec.append(B)
    # 6. sigma
    sigma = int(param_file.readline())
    param_vec.append(sigma)
    # 7. Whether to use quotient ring (false=use Z itself)
    quotient = param_file.readline()
    param_vec.append(quotient)

    return param_vec


'''Get commitment key'''
def getCK(param_vec, m):
    ck = []

    quotient = param_vec[7]
    if quotient == 'T':
        R = Integers(q)
    else:
        R = IntegerRing()

    # choose A_1 matrix
    r = param_vec[2]
    p = param_vec[0]
    q = param_vec[1]
    # A_1 is a uniformly random matrix with dimension r, 2r*log_p(q)
    temp = log(q,p)
    A_1 = random_matrix(R, r, 2*r*temp)

    # choose A_2 matrix
    # A_2 is a uniformly random matrix with dimension r, n
    # n(number of elements that one wishes to commit to)
    n = len(m[0])
    A_2 = random_matrix(R, r, n)

    v = param_vec[3]
    l = len(m)
    N = param_vec[4]
    B = param_vec[5]

    ck.append(p)
    ck.append(q)
    ck.append(r)
    ck.append(v)
    ck.append(l) # total number of vectors one wishes to commit to
    ck.append(N)
    ck.append(B)
    ck.append(R) # the ring
    ck.append(A_1)
    ck.append(A_2)
    return ck

def commitment(ck, m):
    R = ck[7]
    A_1 = ck[8]
    A_2 = ck[9]
    # Generate randomnesses r (matrix)
    x = len(m) # total number of commitments
    y = len(m[0]) # len of each vector one wished to commit to
    r = random_matrix(R, y, x)

    c = A_1 * r + A_2 * m # calculate the (multi-)commitment
    return c

'''Given a file, this function reads the parameters
    and then pass them to make commitment

    param_filename: name of the file that stores the parameter
    m: vectors that one wishes to commit to'''
def commit(param_filename, m):
    
    param_vec = read_param(param_filename)
    ck = getCK(param_vec, m)
    return commitment

m = [0,1]
commit('parameters.txt',m)