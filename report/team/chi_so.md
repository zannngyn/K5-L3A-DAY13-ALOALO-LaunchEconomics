# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Người điền: Vai trò 4 — Người gắn nhãn 2 kiêm giữ hồ sơ. Ba chỉ số chính/dùng/an toàn tính từ các cột `dong_trong_24h`, `mo_lai_trong_7_ngay`, `duoc_xem_lai`, `quyet_dinh_xem_lai` của `src/logix_requests.csv` (không phải cột `_simulated`, nên không mang nhãn `simulated`). Mọi số chi phí ở mục E2 lấy từ `bang_chi_phi.md` và là `simulated`.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu | Trong phạm vi pilot `noi_dia` + `hang_nang` (982 yc) |
| --- | --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200) | 92,26% (906/982) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177: 41 `sua` + 7 `bo`) | 21,09% (27/128) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200) | 3,97% (39/982) |
| Dùng (tự đề xuất) | Tỉ lệ dùng trợ lý ở nhóm can thiệp | Số yêu cầu đủ điều kiện ở nhóm can thiệp có `agent_suggestion_shown` và nhân viên ra `staff_review_decision` hoặc gửi gợi ý, chia số `refund_request_created` đủ điều kiện có `arm = can_thiep`; ngưỡng luật dừng: < 80% trong 1 tuần | Không cần tính (đợt chạy thử không có cột `arm`) | — |
| An toàn (tự đề xuất) | % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 12, 17) | Số đơn trong `audit_sample_checked` có `so_tien_da_hoan ≠ so_tien_dung`, chia số đơn được kiểm (100 đơn/tuần); ngưỡng cảnh báo 1% | Không cần tính | — |
| An toàn (tự đề xuất) | Số lệnh hoàn lệch sổ cái (ca 7, 20) | Số `refund_notification_sent` báo "đã hoàn" không có `refund_ledger_write` `ket_qua = ok` cùng `trace_id`, cộng số `idempotency_key` bị ghi sổ quá 1 lần; ngưỡng 0 ca, đối soát mỗi giờ | Không cần tính | — |

Viết "chỉ số trong đợt chạy thử là 82,83%", không viết "trợ lý đã nâng chỉ số từ 0,70": đợt chạy thử không có nhóm đối chứng, nên chưa tách được tác động của trợ lý.

## Danh sách event

Mỗi event có `trace_id` để nối với trace của agent và `request_id` để nối về yêu cầu. Lưu ý từ dữ liệu: trong `logix_runs.csv` mỗi lần chạy có một `trace_id` riêng (1.624 `trace_id` cho 1.624 lần chạy, 1.200 `request_id`), nên event cấp yêu cầu ghi `trace_id` của lần chạy cuối và luôn kèm `request_id`.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, depot, staff_id, arm, created_at, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status (ok/loi), trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | request_id, staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện cho nhân viên |
| `staff_review_decision` | Nhân viên | request_id, staff_id, quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id | Khi bấm gửi/sửa/bỏ |
| `staff_rework_completed` | Nhân viên | request_id, phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| `handoff_to_staff` | Agent | request_id, reason (thieu_du_lieu / ngoai_pham_vi / het_3_lan), tom_tat, trace_id | Khi chuyển nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | request_id, idempotency_key, so_tien, ket_qua (ok/loi, mã HTTP), trace_id | Khi ghi sổ hoàn tiền |
| `refund_notification_sent` | Agent | request_id, kenh, noi_dung, so_tien, cach_tinh, gio_gui, trace_id | Khi gửi tin "đã hoàn" cho khách |
| `ticket_closed` | Hệ thống ticket | request_id, closed_at, ket_qua, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | request_id, reopened_at, reason, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | request_id, so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, 100 đơn |

## Kiểm tra chéo chỉ số với event

| Chỉ số | Event dùng để tính | Đo được? | Đối chiếu với dữ liệu chạy thử |
| --- | --- | --- | --- |
| Chính: đóng ≤ 24 giờ, không mở lại 7 ngày | `refund_request_created.created_at`, `ticket_closed.closed_at` (≤ 24 giờ), không có `ticket_reopened` trong 7 ngày sau `closed_at` | Có | 994 yêu cầu thỏa cả hai cột trong 1.200 |
| Dùng: tỉ lệ bỏ qua gợi ý | `staff_review_decision.quyet_dinh` ∈ {sua, bo} ÷ số `staff_review_decision` | Có | 177 yêu cầu có `duoc_xem_lai = 1` = 177 event xem lại; 48 `sua` + `bo` |
| An toàn: lỗi lọt đến khách | Số `request_id` có `ticket_reopened` trong 7 ngày ÷ số `refund_request_created` | Có | 51/1.200 |
| Dùng (đề xuất): tỉ lệ dùng trợ lý | `agent_suggestion_shown`, `staff_review_decision` ÷ `refund_request_created` có `arm = can_thiep` | Có, khi pilot ghi `arm` | Chưa có cột `arm` trong dữ liệu chạy thử → luật dừng mức độ sử dụng chỉ đo được sau khi bật event |
| An toàn (đề xuất): sai tiền qua kiểm tra mẫu | `audit_sample_checked` | Có, khi kế toán ghi event hằng tuần | Lỗi ngầm ca 5, 17 không hiện ở `mo_lai_trong_7_ngay` → cần event riêng |
| An toàn (đề xuất): lệch sổ cái | `refund_notification_sent` đối với `refund_ledger_write` cùng `trace_id`; đếm trùng `idempotency_key` | Có | Ca 7, 20 trong bảng lỗi |
| Chi phí mỗi việc thành công (luật dừng chi phí) | `agent_run_completed` (token, tool), `staff_review_decision.phut_xem_lai`, `staff_rework_completed.phut_lam_lai`, `ticket_closed.ket_qua = thanh_cong` | Có | Tổng `so_lan_chay` = 1.624 = số dòng `agent_run_completed`; tử số tính mọi lần chạy kể cả `loi` |

Không có chỉ số nào trong bảng E1 phải dựa vào dữ liệu ngoài danh sách event. Hai chỉ số đề xuất và luật dừng mức độ sử dụng **chưa đo được trên dữ liệu chạy thử**; chỉ đo được khi pilot bật đủ event có `trace_id`.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy B1, B3, B4 và A3, A4 trong `bang_chi_phi.md`. Mọi số chi phí là `simulated`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, chi phí mỗi việc thành công 4.472 → 6.787 đ (`simulated`); yếu tố nhạy nhất | Tỉ lệ `staff_rework_completed` ÷ yêu cầu theo tuần > 7% (đợt chạy thử: 4,89% trong phạm vi, 48/982) | Thu hẹp về `noi_dia`, rà 20 trace làm lại gần nhất theo `trace_id` | Vai trò 1 — Người viết code (chủ agent) |
| Phải xem lại 100% kéo dài sau tuần 1 | 11.743 đ = 0,98× mức 12.000 đ với làm lại 9 phút; 12.415 đ = 1,03× với 15,30 phút như dữ liệu (`simulated`); hoà vốn khi xem lại ≤ 4,80–5,12 phút | % yêu cầu có `staff_review_decision` còn > 50% ở cuối bước rollout 0,25; `phut_xem_lai` đo thật trung bình > 5 phút | Giảm xem lại theo bậc (100% → 50% → 20%) khi tỉ lệ bỏ qua gợi ý < 15% | Vai trò 2 — Người kiểm số |
| Tỉ lệ xem lại gấp đôi (không phải 100%) | +40,7%, lên 6.292 đ (`simulated`) | Tỉ lệ `duoc_xem_lai` theo tuần > 26% (đợt chạy thử: 13,03% trong phạm vi, 128/982) | Rà nguyên nhân bắt xem lại theo loại; không mở rộng bước rollout | Vai trò 2 — Người kiểm số |
| Lương nhân viên tăng 25% | +23,1%, lên 5.506 đ (`simulated`) | Đơn giá phút nhân viên > 2.000 đ trong bảng lương quý | Cập nhật tham số `mo_hinh`, tính lại B4 trước ngày quyết định | Vai trò 2 — Người kiểm số |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yc/tháng (4.599 đ = 0,38×), +2.370 đ/việc nếu còn một nửa (5.784 đ = 0,48×) (`simulated`) | Số `ticket_closed` thành công theo tuần < 50% kế hoạch | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | Vai trò 4 — Người giữ hồ sơ |
| Mở rộng phạm vi sang `quoc_te` / `doi_tac` | `quoc_te` 22.515 đ = 1,88×; `doi_tac` 10.215 đ = 0,85× (`simulated`); chạy lại không giúp `quoc_te` (ok 30,0% → 11,4% → 2,2%) | Có `refund_request_created` loại `quoc_te`/`doi_tac` đi vào luồng trợ lý | Chặn ở bước định tuyến, chuyển thẳng nhân viên | Vai trò 1 — Người viết code (chủ agent) |
