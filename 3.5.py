print("Sinh vien: Dinh viet khoi Nguyen")
print("Ma so SV  :  245752021610082")
print("################################")

a = "Hello Guy!"
def say():
 global a
 a = " Vinh University "
 print(a)

print(f"Giá trị của 'a' trước khi gọi hàm say(): {a}")
say()
print(f"Giá trị của 'a' sau khi gọi hàm say(): {a}")
