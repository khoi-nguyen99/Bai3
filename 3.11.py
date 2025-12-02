print("Sinh vien: Dinh viet khoi Nguyen")
print("Ma so SV  :  245752021610082")
print("################################")
def benefit(t, n, k):
    """
    Tính tổng số tiền nhận được (vốn + lãi) sau k tháng theo công thức lãi kép.

    Args:
        t (float): Lãi suất tiết kiệm theo tháng (tính bằng phần trăm, ví dụ: 0.5)
        n (float): Số vốn ban đầu
        k (int): Số tháng gửi
    
    Returns:
        float or str: Tổng số tiền sau k tháng, hoặc thông báo lỗi nếu input không hợp lệ.
    """
    # 1. Kiểm tra tính hợp lệ của input
    if t < 0 or n < 0 or k < 0:
        return "Lỗi: Lãi suất, vốn gốc và số tháng phải là số không âm."
    
    # 2. Chuyển lãi suất từ phần trăm sang thập phân
    # Ví dụ: nếu t = 0.5% thì rate = 0.005
    monthly_rate = t / 100
    
    # 3. Tính tổng số tiền theo công thức lãi kép S = n * (1 + monthly_rate)^k
    # Sử dụng toán tử ** để tính lũy thừa
    tong_so_tien = n * (1 + monthly_rate) ** k
    
    return tong_so_tien

# --- Phần nhập liệu và hiển thị kết quả ---
try:
    # Nhập các giá trị từ bàn phím
    t_input = float(input("Nhập lãi suất t (%/tháng): "))
    n_input = float(input("Nhập số vốn ban đầu n: "))
    k_input = int(input("Nhập số tháng gửi k: "))

    # Gọi hàm để tính toán
    tong_tien = benefit(t_input, n_input, k_input)
    
    if isinstance(tong_tien, str):
        print(tong_tien)
    else:
        # Làm tròn kết quả đến 2 chữ số thập phân (đơn vị tiền tệ)
        print(f"\n✅ Tổng số tiền nhận được sau {k_input} tháng là: {tong_tien:.2f}")

except ValueError:
    print("Lỗi: Vốn gốc, lãi suất phải là số; số tháng phải là số nguyên.")
