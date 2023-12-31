import math

# Hàm tính gần đúng giá trị của e^x với sai số 10^(-4)
def approximate_exp(x):
    n = 1
    result = 1
    while True:
        term = x ** 2 / n
        result += term
        n += 1
        if term < 1e-4:
            break
    return result

# Yêu cầu người dùng nhập giá trị x
x = float(input("Nhập giá trị x: "))

# Tính gần đúng giá trị của e^x và in ra kết quả
approximation = approximate_exp(x)
true_value = math.exp(x)
print(f"Gần đúng giá trị của e^{x} là {approximation}")
print(f"Giá trị thực tế của e^{x} là {true_value}")