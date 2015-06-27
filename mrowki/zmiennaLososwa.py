__author__ = 'kuban'

import scipy.stats as st

class my_v(st.rv_discrete):
    def _pmf(self,x):
        if x in (2,3):
            return 0.5
        else:
            return 0

xk = range(7)
pk = [0.0, 0.0, 0.9, 0.1, 0.0, 0.0, 0.0]
custm = st.rv_discrete(name='custm', values=(xk, pk))

a = custm.rvs()
print(a)

# a =my_v()
# b=a.rvs(size=7)