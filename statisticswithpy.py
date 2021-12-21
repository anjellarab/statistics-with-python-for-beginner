import statistics
import numpy as np
import statistics
import pandas as pd
import math
# First
x = [8, 1, 2.5, 4, 28.0]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]
print('x = ',x)
print('xNAN = ',x_with_nan)
y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)
print('y array = ',y)
print(y_with_nan)
print(z)
print(z_with_nan)
mean_ = sum(x) / len(x)
print(mean_)
mean_ = statistics.mean(x)
print(mean_)
mean_ = statistics.fmean(x)
print(mean_)
mean_ = np.mean(x)
print(mean_)
print(np.mean(y_with_nan))
print(y_with_nan.mean())
print(np.nanmean(y_with_nan))
