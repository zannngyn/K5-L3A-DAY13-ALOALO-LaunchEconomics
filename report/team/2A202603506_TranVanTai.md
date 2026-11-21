# Báo cáo cá nhân — Trần Văn Tài - 2A202603506

## 1. Thông tin thành viên

- Họ tên: Trần Văn Tài
- MSSV: 2A202603506
- Email: 26ai.taitv2@vinuni.edu.vn
- Vai trong nhóm: Vai trò 4 — Người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Nhiệm vụ C: gắn nhãn độc lập lần 2 cho 20 ca lỗi theo năm loại Google PAIR, so nhãn với Người gắn nhãn 1, tính tỉ lệ đồng thuận và ghi quy tắc cho ca không trùng.
- Nhiệm vụ E: đặc tả và tính thử chỉ số, danh sách event, rủi ro kinh tế (`report/team/chi_so.md`); giữ và hoàn thiện hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`).
- Duyệt chéo nội bộ trước Gate 2a: đối chiếu `pilot_plan.yaml` với số in từ `src/lab13.py`.
- Tổng hợp tài liệu nhóm: `TEAM.md`, `report/team/group_report.md`, `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

- **Gắn nhãn 2 (C):** gắn đủ 20 ca từ mô tả trong đề bài và ghi chốt bộ nhãn trước khi mở cột nhãn 1; không sửa cột nhãn 1 sau khi so.
  - Đồng thuận **18/20 = 90%** (≥ 80%, không cần viết lại định nghĩa). Hai ca không trùng là ca 6 và ca 8 → ghi quy tắc phân biệt một câu cho mỗi ca và nhãn thống nhất.
  - Ghi thêm quy tắc chung cho các ca dễ lẫn đã trùng: ca 13 (ngoài phạm vi → Giới hạn hệ thống), ca 15 (nhân viên bắt được → Hệ thống, không phải Ngầm), ca 12 (sai chi phí 3 tuần không ai thấy → Ngầm).
  - Phân bố nhãn thống nhất: người dùng 4 · hệ thống 5 · ngữ cảnh 4 · giới hạn 4 · ngầm 3.
- **Chỉ số (E1):** tính thử ba chỉ số trên 1.200 yêu cầu:
  - Chỉ số chính **82,83%** (994/1.200); bỏ qua gợi ý **27,12%** (48/177); mở lại trong 7 ngày **4,25%** (51/1.200).
  - Trong phạm vi pilot `noi_dia` + `hang_nang`: 92,26% · 21,09% · **3,97%**.
  - Đề xuất 3 chỉ số mới, 11 event có `trace_id`, kiểm tra chéo giữa chỉ số và event.
- **Rủi ro kinh tế (E2):** 6 dòng rủi ro, mỗi dòng có số, dấu hiệu theo dõi và người phụ trách, ví dụ làm lại ×2 → 6.787 đ (+51,8%), xem lại 100% → 0,98–1,03×, mở sang `quoc_te` → 1,88× (`simulated`).
- **Hồ sơ launch v0:** điền đủ bảy mục với trạng thái và người phụ trách là một vai trò cụ thể; đề xuất cuối **Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, nêu rõ số bất lợi (0,98–1,03× khi xem lại 100%, power 0,64 nếu tác động thật 5 điểm, ngưỡng an toàn chỉ dư 1,03 điểm) và 5 điều kiện có người phụ trách, ngày kiểm tra.
- **Duyệt chéo nội bộ:**
  1. Phát hiện `mde: 0.05` trong `pilot_plan.yaml` mâu thuẫn với `n_per_arm: 859` và mục `predeclared` (ứng với 6 điểm) → sửa thành `mde: 0.06`.
  2. Với rollout 0,10 → 0,25 → 0,50 và ~30,7 yc/người/ngày, nhân viên vào ở bước 0,50 cần ≥ 10 ngày mới đủ 299 yc → thêm điều kiện lùi ngày quyết định nếu thiếu mẫu.
  3. Ghi chú ngưỡng an toàn 5% không làm pilot dừng ngay tuần đầu vì tỉ lệ hiện tại trong phạm vi là 3,97%.
- Cài `statsmodels` qua `pip install -r src/requirements.txt` để chạy lại D1 trên máy mình và đối chiếu số 1.251 · DE 2,48 · 1.000 · 300 · 859 / 299 / DE 6,96 · power 0,64.

## 4. Bằng chứng

- Commit `96eb682` (`feat(role-4): labeler 2, metrics, launch dossier and Gate 2a review`):
  - `report/team/bang_loi.md` — cột nhãn 2, tỉ lệ đồng thuận 18/20, bảng quy tắc ca 6 và ca 8, nhãn thống nhất.
  - `report/team/chi_so.md` — ba chỉ số tính thử, 3 chỉ số đề xuất, 11 event, kiểm tra chéo, 6 dòng rủi ro.
  - `report/team/ho_so_launch_v0.md` — hồ sơ bảy mục và đề xuất cuối.
  - `report/team/pilot_plan.yaml` — sửa `mde: 0.05` → `0.06`.
  - `TEAM.md`, `report/team/group_report.md`, `report/team/phieu_cham.md`.
- Kết quả chạy `src/lab13.py` (với `PYTHONIOENCODING=utf-8`) in đúng các số D1 và tỉ lệ mở lại 4,25% / 3,97% đã dẫn trong hồ sơ.
- Kiểm tra `yaml.safe_load` trên `pilot_plan.yaml` (với `PYTHONUTF8=1` trên Windows): đọc được, không lỗi.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (Claude).
- **Dùng vào việc:** giải thích cách tính cỡ mẫu hiệu dụng khi chia theo cụm, rà soát độ khớp giữa `pilot_plan.yaml`, `chi_so.md` và hồ sơ, gợi ý cách trình bày bảng và câu chữ trong hồ sơ, soát từ bị cấm và nhãn `simulated`.
- **Không dùng AI để:** tạo bộ nhãn 2 hay tỉ lệ đồng thuận; bộ nhãn 2 được chốt trước khi mở cột nhãn 1.
- **Cách tự kiểm tra:**
  - Mọi con số trong `chi_so.md` và hồ sơ đều đối chiếu với output của `src/lab13.py` hoặc tính tay từ CSV (ví dụ 994/1.200 = 82,83%; 48/177 = 27,12%; 51/1.200 = 4,25%).
  - Tự đếm lại 18/20 ca trùng nhãn giữa hai cột trong `bang_loi.md`.
  - Kiểm tra lại logic MDE: 859/nhóm ứng với 6 điểm chứ không phải 5 điểm → phát hiện và sửa `mde`.
  - `grep` trong `report/team/` để chắc không có từ bị cấm theo `RULES.md` và không còn dấu `?` ngoài chú thích trong YAML.

## 6. Tự đánh giá

- Hoàn thành đủ phần việc của Vai trò 4: bộ nhãn 2 độc lập, đồng thuận 90%, chỉ số và rủi ro kinh tế, hồ sơ launch bảy mục với đề xuất có điều kiện và số bất lợi.
- Điểm làm tốt: duyệt chéo nội bộ bắt được lỗi không khớp `mde` và rủi ro thiếu mẫu ở bước rollout 0,50 trước khi lên Gate 2a.
- Điểm cần cải thiện: phút xem lại / làm lại vẫn là `simulated`, nên kết luận "rẻ hơn nhân viên" còn phụ thuộc số đo thật sau tuần 1; mục "Kết quả duyệt chéo nhóm nhận được từ hội đồng" trong `group_report.md` cần bổ sung sau phiên Gate 2a.
