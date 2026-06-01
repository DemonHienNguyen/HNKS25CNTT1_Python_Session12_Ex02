saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

LINE = "-"*60
LINE_EQUAL = "="*61
while True:
    try:
        choose = int(input(
        f"{LINE} \n"
        f"{" HỆ THỐNG QUẢN LÝ TÀI KHOẢN TECHBANK ".center(61, "=")}\n"
        f"{"| 1. Xem danh sách sổ tiết kiệm".ljust(60, " ")}|\n"
        f"{"| 2. Mở sổ tiết kiệm".ljust(60, " ")}|\n"
        f"{"| 3. Cập nhật thông tin sổ tiết kiệm".ljust(60, " ")}|\n"
        f"{"| 4. Tất toán hoặc xóa sổ tiết kiệm".ljust(60, " ")}|\n"
        f"{"| 5. Tính lãi dự kiến khi đến hạn".ljust(60, " ")}|\n"
        f"{"| 6. Kiểm tra điều kiện rút trước hạn".ljust(60, " ")}|\n"
        f"{"| 7. Thoát chương trình".ljust(60, " ")}|\n"
        f"{LINE_EQUAL} \n"
        f"> Lựa chọn của bạn: "
        ))
    except:
        print("Lỗi ! dữ liệu không khớp, chỉ được nhập số")
        continue 
    match choose:
        case 1:
            print()
            if(len(saving_accounts) == 0):
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else:
                print("+" + "".center(118, "-") + "+")
                print("|" + "DANH SÁCH SỔ TIẾT KIỆM".center(118, " ") + "|")
                print("+" + "".center(118, "-") + "+")
                print(f"| {"STT":<5} | {"MÃ SỐ":<10} | {"KHÁCH HÀNG":<30} | {"SỐ TIỀN GỬI":<20} | {"KỲ HẠN ":<11} | {"LÃI SUẤT":<10} | {"TRẠNG THÁI":<12} |")
                print("+" + "".center(118, "-") + "+")

                for index, value in enumerate(saving_accounts):
                    print(f"| {(index + 1):<5} | {value.get("account_id"):<10} | {value.get("customer_name"):<30} | {f"{value.get("balance"):,}đ":<20} | {f"{value.get("term_months")} tháng":<11} | {f"{value.get("interest_rate")}%/năm":<10} | {value.get("status"):<12} |")
                print("+" + "".center(118, "-") + "+")
            print()
        case 2:
            print()
            
            while True:
                account_code = input("Vui lòng nhập mã của sổ tiết kiệm: ").strip().upper()
                if(not account_code):
                    print("Lỗi ! mã tiết kiệm không được để trống !")
                    continue 
                break 
            index = next((i for i, value in enumerate(saving_accounts) if value["account_id"] == account_code), -1)
            if(index != -1 ):
                print("Mã này đã có trong danh sách !")
            else:
                while True:
                    account_name = input("Vui lòng nhập tên của khách hàng: ").strip().upper()
                    if(not account_code):
                        print("Lỗi ! tên khách hàng không được để trống !")
                        continue 
                    break 
                
                while True:
                    try:
                        deposit_amount = int(input("Vui lòng nhập số tiền gửi: "))    
                    except:
                        print("Lỗi Số tiền gửi không hợp lệ !")
                        continue 
                    if(deposit_amount <= 0):
                        print("Số tiền gửi không được để âm")
                        continue 
                    break 
                
                while True:
                    try:
                        deposit_term = int(input("Vui lòng nhập kỳ hạn gửi theo tháng: "))    
                    except:
                        print("Lỗi số kỳ hạn không hợp lệ !")
                        continue 
                    if(deposit_term <= 0):
                        print("Số kỳ hạn không được để âm")
                        continue 
                    break 
                while True:
                    try:
                        annual_interest_rate = float(input("Vui lòng nhập lãi suất năm: "))
                    except:
                        print("Lỗi ! Số lãi xuất không phù hợp !")
                        continue 
                    if(annual_interest_rate <= 0 ):
                        print("Lỗi ! Lãi suất năm không được để âm và bằng 0")
                        continue 
                    break 
                saving_accounts.append(
                    {
                        "account_id": account_code,
                        "customer_name": account_name,
                        "balance": deposit_amount,
                        "term_months": deposit_term,
                        "interest_rate": annual_interest_rate,
                        "status": "active"
                    }
                )
                print("Đã thêm sổ tiết kiệm mới !")
            print()
        case 3:
            while True:
                account_code = input("Vui lòng nhập mã của sổ tiết kiệm cần được cập nhật: ").strip().upper()
                if(not account_code):
                    print("Lỗi ! mã tiết kiệm không được để trống !")
                    continue 
                break 
            index = next((i for i, value in enumerate(saving_accounts) if value["account_id"] == account_code), -1)
            if(index == -1 ):
                print("Mã này chưa có trong danh sách !")
            else:
                while True:
                    account_name = input("Vui lòng nhập tên của khách hàng mới: ").strip().upper()
                    if(not account_code):
                        print("Lỗi ! tên khách hàng không được để trống !")
                        continue 
                    break 
                
                while True:
                    try:
                        deposit_amount = int(input("Vui lòng nhập số tiền gửi mới: "))    
                    except:
                        print("Lỗi Số tiền gửi không hợp lệ !")
                        continue 
                    if(deposit_amount <= 0):
                        print("Số tiền gửi không được để âm")
                        continue 
                    break 
                
                while True:
                    try:
                        deposit_term = int(input("Vui lòng nhập kỳ hạn gửi theo tháng MỚI: "))    
                    except:
                        print("Lỗi số kỳ hạn không hợp lệ !")
                        continue 
                    if(deposit_term <= 0):
                        print("Số kỳ hạn không được để âm")
                        continue 
                    break 
                while True:
                    try:
                        annual_interest_rate = float(input("Vui lòng nhập lãi suất năm MỚI: "))
                    except:
                        print("Lỗi ! Số lãi xuất không phù hợp !")
                        continue 
                    if(annual_interest_rate <= 0 ):
                        print("Lỗi ! Lãi suất năm không được để âm và bằng 0")
                        continue 
                    break 
                saving_accounts[index].update(
                    {
                        "account_id": account_code,
                        "customer_name": account_name,
                        "balance": deposit_amount,
                        "term_months": deposit_term,
                        "interest_rate": annual_interest_rate,
                        "status": "active"
                    }
                )
                print("Đã cập nhật thành công !")
            print()
        case 4:
            print()
            while True:
                account_code = input("Vui lòng nhập mã của sổ tiết kiệm cần được tất toán /xóa: ").strip().upper()
                if(not account_code):
                    print("Lỗi ! mã tiết kiệm không được để trống !")
                    continue 
                break 
            index = next((i for i, value in enumerate(saving_accounts) if value["account_id"] == account_code), -1)
            if(index == -1 ):
                print("Mã này chưa có trong danh sách !")
            else:
                saving_accounts[index]["status"] = "closed"
                print(f"Đã xóa số tài khoản {account_code} thành công !")
            print()
        case 5:
            print()
            while True:
                account_code = input("Vui lòng nhập mã của sổ tiết kiệm cần được tính lãi: ").strip().upper()
                if(not account_code):
                    print("Lỗi ! mã tiết kiệm không được để trống !")
                    continue 
                break 
            index = next((i for i, value in enumerate(saving_accounts) if value["account_id"] == account_code), -1)
            if(index == -1 ):
                print("Mã này chưa có trong danh sách !")
            else:
                if(saving_accounts[index]["status"] == "active"):
                    result = saving_accounts[index]["balance"] * (saving_accounts[index]["term_months"] / 12) *(saving_accounts[index]["interest_rate"] /100)
                    print(
                        f"Tiền lãi của bạn: {result:,}đ\n"
                        f"Tổng tiền nhận khi đến hạn: {(saving_accounts[index]["balance"] + result):,}đ"
                        )
                    print()
                else:
                    print("Tài khoản đã tất toán")
        case 6:
            print()
            while True:
                account_code = input("Vui lòng nhập mã của sổ tiết kiệm cần được kiểm tra: ").strip().upper()
                if(not account_code):
                    print("Lỗi ! mã tiết kiệm không được để trống !")
                    continue 
                break 
            index = next((i for i, value in enumerate(saving_accounts) if value["account_id"] == account_code), -1)
            if(index == -1 ):
                print("Mã này chưa có trong danh sách !")
            else:
                while True:
                    try:
                        month_send =int(input("Vui lòng nhập số tháng thực gửi: ")) 
                    except:
                        print("Số tháng không hợp lệ !")
                        continue 
                    if(month_send < 0):
                        print("Số tháng không được nhỏ hơn 0 !")
                        continue 
                    break 
                if(saving_accounts[index]["status"] != "active"): 
                    print("Tài khoản đã tất toán")
                else:
                    if(month_send < saving_accounts[index]["term_months"]):
                        result = saving_accounts[index]["balance"] * (month_send / 12) *(0.5/100)
                        print(
                            f"Tiền lãi của bạn: {result:,}đ\n"
                            f"Tổng tiền nhận khi đến hạn: {(saving_accounts[index]["balance"] + result):,}đ"
                            )
                    else:
                        result = saving_accounts[index]["balance"] * (month_send / 12) *(saving_accounts[index]["interest_rate"] /100)
                        print(
                            f"Tiền lãi của bạn: {result:,}đ\n"
                            f"Tổng tiền nhận khi đến hạn: {(saving_accounts[index]["balance"] + result):,}đ"
                            )
                        print()
        case 7:
            break 
        case _:
            print()
            print("Lỗi ! Chỉ được chọn từ 1 ->  5 !")
            print()
            
            
"""
INPUT
- Mã sổ tiết kiệm
- Tên khách hàng
- Số tiền gửi 
- Kỳ hạn gửi theo tháng 
- Lãi suất năm 
- Số tháng thực gửi 
OUTPUT
- Hiển thị danh sách sổ tiết kiệm
- Thông báo thêm / cập nhật / tất toán thành công
- Tiền lãi dự kiến
- Kiểm tra điều kiện rút trước hạn
- Thông báo lỗi nếu dữ liệu không hợp lệ
EDGE CASES
- Mã sổ bị trùng
- Tên khách hàng rỗng
- Số tiền gửi hoặc kỳ hạn không hợp lệ
- Lãi suất không hợp lệ
- Không tìm thấy mã sổ
- Không thao tác được với sổ đã tất toán
- Số tháng thực gửi không hợp lệ
- Menu nhập sai dữ liệu
"""
