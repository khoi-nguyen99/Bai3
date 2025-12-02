print("Sinh vien: Dinh viet khoi Nguyen")
print("Ma so SV  :  245752021610082")
print("################################")
import math

def Tinh(R):
    """
    Tính chu vi và diện tích hình tròn với bán kính R.

    Args:
        R (float): Bán kính của hình tròn.
    
    Returns:
        tuple or str: (Chu vi, Diện tích) nếu R hợp lệ, hoặc thông báo lỗi nếu không.
    """
    # 1. Kiểm tra tính hợp lệ của bán kính
    if R is None or R < 0:
        return "Lỗi: Bán kính phải là một số không âm (R >= 0)."
    
    # 2. Tính toán
    # Công thức Chu vi: C = 2 * pi * R
    chu_vi = 2 * math.pi * R
    
    # Công thức Diện tích: A = pi * R^2
    dien_tich = math.pi * (R ** 2)
    
    return chu_vi, dien_tich

# --- Phần nhập liệu và hiển thị kết quả ---
try:
    # Nhập bán kính từ bàn phím (sử dụng float để chấp nhận số thập phân)
    R_input = float(input("Vui lòng nhập bán kính R của hình tròn: "))
    
    # Gọi hàm để tính toán
    ket_qua = Tinh(R_input)
    
    if isinstance(ket_qua, str):
        # In thông báo lỗi
        print(ket_qua)
    else:
        # In kết quả (ket_qua là một tuple: (chu_vi, dien_tich))
        chu_vi, dien_tich = ket_qua
        print(f"\n✅ Với bán kính R = {R_input}:")
        print(f"   Chu vi hình tròn (C): {chu_vi:.2f}")
        print(f"   Diện tích hình tròn (A): {dien_tich:.2f}")

except ValueError:
    print("Lỗi: Đầu vào không phải là một số hợp lệ.")
