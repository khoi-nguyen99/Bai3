print("Sinh vien: Dinh viet khoi Nguyen")
print("Ma so SV  :  245752021610082")
print("################################")
import math

# pos[0] là tọa độ dọc (y), pos[1] là tọa độ ngang (x)
pos = [0, 0]

print("Nhập các lệnh di chuyển (ví dụ: UP 5). Nhấn Enter trống để kết thúc:")

while True:
    s = input()
    if not s:
        break
    
    # Tách chuỗi nhập thành hướng di chuyển và số bước
    try:
        movement = s.split(" ")
        direction = movement[0].upper() # Chuyển sang chữ hoa để đảm bảo khớp
        steps = int(movement[1])
    except:
        print("Định dạng nhập không hợp lệ. Vui lòng nhập lại.")
        continue # Bỏ qua vòng lặp này và tiếp tục vòng lặp mới

    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        print(f"Hướng di chuyển '{direction}' không hợp lệ.")

# Tính khoảng cách Manhattan (tọa độ y là pos[0], tọa độ x là pos[1])
# Khoảng cách từ (x, y) đến (0, 0) là sqrt(x^2 + y^2)
distance = math.sqrt(pos[1]**2 + pos[0]**2)

# In số nguyên gần nhất (sử dụng round() để làm tròn, sau đó int() để lấy phần nguyên)
print(f"Vị trí cuối cùng: ({pos[1]}, {pos[0]})")
print(f"Khoảng cách chính xác từ gốc: {distance}")
print(f"Kết quả (số nguyên gần nhất): {int(round(distance))}")

# Ví dụ minh họa:
# Input (lần lượt): UP 5, DOWN 3, LEFT 3, RIGHT 2
# pos cuối cùng: y = 5 - 3 = 2; x = -3 + 2 = -1. Vị trí (-1, 2)
# Khoảng cách: sqrt((-1)^2 + 2^2) = sqrt(1 + 4) = sqrt(5) ≈ 2.236
# Output mong đợi: 2
