print("Sinh vien: Dinh viet khoi Nguyen")
print("Ma so SV  :  245752021610082")
print("################################")
""" Program make a simple calculator that can add, subtract, multiply and
divide using functions"""

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    # Xử lý trường hợp chia cho 0
    if y == 0:
        return "Lỗi: Không thể chia cho 0"
    return x / y

print("Chọn phép toán.")
print("1.Cộng (+)")
print("2.Trừ (-)")
print("3.Nhân (*)")
print("4.Chia (/)")

try:
    # Lấy input từ người dùng
    choice = input("Nhập lựa chọn (1/2/3/4):")
    num1 = float(input("Nhập số thứ nhất: ")) # Sử dụng float để hỗ trợ số thập phân
    num2 = float(input("Nhập số thứ hai: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Lựa chọn không hợp lệ")

except ValueError:
    print("Lỗi: Đầu vào không phải là số hợp lệ.")
