import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu
from scipy.stats import ks_2samp
from scipy.stats import cramervonmises_2samp
from scipy.stats import mode

chat_id = 425154307 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, p1 = mannwhitneyu(x, y)
    stat, p2 = ks_2samp(x, y)
    res = cramervonmises_2samp(x, y)
    p3 = res.pvalue
    bin1 = (p1 > 0.07)
    bin2 = (p2 > 0.07)
    bin3 = (p3 > 0.07)
    
    return (not mode([bin1, bin2, bin3]))
    

