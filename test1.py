import json
def process_logs(log_file, severity="ERROR", **filters):
    try:
        ip_set = set()
        with open(log_file, "r", encoding="utf-8") as file:
            for line in file:
                if severity in line:
                    thoaman = True
                    for key, value in filters.items():
                        dieukien = f"{key}={value}"
                        if dieukien not in line:
                            thoaman = False
                            break
                    if thoaman:
                        words = line.split()
                        for word in words:
                            if word.startswith("ip"):
                                ip = word.split("=")[1]
                                ip_set.add(ip)
        with open("alert_ips.json", "w", encoding="utf-8") as file:
            json.dump(list(ip_set), file, indent=4)         

    except FileNotFoundError:
        print("Lỗi không tìm thấy tệp");

# Gọi hàm lọc tất cả các dòng ERROR và có liên quan đến user "admin"
process_logs("server.txt", severity="ERROR", user="admin")