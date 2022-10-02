def get_polynomial(*n):
    """生成多项式。第一个形参为次数，其他形参为系数"""
    power, coefficients = n[0], {}
    for i in range(power+1):
        coefficients['a' + str(i+1)] = n[i+1]  # 存储系数的字典

    counter = 0
    polynomial = ""
    while counter <= power:
        poly = coefficients[f'a{counter+1}']
        if abs(poly) != 1:  # 判断系数绝对值是否为1
            if counter != 0:  # 判断是否为最高次项
                if power-counter != 1:  # 判断是否为一次项
                    if counter != power:  # 判断是否为常数项
                        if poly > 0:
                            polynomial += f"+{poly}*x**{power-counter}"
                        elif poly < 0:
                            polynomial += f"{poly}*x**{power-counter}"
                        else:
                            pass
                    else:
                        if poly > 0:
                            polynomial += '+' + str(poly)
                        elif poly < 0:
                            polynomial += '-' + str(poly)
                        else:
                            pass
                else:
                    if poly > 0:
                        polynomial +=  "+" + str(poly) + "*x"
                    elif poly < 0:
                        polynomial +=  "-" + str(poly) + "*x"
                    else:
                        pass
            else:
                if poly > 0:
                    polynomial += f"{poly}*x**{power-counter}"
                elif poly < 0:
                    polynomial += f"{poly}*x**{power-counter}"
                else:
                    pass
        else:
            if counter != 0:
                if power-counter != 1:
                    if counter != power:
                        if poly > 0:
                            polynomial += f"+x**{power-counter}"
                        else:
                            polynomial += f"-x**{power-counter}"
                    else:
                        if poly > 0:
                            polynomial += '+1'
                        else:
                            polynomial += '-1'
                else:
                    if poly > 0:
                        polynomial += "+x"
                    else:
                        polynomial += "-x"
            else:
                if poly > 0:
                    polynomial += f"x**{power-counter}"
                elif poly < 0:
                    polynomial += f"-x**{power-counter}"
                else:
                    pass
        counter += 1
    return polynomial


if __name__ == '__main__':
    print(get_polynomial(3, 5, -1, 0, 11))