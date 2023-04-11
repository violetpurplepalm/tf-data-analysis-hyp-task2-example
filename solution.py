import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

chat_id = 425154307 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    from scipy.stats import mannwhitneyu
    stat, p = mannwhitneyu(x, y)
    if p > 0.07:
        return False
    return True

