from sympy import *

from get_polynomial_feature import *

x = symbols('x')  # x为符号变量
x0 = -0.5  # 初值
x_list = [x0]
i = 0  # 计数器
polynomial_feature = get_polynomial(3, 5, -1, 0, 11)  # 待求解多项式


def f(x):
    f = eval(polynomial_feature)
    return f


while True:   
    if diff(f(x), x).subs(x, x0) == 0:  # subs()将变量x替换为x0;若f'(x0)=0
        print("极值点：", x0)
        break
    else:
        x0 = x0 - f(x0) / diff(f(x), x).subs(x, x0)  # 牛顿法
        x_list.append(x0)
    if len(x_list) > 1:
        i += 1
        error = abs((x_list[-1] - x_list[-2]) / x_list[-1])  # 计算误差
        if error < 10 ** (-6):
            print(f"迭代第 {i} 次后，误差小于 10^(-6)，误差为 {error}")
            break
    else:
        pass
print(f"{polynomial_feature} 的根为 {x_list[-1]}")
