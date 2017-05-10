import numpy
from numpy import arange, isrealobj
from pylab import rms_flat

__all__ = ['CORRELATION', 'xcorr']


def CORRELATION(x, y=None, maxlags=None, norm='unbiased'):
    assert norm in ['unbiased', 'biased', 'coeff', None]
    if y is None:
        y = x

    N = max(len(x), len(y))
    if len(x) < N:
        y = y.copy()
        y.resize(N)
    if len(y) < N:
        y = y.copy()
        y.resize(N)

    if maxlags is None:
        maxlags = N - 1
    assert maxlags < N, 'lag must be less than len(x)'

    realdata = isrealobj(x) and isrealobj(y)
    if realdata is True:
        r = numpy.zeros(maxlags, dtype=float)
    else:
        r = numpy.zeros(maxlags, dtype=complex)

    if norm == 'coeff':
        rmsx = rms_flat(x)
        rmsy = rms_flat(y)

    for k in range(0, maxlags+1):
        nk = N - k - 1

        if realdata is True:
            sum = 0
            for j in range(0, nk+1):
                sum = sum + x[j+k] * y[j]
        else:
            sum = 0. + 0j
            for j in range(0, nk+1):
                sum = sum + x[j+k] * y[j].conjugate()
        if k == 0:
            if norm in ['biased', 'unbiased']:
                r0 = sum/float(N)
            elif norm is None:
                r0 = sum
            else:
                r0 = 1.
        else:
            if norm == 'unbiased':
                r[k-1] = sum / float(N-k)
            elif norm == 'biased':
                r[k-1] = sum / float(N)
            elif norm is None:
                r[k-1] = sum
            elif norm == 'coeff':
                r[k-1] = sum/(rmsx*rmsy)/float(N)

    r = numpy.insert(r, 0, r0)
    return r
 

def xcorr(x, y=None, maxlags=None, norm='biased'):
    N = len(x)
    if y is None:
        y = x
    assert len(x) == len(y), 'x and y must have the same length. Add zeros if needed'
    assert maxlags <= N, 'maxlags must be less than data length'

    if maxlags is None:
        maxlags = N-1
        lags = arange(0, 2*N-1)
    else:
        assert maxlags < N
        lags = arange(N-maxlags-1, N+maxlags)

    res = numpy.correlate(x, y, mode='full')

    if norm == 'biased':
        Nf = float(N)
        res = res[lags] / float(N)    # do not use /= !! 
    elif norm == 'unbiased':
        res = res[lags] / (float(N)-abs(arange(-N+1, N)))[lags]
    elif norm == 'coeff':        
        Nf = float(N)
        rms = rms_flat(x) * rms_flat(y)
        res = res[lags] / rms / Nf
    else:
        res = res[lags]

    lags = arange(-maxlags, maxlags+1)
    return res, lags