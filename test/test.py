from scipy.stats.stats import pearsonr
import scipy
from scipy.stats import pearsonr

x = scipy.array([-0.65499887,  2.34644428, 3.0])
y = scipy.array([-1.46049758,  3.86537321, 21.0])

r_row, p_value = pearsonr(x, y)

print r_row , p_value