"""
Some functions to calculate frequentist p-values (and CLs) for the "on-off"
problem, that is, a counting experiment in an "on" region with background
expectation, signal expectation and an uncertainty on the background
expectation, constrained by a count in an "off" region.

See Eur.Phys.J.C71, `arXiv:1007.1727 <https://arxiv.org/abs/1007.1727>`_ ("CCGV paper") for the formulas.

Also see <http://www.pp.rhul.ac.uk/~cowan/stat/medsig/medsigNote.pdf> for a closed-form solution for p0/z0

Mainly, this module provides `z0_exp` and `cls_exp` to calculate the median
expected discovery significance and CLs.

Additionally, another common approach using the properties of the Binomial
distribution is also provided by `z0_exp_binomial`.
"""

import numpy as np
import scipy.stats
import scipy.special


def ll(n, m, mu, s, b, tau):
    "Log likelihood without factorials (cancel in ratio)"
    return n * np.log(mu * s + b) - (mu * s + b) + m * np.log(tau * b) - tau * b


def mles(mu, n, m, s, tau):
    "Maximum likelihood estimates, see eq. 91-93 in CCGV paper"
    muhat = (n - m / tau) / s
    bhat = m / tau
    bhathat = (
        n
        + m
        - (1 + tau) * mu * s
        + np.sqrt((n + m - (1 + tau) * mu * s) ** 2 + 4 * (1 + tau) * m * mu * s)
    ) / (2 * (1 + tau))
    return muhat, bhat, bhathat


def tau_from_db(b, db):
    """
    Calculate tau (the ratio between expected background in the off and on region)
    from the expected background and the absolute uncertainty on it.
    """
    return b / (db ** 2)


def nllr(mu, n, m, s, tau):
    """
    Negative log likelihood ratio
    """
    muhat, bhat, bhathat = mles(mu, n, m, s, tau)
    condll = ll(n, m, mu, s, bhathat, tau)
    uncondll = ll(n, m, muhat, s, bhat, tau)
    return uncondll - condll


def z0_exp(s, b, db):
    """
    Median expected discovery significance from signal expectation `s`,
    background expectation `b` and an absolute uncertainty on the background
    expectation `db`.
    """
    mu = 0
    tau = tau_from_db(b, db)
    n = s + b
    m = tau * b
    return np.sqrt(2 * nllr(mu, n, m, s, tau))


def cls_exp(s, b, db):
    """
    Median expected CLs from signal expectation `s`, background expectation `b`
    and an absolute uncertainty on the background expectation `db`.
    """
    mu = 1
    tau = tau_from_db(b, db)
    n = b
    m = tau * b
    zsb = np.sqrt(2 * nllr(mu, n, m, s, tau))
    clsb = scipy.stats.norm.sf(zsb)
    clb = 0.5
    return clsb / clb


def z0_exp_binomial(s, b, db):
    """
    Median expected discovery significance from signal expectation `s`,
    background expectation `b` and an absolute uncertainty on the background
    expectation `db`, here calculated using the binomial distribution. The
    assumption here is we pick n events out of n + m events and we know the
    probability from tau. The p-value is then given by the probability to pick
    at least n (and at most n + m) events which can be calculated from the
    incomplete beta function.

    Also see http://dx.doi.org/10.1016/j.nima.2008.07.086,
    http://arxiv.org/abs/physics/0702156 and the ROOT implementation:
    https://root.cern.ch/doc/master/NumberCountingUtils_8cxx_source.html#l00025
    """
    tau = tau_from_db(b, db)
    n = s + b
    m = tau * b

    a = n
    b = m + 1
    x = 1 / (1 + tau)
    p = scipy.special.betainc(a, b, x)

    return scipy.stats.norm.isf(p)
