from fpylll import *
from ProductArguVerifier import *
def prove():
    # Randomly select A_0, B_m+1

    # Select alpha_i, beta_i, gamma_i uniformly at random
    for i in range(1, m):

    # Request vector y from Verifier

    # Request vector x from Verifier


def elementwise( M, N ):
    print "M parent is: %s" % M.parent()
    print "N parent is: %s" % N.parent()

    assert( M.parent() == N.parent() )

    nc, nr = M.ncols(), M.nrows()
    A = copy( M.parent().zero() )

    for r in xrange(nr):
        for c in xrange(nc):
            A[r,c] = M[r,c] * N[r,c]
    return A