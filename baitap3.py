# =============================================================
#  HỆ THỐNG QUẢN LÝ BỆNH NHÂN NỘI TRÚ RIKKEI HOSPITAL
# =============================================================

# Danh sách bệnh nhân ban đầu (List of Lists)
patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B",  "Nu",  "Sot Xuat Huyet"]
]


# -------------------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------------------

def validate_gender(gender_input):
    """Kiểm tra giới tính hợp lệ. Trả về True nếu là 'nam' hoặc 'nu'."""
    return gender_input.strip().lower() in ["nam", "nu"]


def find_patient_index(patient_list, patient_id):
    """Tìm index của bệnh nhân theo mã BN. Trả về index hoặc -1 nếu không thấy."""
    patient_id = patient_id.strip().upper()
    for i in range(len(patient_list)):
        if patient_list[i][0] == patient_id:
            return i
    return -1


# -------------------------------------------------------------
# CHỨC NĂNG 1: HIỂN THỊ DANH SÁCH BỆNH NHÂN
# -------------------------------------------------------------

def display_patients(patient_list):
    """In ra toàn bộ danh sách bệnh nhân đang điều trị."""
    print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")
    if len(patient_list) == 0:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return
    for i in range(len(patient_list)):
        p = patient_list[i]
        print(f"{i + 1}. Mã: {p[0]} | Tên: {p[1]} | Giới tính: {p[2]} | Bệnh: {p[3]}")


# -------------------------------------------------------------
# CHỨC NĂNG 2: TIẾP NHẬN BỆNH NHÂN MỚI
# -------------------------------------------------------------

def add_patient(patient_list):
    """Tiếp nhận bệnh nhân mới, chuẩn hóa dữ liệu và thêm vào danh sách."""
    print("----- TIẾP NHẬN BỆNH NHÂN MỚI -----")

    # Nhập và kiểm tra mã bệnh nhân
    ma_bn = input("Nhập mã bệnh nhân: ").strip().upper()
    if len(ma_bn) == 0:
        print("Mã bệnh nhân không được để trống!")
        return
    if find_patient_index(patient_list, ma_bn) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return

    # Nhập và kiểm tra tên bệnh nhân
    ten_bn = input("Nhập tên bệnh nhân: ").strip().title()
    if len(ten_bn) == 0:
        print("Tên bệnh nhân không được để trống!")
        return

    # Nhập và kiểm tra giới tính (vòng lặp đến khi hợp lệ)
    while True:
        gioi_tinh = input("Nhập giới tính Nam/Nu: ")
        if validate_gender(gioi_tinh):
            gioi_tinh = gioi_tinh.strip().title()
            break
        print("Giới tính không hợp lệ, vui lòng nhập lại!")

    # Nhập và kiểm tra chẩn đoán bệnh
    chan_doan = input("Nhập chẩn đoán bệnh: ").strip().capitalize()
    if len(chan_doan) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return

    # Gói thành list con và thêm vào danh sách
    patient_list.append([ma_bn, ten_bn, gioi_tinh, chan_doan])
    print("Tiếp nhận bệnh nhân thành công!")


# -------------------------------------------------------------
# CHỨC NĂNG 3: CẬP NHẬT CHẨN ĐOÁN BỆNH
# -------------------------------------------------------------

def update_diagnosis(patient_list):
    """Cập nhật chẩn đoán bệnh của bệnh nhân theo mã BN."""
    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")

    # Nhập và kiểm tra mã bệnh nhân
    ma_bn = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()
    if len(ma_bn) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    # Tìm bệnh nhân trong danh sách
    index = find_patient_index(patient_list, ma_bn)
    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {ma_bn}!")
        return

    # Hiển thị thông tin hiện tại
    print(f"Tìm thấy bệnh nhân: {patient_list[index][1]}")
    print(f"Chẩn đoán hiện tại: {patient_list[index][3]}")

    # Nhập và kiểm tra chẩn đoán mới
    chan_doan_moi = input("Nhập chẩn đoán mới: ").strip().capitalize()
    if len(chan_doan_moi) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return

    # Cập nhật vào đúng vị trí index 3 của list con
    patient_list[index][3] = chan_doan_moi
    print("Cập nhật chẩn đoán bệnh thành công!")


# -------------------------------------------------------------
# CHỨC NĂNG 4: TÌM KIẾM VÀ THỐNG KÊ THEO TÊN BỆNH
# -------------------------------------------------------------

def search_by_disease(patient_list):
    """Tìm kiếm bệnh nhân theo từ khóa tên bệnh, không phân biệt hoa/thường."""
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")

    # Nhập và kiểm tra từ khóa
    keyword = input("Nhập từ khóa tên bệnh: ").strip()
    if len(keyword) == 0:
        print("Từ khóa tìm kiếm không được để trống!")
        return

    # Duyệt danh sách, tìm theo từ khóa không phân biệt hoa/thường
    results = []
    for p in patient_list:
        if keyword.lower() in p[3].lower():
            results.append(p)

    # In kết quả
    print("Kết quả tìm kiếm:")
    if len(results) == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")
    else:
        for i in range(len(results)):
            p = results[i]
            print(f"{i + 1}. Mã: {p[0]} | Tên: {p[1]} | Giới tính: {p[2]} | Bệnh: {p[3]}")

    print(f"Có tổng cộng {len(results)} bệnh nhân mắc bệnh liên quan đến '{keyword}'.")


# -------------------------------------------------------------
# MAIN FLOW — VÒNG LẶP CHÍNH
# -------------------------------------------------------------

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
    print("1. Hiển thị danh sách bệnh nhân")
    print("2. Tiếp nhận bệnh nhân mới")
    print("3. Cập nhật chẩn đoán bệnh theo mã BN")
    print("4. Tìm kiếm và thống kê theo tên bệnh")
    print("5. Thoát chương trình")
    print("===========================================")

    lua_chon = input("Nhập lựa chọn của bạn: ").strip()

    if lua_chon == "1":
        display_patients(patients)
    elif lua_chon == "2":
        add_patient(patients)
    elif lua_chon == "3":
        update_diagnosis(patients)
    elif lua_chon == "4":
        search_by_disease(patients)
    elif lua_chon == "5":
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")
