print("Sinh vien: Dinh viet khoi Nguyen")
print("Ma so SV  :  245752021610082")
print("################################")
def checkValue(n):
    """
    Kiểm tra một số nguyên n là chẵn hay lẻ và in ra kết quả tương ứng.
    """
    # Sử dụng toán tử modulo (%) để lấy số dư khi chia cho 2
    if n % 2 == 0:
        print("Đây là một số chẵn")
    else:
        print("Đây là một số lẻ")

# Ví dụ kiểm tra:
checkValue(7)  # Output: Đây là một số lẻ
checkValue(10) # Output: Đây là một số chẵn
