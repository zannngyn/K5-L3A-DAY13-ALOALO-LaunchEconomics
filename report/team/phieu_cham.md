# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): ALOALO (L3A) · người ghi phiếu: Vai trò 4 — Người giữ hồ sơ (cả nhóm cùng rà soát)
- Nhóm được chấm: Buffet (L3A) · Repo: `https://github.com/tiennguyen-ctrl/K5-L3A-DAY13-Buffet-LaunchEconomics`

## Danh sách kiểm tra bằng chứng (dùng khi đọc hồ sơ nhóm bạn)

| Tiêu chí | Kiểm tra gì | Đối chiếu số |
| --- | --- | --- |
| Đề xuất khớp bằng chứng | Đề xuất là một trong Go / Go có điều kiện / No-go; có nêu số bất lợi B4 (xem lại 100%) và power khi tác động thật là 5 điểm; mỗi điều kiện có người phụ trách và ngày kiểm tra | B4: 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút) (`simulated`); power ≈ 0,64 với MDE 6 điểm |
| Số giả lập và phạm vi | Mọi số từ cột `_simulated` có nhãn; phạm vi đã thu hẹp và lý do bằng số A3 | `quoc_te`: 22.515 đ = 1,88×; `doi_tac`: 10.215 đ = 0,85× (`simulated`) |
| Pilot ra được quyết định | Có đối chứng đồng thời, chia ngẫu nhiên; ≥ 20 cụm/nhóm hoặc ghi rõ đánh đổi; luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ, có ngưỡng, thời hạn, người có quyền dừng; ngưỡng an toàn đặt sau khi tính tỉ lệ hiện tại | Chia theo yêu cầu 1.251/nhóm; 20 nhân viên → tối đa 1.000; 6 depot → tối đa 300; mở lại hiện tại 4,25% (3,97% trong phạm vi) |

## Phiếu điểm

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất **Go có điều kiện** nhất quán với lợi thế chi phí ở phạm vi `noi_dia + hang_nang` (`4.599 đ = 0,38×` đã cộng cố định, `5.865 đ = 0,49×` cả hệ thống, `simulated`). Nhóm nhìn thẳng cả 3 điểm bất lợi — xem lại 100% chỉ còn `0,98–1,03×`, `power ≈ 0,64` nếu tác động thật chỉ 5 điểm, và tỉ lệ mở lại sẵn có `3,97%` — đồng thời gắn kèm 4 điều kiện xử lý có vai trò phụ trách và hạn kiểm tra (`2026-12-04`, `12-14`, `12-21`). *(Lưu ý nhỏ: mục 4 gắn `[simulated]` hơi dư cho 3 chỉ số không dùng cột `_simulated`.)* |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Toàn bộ số tính từ cột `_simulated` trong `ho_so_launch_v0.md`, `bang_chi_phi.md`, `chi_so.md` (E2) và `pilot_plan.yaml` đều được gắn nhãn `simulated` đầy đủ; tuân thủ đúng quy tắc không dùng từ cấm. Phạm vi pilot được thu hẹp có cơ sở định lượng từ A3: loại `quoc_te` (`22.515 đ = 1,88×`, thành công `27,3%`, chạy lại tụt từ `30,0% → 11,4% → 2,2%`) và tạm loại `doi_tac` (`10.215 đ = 0,85×`, có điều khoản riêng). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | `pilot_plan.yaml` hợp lệ qua `yaml.safe_load` và sạch dấu `?`. Thiết kế tách được tác động nhờ đối chứng đồng thời `20 + 20` nhân viên, phân bổ ngẫu nhiên có phân tầng theo depot (`seed 2026`), kiểm soát spillover qua tài khoản và log `staff_id`. Nhóm tính đủ 5 bài toán D1, chấp nhận MDE `6 điểm` (`n_eff = 859`, `m ≥ 299`, `DE = 6,96`, nêu rõ `power ≈ 0,64` ở mức 5 điểm), và chốt 4 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ` có ngưỡng neo theo baseline `3,97%`, thời hạn rõ ràng và 1 vai trò chịu trách nhiệm. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** **Go có điều kiện**

**Lý do:** Hồ sơ của nhóm Buffet có độ tin cậy cao nhờ sự khớp nối chặt chẽ từ `lab13.py` đến `bang_chi_phi.md`, `bang_loi.md` (lưu giữ nguyên bản 2 bộ nhãn độc lập 20/20 trong `nhan_doc_lap/`), `chi_so.md` (đặc tả 14 event có `trace_id`, tách rõ cohort đủ 7 ngày theo dõi) và `pilot_plan.yaml`. Thay vì né tránh rủi ro, nhóm nêu thẳng các điểm bất lợi về chi phí xem lại, `power` và nền mở lại `3,97%`, đồng thời đặt các điều kiện tiền kiểm (`2026-12-04`) làm chốt chặn trước khi bật pilot.

**Một câu hỏi cho đội trình:** Trong `pilot_plan.yaml`, luật dừng chi phí quy định thu hẹp phạm vi nếu chi phí vượt `8.000 đ` trong 2 tuần liên tiếp; trong khi theo B4, xem lại 100% đẩy chi phí lên `11.743–12.415 đ` (`simulated`), còn hạn kiểm tra kế hoạch giảm xem lại lại đặt tới `2026-12-21` (hơn 2 tuần sau mốc `2026-12-04`). Vậy trong 2 tuần đầu làm quen, luật dừng chi phí này có kích hoạt thu hẹp ngay trước khi nhóm kịp hạ tỉ lệ xem lại không?

**Câu trả lời của đội trình:** Đội Buffet thống nhất với phản biện của hội đồng và chốt phương án xử lý theo hai ý:
- **1. Giữ luật dừng `> 8.000 đ` làm chốt chặn kinh tế:** Theo tính toán B4, nếu chế độ xem lại 100% kéo dài hết 2 tuần đầu, chi phí sẽ vọt lên **11.743–12.415 đ/việc** (`0,98–1,03×`, `simulated`) — gần như không còn lợi thế so với nhân viên tự làm (`12.000 đ`). Khi đó, việc luật dừng kích hoạt thu hẹp về `noi_dia` (**2.696 đ**, `simulated`) và giới hạn 2 lần chạy là cơ chế tự vệ đúng đắn để cắt phần chi phí cao từ `hang_nang` (**8.221 đ**, `simulated`).
- **2. Chỉnh lại tiến độ kiểm soát xem lại để không kích hoạt oan ở giai đoạn làm quen:** Mốc kiểm tra kế hoạch giảm xem lại đặt ở `2026-12-21` (trễ hơn 2 tuần so với `2026-12-04`) tạo độ trễ khiến pilot dễ chạm ngưỡng `8.000 đ` trước khi kịp hạ tỉ lệ xem lại. Nhóm khắc phục bằng cách **phê duyệt sẵn lộ trình giảm xem lại theo bậc trước ngày mở pilot `2026-12-04`** (chỉ hạ khi `sửa + bỏ < 15%`, giữ thời lượng xem lại `≤ 4,8–5,1 phút` theo mức hoà vốn B4) và **bắt đầu nới giảm ngay từ tuần 2 (`2026-12-14`)**, song song với việc thay số phút `simulated` bằng thời gian đo thật từ event.
