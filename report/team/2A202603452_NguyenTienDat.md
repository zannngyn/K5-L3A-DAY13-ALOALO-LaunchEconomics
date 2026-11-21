# Báo cáo cá nhân — Nguyễn Tiến Đạt

## 1. Thông tin thành viên

- Họ tên: Nguyễn Tiến Đạt
- MSSV: 2A202603452
- Email: 26ai.datnt23@vinuni.edu.vn
- Vai trong nhóm: Vai trò 3 — Người gắn nhãn 1

## 2. Phần việc phụ trách

- Thực hiện nhiệm vụ C: đọc 20 ca lỗi, gắn nhãn độc lập lần 1 theo năm loại lỗi Google PAIR và chuẩn bị bảng khắc phục.
- Thực hiện nhiệm vụ D: hoàn thiện kế hoạch pilot trong `report/team/pilot_plan.yaml`.
- Theo dõi các điều kiện hoàn thành của CP3 và CP4, đồng thời chuẩn bị thông tin bàn giao cho Vai trò 4.

## 3. Đóng góp cụ thể

- Trích xuất đầy đủ 20 ca lỗi từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` vào `report/team/bang_loi.md`.
- Gắn nhãn độc lập Người gắn nhãn 1 cho 20 ca theo nguyên nhân gốc: Do người dùng, Hệ thống, Ngữ cảnh, Giới hạn hệ thống và Ngầm.
- Điền bảng khắc phục 5 ca, mỗi loại một ca; mỗi dòng có cách phát hiện đo được và vai trò phụ trách.
- Hoàn thiện D1: 1.251 yêu cầu/nhóm khi chia theo yêu cầu; 3.103 yêu cầu/nhóm khi chia theo nhân viên với m=75; phương án 20 nhân viên/nhóm có giới hạn hiệu dụng 1.000; 6 depot/nhóm có giới hạn 300; phương án chấp nhận mức chênh 6 điểm cần 859 yêu cầu hiệu dụng/nhóm và ít nhất 299 yêu cầu/nhân viên.
- Hoàn thiện D2, phạm vi `noi_dia + hang_nang`, chia ngẫu nhiên theo nhân viên, rollout, rollback, ngày quyết định và ba luật dừng về an toàn, chi phí và mức độ sử dụng.
- Ghi rõ các số liệu từ cột giả lập bằng nhãn `simulated` và không sử dụng từ bị cấm trong hồ sơ.

## 4. Bằng chứng

- File: `report/team/bang_loi.md` — mô tả 20 ca, bộ nhãn Người gắn nhãn 1 và bảng khắc phục 5 loại lỗi.
- File: `report/team/pilot_plan.yaml` — chú thích D1–D2, thiết kế pilot, trường nhận diện tác động và luật dừng.
- Kết quả chạy `src/lab13.py`: ba phép thử A1 đạt; D1 in các số 1.251, 3.103, 1.000, 300 và 859 như hồ sơ.
- Kết quả kiểm tra YAML bằng `yaml.safe_load`: `YAML OK`.
- Commit bằng chứng: `34cdf52` — cập nhật `report/team/bang_loi.md` và `report/team/pilot_plan.yaml`.

Lưu ý: bộ nhãn Người gắn nhãn 2, tỷ lệ đồng thuận và nhãn thống nhất phải do Thành viên C thực hiện độc lập trước khi điền vào báo cáo nhóm.

## 5. Công cụ AI đã dùng

- Codex/ChatGPT: hỗ trợ đọc hướng dẫn, trích xuất nội dung DOCX, lập bảng nhãn lần 1, soạn cấu trúc `pilot_plan.yaml` và rà soát placeholder.
- Tự kiểm tra bằng cách đối chiếu với `CHECKPOINTS.md`, `RULES.md`, `RUBRIC.md`, đề bài DOCX và các số được in từ `src/lab13.py`.
- Không dùng AI để tạo bộ nhãn Người gắn nhãn 2 hoặc tuyên bố đồng thuận; phần đó được giữ cho Thành viên C thực hiện độc lập.

## 6. Tự đánh giá

- Đã hoàn thành các đầu việc thuộc Vai trò 3 và để lại bằng chứng trong hai file báo cáo nhóm.
- Điểm cần bàn giao: Thành viên C phải tự gắn nhãn lần 2, so nhãn và tính tỷ lệ đồng thuận trước khi nộp.
- Cần thống nhất cách trình bày giữa `mde: 0.05` và phương án chấp nhận mức chênh 6 điểm (`n_per_arm: 859`) trong bản hồ sơ cuối.
