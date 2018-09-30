# This is an application of BSM evaluation to Geometric asian option price
import numpy as np
import scipy.stats as ss
import time
import math
S0 = 100.0 #initial stock price
K = 110.0 #strike
r=0.0475 #interest rate
sigma = 0.20 #volatility 
T = 1. #maturity
Otype='C' #Call type
n = 4 #number of periods
t = np.linspace(0., T, n+1)[1:] #times to be used for geometric averaging stock price ???
def d1f(St, K, t, T, r, sigma):
    d1 = (math.log(St / K) + (r + 0.5 * sigma ** 2)
          * (T - t)) / (sigma * math.sqrt(T - t))
    return d1
def BSM_call_value(St, K, t, T, r, sigma):
    d1 = d1f(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T - t)
    call_value = St * ss.norm.cdf(d1) - math.exp(-r * (T - t)) * K * ss.norm.cdf(d2)
    return call_value
#calcule sigma_hat and r_hat for GAC price
sigma_hat=sigma/n*math.sqrt((n+1)*(2*n+1)/6)
r_hat=1/2*sigma_hat**2+(n+1)*(r-1/2*sigma**2)/(2*n)
GAC=math.exp((r_hat-r)*T)*BSM_call_value(S0, K, 0, T, r_hat, sigma_hat)
print('GAC price = ', GAC)