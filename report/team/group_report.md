# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính. Mọi số chi phí tính từ cột `_simulated` mang nhãn `simulated`.

## 1. Thông tin nhóm

- Tên nhóm: ALOALO
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Trả lời bốn câu cho trợ lý hoàn phí LogiX-VN từ mẫu 1.200 yêu cầu / 1.624 lần chạy (dữ liệu giả lập): có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot phải thiết kế thế nào. Cách làm: tính chi phí mỗi việc thành công từ trace (tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `thanh_cong`), tìm yếu tố nhạy nhất, phân loại lỗi theo Google PAIR, rồi thiết kế pilot có đối chứng đủ cỡ mẫu và gom thành hồ sơ Gate 2a.

## 3. Giải pháp

- **A — Mô hình chi phí** ([bang_chi_phi.md](bang_chi_phi.md), `src/lab13.py`): ba phép thử A1 ĐẠT (1,20 · 1,25 · 1,25); A2 từ trace; A3 tách theo `loai`; A4 cộng chi phí cố định 40 triệu đ/tháng.
- **B — Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): 9 kịch bản B1, cặp B2 (cộng tuyến tính), giới hạn chạy lại B3, xem lại 100% B4.
- **C — Bảng lỗi** ([bang_loi.md](bang_loi.md)): hai người gắn nhãn độc lập, so nhãn, quy tắc cho ca không trùng, bảng khắc phục 5 ca đủ năm loại.
- **D — Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): so cỡ mẫu ba cách chia, chọn chia theo nhân viên, ba luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ.
- **E — Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): ba chỉ số tính thử, ba chỉ số tự đề xuất, 11 event có `trace_id`, kiểm tra chéo, 6 dòng rủi ro kinh tế, hồ sơ bảy mục.

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** (`simulated`), gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu; cả hệ thống **5.865 đ/yêu cầu = 0,49×** mức 12.000 đ (`simulated`).
- `quoc_te` 22.515 đ = 1,88× (`simulated`), chạy lại không giúp (ok 30,0% → 11,4% → 2,2%) → phạm vi pilot `noi_dia` + `hang_nang`.
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%) (`simulated`). Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống: 6.901.220 đ (`simulated`).
- Bảng lỗi: đồng thuận **18/20 = 90%**.
- Chỉ số trong đợt chạy thử là: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25% (phạm vi pilot: 3,97%).
- Pilot: chia theo nhân viên, 20/nhóm, MDE 6 điểm, n_eff 859/nhóm, ≥ 299 yc/nhân viên, DE 6,96; power 0,64 nếu tác động thật 5 điểm.
- **Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, 5 điều kiện có người phụ trách và ngày kiểm tra (xem hồ sơ).
- **Duyệt chéo nội bộ trước Gate 2a** (Vai trò 4): (1) `mde: 0.05` trong `pilot_plan.yaml` mâu thuẫn với `n_per_arm: 859` và mục `predeclared` (6 điểm) → đã sửa `mde: 0.06`; (2) với rollout theo tuần 0,10 → 0,25 → 0,50 và ~30,7 yc trong phạm vi/người/ngày, nhân viên vào ở bước 0,50 cần ≥ 10 ngày mới đủ 299 yc → thêm điều kiện lùi ngày quyết định nếu thiếu mẫu; (3) ngưỡng an toàn 5% không làm pilot dừng ngay tuần đầu vì tỉ lệ hiện tại trong phạm vi là 3,97%.
- **Kết quả duyệt chéo nhóm nhận được từ hội đồng:**

## 5. Khó khăn và cách xử lý

- `python lab13.py` trên Windows báo `UnicodeEncodeError` (console cp1252 không in được tiếng Việt). Cách xử lý: chạy `PYTHONIOENCODING=utf-8 python lab13.py` (PowerShell: `$env:PYTHONIOENCODING='utf-8'`); code không cần sửa.
- Máy của Vai trò 4 thiếu `statsmodels` → phần D1 dừng ở `ModuleNotFoundError`. Cách xử lý: tạo venv và `pip install -r src/requirements.txt`; sau đó D1 in đúng 1.251 · DE 2,48 · 1.000 · 300 · 859 / 299 / DE 6,96 · power 0,64 và tỉ lệ mở lại 4,25% / 3,97%.
- Lệnh kiểm tra `python -c "import yaml; yaml.safe_load(open('report/team/pilot_plan.yaml'))"` lỗi `UnicodeDecodeError` trên Windows vì `open()` mặc định đọc cp1252; file là UTF-8 hợp lệ. Cách xử lý: chạy với `PYTHONUTF8=1` (PowerShell: `$env:PYTHONUTF8='1'`) hoặc `open(..., encoding='utf-8')` → đọc được, không lỗi; trên Linux/macOS lệnh gốc chạy bình thường.
- Giữ tính độc lập ở nhiệm vụ C: người gắn nhãn 2 ghi chốt bộ nhãn trước khi mở cột nhãn 1; không sửa cột nhãn 1 sau khi so.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Toàn bộ phút xem lại / làm lại là `simulated`; B4 cho thấy kết luận rẻ hơn nhân viên phụ thuộc mạnh vào số phút này (0,98–1,03× khi xem lại 100%) → pilot phải đo phút thật sau tuần 1.
- Đợt chạy thử không có đối chứng, nên chưa nói được trợ lý nâng chỉ số chính; chỉ nói "chỉ số trong đợt chạy thử là 82,83%".
- 20 cụm/nhóm không đủ cho mục tiêu 5 điểm (giới hạn 1.000 < 1.251); chấp nhận MDE 6 điểm với power 0,64 ở mức 5 điểm.
- Lỗi ngầm (ca 5, 12, 17) không hiện trong `mo_lai_trong_7_ngay` → cần event `audit_sample_checked` hằng tuần.

## 8. Tài liệu tham khảo

- Đề bài Lab 13 (`docs/Ngay13_Lab13_De_bai_hoc_vien.docx`), Hướng dẫn chi tiết buổi chiều (`docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`), dữ liệu và công thức (`docs/du_lieu_va_cong_thuc.md`).
- Google PAIR, People + AI Guidebook — chương Errors + Graceful Failure (năm loại lỗi).
