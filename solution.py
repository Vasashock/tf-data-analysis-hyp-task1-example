import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)
    se = np.sqrt(p * (1 - p) * (1 / x_cnt + 1 / y_cnt))
    z = (p1 - p2) / se
    return not(-1.96 <= z <= 1.96)

