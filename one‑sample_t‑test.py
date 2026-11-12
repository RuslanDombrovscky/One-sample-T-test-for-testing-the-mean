import numpy as np
from scipy.stats import ttest_1samp

data = np.loadtxt("iris.data", delimiter=",", dtype=str)

sepal_length = data[data[:, 4] == "Iris-virginica"][:, 0].astype(float)

mu_0 = 6.0
stat, p_val = ttest_1samp(sepal_length, popmean=mu_0)

print(f"n = {len(sepal_length)}")
print(f"Среднее = {sepal_length.mean():.3f} см")
print(f"Одновыборочный t-тест: t = {stat:.4f}, p-value = {p_val:.4g}")

alpha = 0.05
if p_val < alpha:
    print(f"Среднее значимо отличается от {mu_0} см (p < {alpha})")
else:
    print(f"Нет оснований считать, что среднее отличается от {mu_0} см (p >= {alpha})")