# Báo cáo cá nhân — Nguyễn Thế Văn - 2A202603474

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thế Văn
- MSSV: 2A202603474
- Email: zannngyn@gmail.com
- Vai trong nhóm: Vai trò 1 (Người viết code) kiêm Vai trò 2 (Người kiểm số)

## 2. Phần việc phụ trách

- Khởi tạo repo nhóm `K5-L3A-DAY13-ALOALO-LaunchEconomics` trên GitHub và cấu hình môi trường chạy `src/.venv`.
- Hoàn thiện phần code A1–A4, B1–B4 và phần tính cỡ mẫu D1 trong `src/lab13.py`.
- Tính tay đối chiếu số liệu và điền trọn vẹn bảng chi phí / độ nhạy (nhiệm vụ A và B) trong `report/team/bang_chi_phi.md`.
- Rà soát kiểm tra kỹ thuật cuối buổi trước khi chốt bài nộp của nhóm.

## 3. Đóng góp cụ thể

- Viết 3 hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) và qua cả 3 phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`).
- Viết hàm `mo_hinh(...)` tính chi phí từ trace (`logix_runs.csv` và `logix_requests.csv` đọc với `keep_default_na=False`):
  - Chi phí mỗi việc thành công: **4.472 đ** (`simulated`, gấp 16,3 lần hoá đơn 274,7 đ/yêu cầu); chi phí cả hệ thống: **5.865 đ/yêu cầu = 0,49×** mức 12.000 đ (`simulated`).
  - Phân tách theo loại (A3) và cộng chi phí cố định 40 triệu đ/tháng (A4) để chốt phạm vi pilot là `noi_dia` + `hang_nang` (loại `quoc_te` 1,88× và `doi_tac` 0,85×).
  - Chạy 9 kịch bản độ nhạy B1, cặp cộng tuyến tính B2, chi phí cả hệ thống B3 (giới hạn 2 lần chạy rẻ nhất: 6.901.220 đ, `simulated`) và kịch bản xem lại 100% B4 (11.743 đ = 0,98× với 9 phút/ca làm lại; 12.415 đ = 1,03× với trung bình thực tế 15,30 phút/ca, `simulated`).
  - Viết phần D1 trong `src/lab13.py` tính cỡ mẫu 5 câu (1.251; DE 2,48; 1.000; 300; 859/nhóm với m ≥ 299 và power 0,64 ở mức 5 điểm) và tỉ lệ `mo_lai_trong_7_ngay` hiện tại (4,25% toàn mẫu; 3,97% trong phạm vi).
- Kiểm tay đối chiếu số liệu A2 (`890 × 2.000 = 1.780.000 đ`; `1.132 × 2.000 = 2.264.000 đ`; `5.600 × 15 = 84.000 đ`; `4.373.585 / 978 = 4.472 đ`) và điền `report/team/bang_chi_phi.md`.

## 4. Bằng chứng

- Commit `2a346e4`: cập nhật `src/lab13.py` và `report/team/bang_chi_phi.md`.
- File `TEAM.md` (cập nhật thông tin thành viên và bằng chứng).
- Kết quả chạy `cd src && ./.venv/bin/python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` và đầy đủ bảng A2–D1.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI Antigravity (Gemini) hỗ trợ phân chia công việc theo cấu trúc lab, gợi ý cài đặt code `src/lab13.py`, trình bày `report/team/bang_chi_phi.md` và rà soát checklist nộp bài.
- **Cách tự kiểm tra:**
  - Chạy trực tiếp `src/lab13.py` kiểm tra 3 phép thử A1 đạt 100% (`1,20 · 1,25 · 1,25`).
  - Tính tay lại các khoản chi phí A2 (số phút xem lại/làm lại × 2.000 đ, số lần gọi tool × 15 đ, chia cho 978 việc thành công) và đối chiếu sai số ≤ 2% với các công thức trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
  - Chạy `yaml.safe_load`, `grep` kiểm tra không còn dấu `?` ngoài chú thích trong `report/team/pilot_plan.yaml` và không có từ cấm trong `report/team/`.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ các phần việc của Vai trò 1 và Vai trò 2, giúp thành viên phụ trách Vai trò 3 và Vai trò 4 có đầy đủ số liệu để hoàn thiện `pilot_plan.yaml`, `chi_so.md` và `ho_so_launch_v0.md` đúng hạn trước phiên duyệt chéo Gate 2a.
