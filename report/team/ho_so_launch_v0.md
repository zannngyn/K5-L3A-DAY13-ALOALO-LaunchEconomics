# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: ALOALO · Lớp: L3A · Người giữ hồ sơ: Vai trò 4 · Dữ liệu: mẫu 1.200 yêu cầu, 1.624 lần chạy, toàn bộ là giả lập của lab

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** (`simulated`) = 4.373.585 đ ÷ 978 việc thành công, gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ). Giờ nhân viên chiếm 92,5% tổng chi phí (`simulated`) — [bang_chi_phi.md](bang_chi_phi.md) A2 | Giả lập | Vai trò 1 — Người viết code |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại ×2: **+51,8%** → 6.787 đ · 2. Tỉ lệ xem lại ×2: **+40,7%** → 6.292 đ · 3. Lương +25%: **+23,1%** → 5.506 đ (`simulated`); giá token ×2 chỉ +5,6% — B1, B2 | Giả lập | Vai trò 2 — Người kiểm số |
| 3 · So với nhân viên tự làm | Cả hệ thống **5.865 đ/yêu cầu = 0,49×** mức 12.000 đ (`simulated`). Theo loại: `noi_dia` 0,22×, `hang_nang` 0,69×, `doi_tac` 0,85×, **`quoc_te` 1,88×** (`simulated`) → phạm vi pilot thu hẹp còn `noi_dia` + `hang_nang`. Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống: 6.901.220 đ (`simulated`). **Bất lợi:** xem lại 100% tuần đầu → **11.743 đ = 0,98×**, tới **12.415 đ = 1,03×** nếu làm lại 15,30 phút như dữ liệu (`simulated`) — A3, B3, B4 | Giả lập | Vai trò 2 — Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử là: chính **82,83%** (994/1.200), dùng — bỏ qua gợi ý **27,12%** (48/177), an toàn — mở lại 7 ngày **4,25%** (51/1.200); trong phạm vi pilot: 92,26% · 21,09% · **3,97%**. Có 3 chỉ số tự đề xuất, 11 event có `trace_id`, đã kiểm tra chéo — [chi_so.md](chi_so.md) | Xong, có bằng chứng | Vai trò 4 — Người giữ hồ sơ |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận hai người gắn nhãn độc lập **18/20 = 90%**; không trùng ca 6, 8 (đã ghi quy tắc). Phân bố: người dùng 4 · hệ thống 5 · ngữ cảnh 4 · giới hạn 4 · ngầm 3. Bảng khắc phục 5 ca đủ năm loại; lỗi phải sửa trước pilot: ca 7 (báo đã hoàn khi sổ cái 503), ca 20 (hoàn trùng) — [bang_loi.md](bang_loi.md) | Xong, có bằng chứng | Vai trò 3 — Người gắn nhãn 1 |
| 6 · Pilot plan | Chia ngẫu nhiên theo `staff`, **20 nhân viên/nhóm**, đối chứng chạy đồng thời. Mục tiêu 5 điểm cần 1.251 yc/nhóm nhưng 20 cụm chỉ cho tối đa 1.000 → chấp nhận **MDE 6 điểm**, n_eff **859/nhóm**, **≥ 299 yc/nhân viên**, DE 6,96. **Bất lợi:** nếu tác động thật là 5 điểm, power chỉ **0,64**. Ba luật dừng (an toàn > 5% mở lại, chi phí > 12.000 đ, dùng < 80%) có ngưỡng, thời hạn, người có quyền dừng; ngày quyết định 2026-12-19 — [pilot_plan.yaml](pilot_plan.yaml) | Xong, có bằng chứng | Vai trò 3 — Người gắn nhãn 1 |
| 7 · Rủi ro kinh tế | Làm lại ×2 → 6.787 đ (+51,8%); xem lại 100% kéo dài → 0,98–1,03×; khối lượng còn một nửa → cố định +2.370 đ/việc, 5.784 đ = 0,48×; mở sang `quoc_te` → 1,88× (`simulated`). Mỗi dòng có dấu hiệu theo dõi và người phụ trách — [chi_so.md](chi_so.md) E2 | Giả lập | Vai trò 2 — Người kiểm số |

**Đề xuất: Go có điều kiện** — pilot chỉ cho `noi_dia` + `hang_nang` ở 6 depot đã chạy thử, chia theo nhân viên, MDE 6 điểm. Lý do: trong phạm vi này chi phí cả hệ thống 0,49× (`simulated`) và tỉ lệ mở lại 3,97% dưới ngưỡng an toàn 5%. Con số bất lợi đã nêu và cách xử lý: xem lại 100% làm mất tiết kiệm (0,98–1,03×, `simulated`) → phải có kế hoạch giảm xem lại; power 0,64 nếu tác động chỉ 5 điểm → cần chữ ký chấp nhận; ngưỡng an toàn chỉ dư 1,03 điểm so với hiện tại → giữ kiểm tra an toàn ở mọi lần xem giữa kỳ; `hang_nang` chỉ thành công 74,1%. Điều kiện:

- Sửa khoá chống trùng và chỉ báo "đã hoàn" khi `refund_ledger_write` trả ok (ca 7, 20); đối soát mỗi giờ, ngưỡng 0 ca — Vai trò 1 — Người viết code — kiểm tra 2026-11-27, trước ngày bắt đầu.
- Giám đốc vận hành ký chấp nhận MDE 6 điểm (power 0,64 nếu tác động thật 5 điểm) — Vai trò 4 — Người giữ hồ sơ trình ký — kiểm tra 2026-11-27.
- Bật đủ 11 event có `trace_id`; thay phút `simulated` bằng phút đo thật từ `staff_review_decision` và `staff_rework_completed` sau tuần 1 — Vai trò 2 — Người kiểm số — kiểm tra 2026-12-05.
- Có kế hoạch giảm xem lại theo bậc (100% → 50% → 20% khi tỉ lệ bỏ qua gợi ý < 15%), vì xem lại 100% thì không tiết kiệm (B4) — Vai trò 2 — Người kiểm số — kiểm tra 2026-12-12.
- Mỗi nhân viên nhóm can thiệp phải đạt ≥ 299 yêu cầu trong phạm vi trước ngày quyết định (ước tính ~30,7 yc/người/ngày → cần ≥ 10 ngày ở bước 0,50); nếu chưa đủ, lùi ngày quyết định thay vì kết luận sớm — Vai trò 3 — Người gắn nhãn 1 — kiểm tra 2026-12-12.

**Đề xuất cuối: Go có điều kiện** — pilot `noi_dia` + `hang_nang`, đủ 5 điều kiện trên trước ngày kiểm tra; điều kiện nào không đạt đúng hạn thì hồ sơ quay về No-go.
