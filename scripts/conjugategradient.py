import numpy as np

def conjugate_gradient(A, b, x=None, max_iter=512, reltol=1e-2, verbose=False):
    """
    Implements conjugate gradient method to solve Ax=b for a large matrix A that is not
    computed explicitly, but given by the linear function A. Also we need a preconditioning matrix precond
    """
    if verbose:
        print("Starting conjugate gradient...")
    if x is None:
        x=np.zeros_like(b)

    # cg standard
    r=b-A(x)
    d=r
    rsnew=np.sum(r.conj()*r).real
    rs0=rsnew

    if verbose:
        print("initial residual: {}".format(rsnew))

    ii=0
    while ((ii<max_iter) and (rsnew>(reltol**2*rs0))):
        ii=ii+1
        Ad=A(d)
        alpha=rsnew/(np.sum(d.conj()*Ad))
        x=x+alpha*d
        if ii%50==0:
            #every now and then compute exact residual to mitigate
            # round-off errors
            r=b-A(x)
            d=r
        else:
            r=r-alpha*Ad

        rsold=rsnew
        rsnew=np.sum(r.conj()*r).real
        d=r+rsnew/rsold*d

        if verbose:
            print("{}, residual: {}".format(ii, rsnew))
    return x


if __name__ == '__main__':
    matrixSize = 10

    # Set up simple Ax = b problem
    diag = np.random.rand(matrixSize).astype(np.float32)
    A_mat = np.diag(diag)
    b = np.ones_like(diag)

    def A(x):
        return A_mat.dot(x)

    x = conjugate_gradient(A, b, reltol=1e-3)

    # print Ax (=1)
    print(A_mat.dot(x))
