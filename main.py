import matplotlib.pyplot as plt
import AO3
import scipy
import numpy as np

AO3.extra.download_all_threaded()
AO3.utils.load_fandoms()

def func(x, k, a):
    return k * np.array(x).astype(float) ** a

y_data = list(AO3.utils._FANDOMS.values())
x_data = range(0, max(y_data) + 1)
x_max = 100
hist, edges = np.histogram(y_data, bins = x_data)

popt, pcov = scipy.optimize.curve_fit(func, edges[1:-1], hist[1:], p0=(10000, -2))
print(popt)

plt.stairs(hist[:x_max], edges[:x_max + 1], fill=True, label="Work function of AO3 fandoms")
label_string = "$" + str(popt[0]) + r"x^{" + str(popt[1]) + "}$" #can't be bothered to figure out f strings with MathML...
plt.plot(range(0, x_max + 1), func(range(0, x_max + 1), *popt), label=label_string)

plt.xlim(1, x_max)
plt.legend()
plt.tight_layout()
plt.savefig("ao3_distribution.png")
plt.show()
