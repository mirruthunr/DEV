import pandas as p
import numpy as n
import matplotlib.pyplot as m
import statsmodels.api as s
from statsmodels.graphics.tsaplots import plot_acf

n.random.seed(0)
a = p.date_range(start='2020-01-01', end='2023-12-31', freq='M')
b = n.random.randint(10000, 50000, len(a))
c = p.DataFrame({'Date': a, 'Sales': b})
c.set_index('Date', inplace=True)

# Line Plot
m.plot(c.index, c['Sales'])
m.title('Monthly Sales')
m.xlabel('Date')
m.ylabel('Sales')
m.grid(True)
m.show()

# Decompose
d = s.tsa.seasonal_decompose(c['Sales'], model='additive', period=12)
d.plot()
m.show()

# Autocorrelation
plot_acf(c['Sales'], lags=24)
m.title('Autocorrelation')
m.show()

# Rolling Stats
mean = c['Sales'].rolling(12).mean()
std = c['Sales'].rolling(12).std()
m.plot(c['Sales'], label='Sales')
m.plot(mean, label='Mean', color='red')
m.plot(std, label='Std Dev', color='green')
m.legend()
m.title('Rolling Statistics')
m.grid(True)
m.show()
