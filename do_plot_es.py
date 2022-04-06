#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy

import thermo

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(3, 3))

th = thermo.Thermo(data=dict(T=numpy.linspace(230, 280)))
ax.plot(th.get('T'), th.get('esati') / 100., label="$e_{si}$")
ax.plot(th.get('T'), th.get('esatw') / 100., label="$e_{sw}$")
ax.legend(loc=2)
ax.set_xlabel('T (K)')
ax.set_ylabel('e (hPa)')
fig.tight_layout()
plt.show()
