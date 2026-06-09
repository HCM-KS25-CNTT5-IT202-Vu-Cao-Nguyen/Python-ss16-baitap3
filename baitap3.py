from datetime import datetime

patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]


def find_patient_index(records, patient_id):
    """
    Tìm vị trí bệnh nhân theo mã bệnh nhân.

    Parameters:
        records (list): Danh sách hồ sơ bệnh án.
        patient_id (str): Mã bệnh nhân cần tìm.

    Returns:
        int:
            Index của bệnh nhân nếu tìm thấy.
            -1 nếu không tìm thấy.
    """
    patient_id = patient_id.strip().upper()

    for index, record in enumerate(records):
        if record.startswith(patient_id):
            return index

    return -1


def display_records(records):
    """
    Hiển thị danh sách hồ sơ bệnh án.

    Parameters:
        records (list): Danh sách hồ sơ bệnh án.

    Returns:
        None
    """
    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("\n--- DANH SÁCH BỆNH NHÂN ----------------------------------------------")

    for index, record in enumerate(records, start=1):
        patient_id, name, birth_year, diagnosis = record.split("-")

        print(
            f"{index}. [{patient_id}] "
            f"{name:<20} | "
            f"Năm sinh: {birth_year} | "
            f"Chẩn đoán: {diagnosis}"
        )

    print("---------------------------------------------------------------------")


def add_patient(records):
    """
    Thêm hồ sơ bệnh nhân mới.

    Parameters:
        records (list): Danh sách hồ sơ bệnh án.

    Returns:
        None
    """
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if find_patient_index(records, patient_id) != -1:
        print("\nMã bệnh nhân đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ")
    name = name.replace("-", " ").strip().title()

    current_year = datetime.now().year

    while True:
        birth_year = input("Nhập năm sinh: ").strip()

        if (
            birth_year.isdigit()
            and 1900 <= int(birth_year) <= current_year
        ):
            break

        print("Năm sinh không hợp lệ, vui lòng nhập lại!")

    diagnosis = input("Nhập chẩn đoán: ")
    diagnosis = diagnosis.replace("-", " ").strip().capitalize()

    record = "-".join([
        patient_id,
        name,
        birth_year,
        diagnosis
    ])

    records.append(record)

    print("\nThêm hồ sơ bệnh nhân thành công!")
    print("Dữ liệu được lưu:")
    print(record)


def update_diagnosis(records):
    """
    Cập nhật chẩn đoán theo mã bệnh nhân.

    Parameters:
        records (list): Danh sách hồ sơ bệnh án.

    Returns:
        None
    """
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input(
        "Nhập mã bệnh nhân cần cập nhật: "
    ).strip().upper()

    index = find_patient_index(records, patient_id)

    if index == -1:
        print(f"\nKhông tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    patient_data = records[index].split("-")

    print(f"\nTìm thấy bệnh nhân: {patient_data[1]}")
    print(f"Chẩn đoán hiện tại: {patient_data[3]}")

    new_diagnosis = input(
        "Nhập chẩn đoán mới: "
    )

    new_diagnosis = (
        new_diagnosis.replace("-", " ")
        .strip()
        .capitalize()
    )

    patient_data[3] = new_diagnosis

    records[index] = "-".join(patient_data)

    print("\nCập nhật chẩn đoán thành công!")
    print("Dữ liệu mới được lưu:")
    print(records[index])


def generate_age_report(records):
    """
    Báo cáo phân loại bệnh nhân theo độ tuổi.

    Parameters:
        records (list): Danh sách hồ sơ bệnh án.

    Returns:
        None
    """
    current_year = datetime.now().year

    children = 0
    adults = 0
    seniors = 0

    for record in records:
        birth_year = int(record.split("-")[2])

        age = current_year - birth_year

        if age < 16:
            children += 1
        elif age <= 60:
            adults += 1
        else:
            seniors += 1

    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    print(f"Trẻ em: {children} bệnh nhân")
    print(f"Trưởng thành: {adults} bệnh nhân")
    print(f"Người cao tuổi: {seniors} bệnh nhân")
    print("--------------------------------------")


def display_menu():
    """
    Hiển thị menu chức năng của hệ thống.

    Returns:
        None
    """
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
    print("1. Xem danh sách hồ sơ bệnh án")
    print("2. Thêm hồ sơ bệnh nhân mới")
    print("3. Cập nhật chẩn đoán theo Mã BN")
    print("4. Báo cáo phân loại theo độ tuổi")
    print("5. Thoát chương trình")
    print("==================================================")


def main():
    """
    Hàm điều khiển chương trình chính.

    Returns:
        None
    """
    while True:
        display_menu()

        try:
            choice = int(
                input("Chọn chức năng (1-5): ").strip()
            )

            match choice:
                case 1:
                    display_records(patient_records)

                case 2:
                    add_patient(patient_records)

                case 3:
                    update_diagnosis(patient_records)

                case 4:
                    generate_age_report(patient_records)

                case 5:
                    print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
                    break

                case _:
                    print("Lựa chọn không hợp lệ!")

        except ValueError:
            print("Lựa chọn không hợp lệ!")


main()