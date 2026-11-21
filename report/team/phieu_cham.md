# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): ALOALO (L3A) · người ghi phiếu: Vai trò 4 — Người giữ hồ sơ (kiểm tra hồ sơ cùng cả nhóm)
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
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất **Go có điều kiện** khớp số liệu phạm vi `noi_dia + hang_nang` (`4.599 đ = 0,38×` đã cộng cố định, `0,49×` cả hệ thống, `simulated`). Nêu đủ cả 3 số bất lợi (xem lại 100% còn `0,98×`/`1,03×`, `power 0,64` nếu thật là 5 điểm, mở lại hiện tại `3,97%`) kèm 4 điều kiện có vai trò phụ trách và ngày kiểm tra (`2026-12-04`, `12-14`, `12-21`). Lưu ý nhỏ: mục 4 gắn `[simulated]` hơi dư cho 3 chỉ số không dùng cột `_simulated`. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi số từ cột `_simulated` trong `ho_so_launch_v0.md`, `bang_chi_phi.md`, `chi_so.md` E2 và `pilot_plan.yaml` đều có nhãn `simulated`; không dùng từ cấm theo quy tắc 5. Phạm vi thu hẹp còn `noi_dia + hang_nang` có lý do bằng số từ A3 (`quoc_te` `22.515 đ = 1,88×`, thành công `27,3%`, `ok` giảm `30,0% → 11,4% → 2,2%`; `doi_tac` `10.215 đ = 0,85×`, có điều khoản riêng). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn dấu `?`. Có đối chứng đồng thời `20 + 20` nhân viên, bốc thăm ngẫu nhiên (`seed 2026`, phân tầng theo depot), giảm spillover theo tài khoản và `staff_id`, tính đủ 5 câu D1 và ghi rõ đánh đổi MDE 6 điểm (`n_eff = 859`, `m ≥ 299`, `DE = 6,96`, `power ≈ 0,64` ở 5 điểm). Có 4 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`, có ngưỡng theo baseline `3,97%`, thời hạn và 1 vai trò có quyền dừng. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** **Go có điều kiện** (giữ một trong Go · Go có điều kiện · No-go)

**Lý do:** Hồ sơ của nhóm Buffet đầy đủ bằng chứng định lượng, đồng bộ giữa `lab13.py`, `bang_chi_phi.md`, `bang_loi.md` (có bản gốc độc lập 20/20 trong `nhan_doc_lap/`), `chi_so.md` (14 event có `trace_id`, định nghĩa rõ cohort 7 ngày) và `pilot_plan.yaml`. Nhóm không bỏ qua số bất lợi (xem lại 100% = `0,98–1,03×`, `power = 0,64` ở mức 5 điểm, mở lại `3,97%`) và đặt đủ điều kiện tiền kiểm (`2026-12-04`) trước khi chạy pilot.

**Một câu hỏi cho đội trình:** Luật dừng chi phí trong `pilot_plan.yaml` đặt ngưỡng `> 8.000 đ trong 2 tuần liên tiếp`, trong khi ở B4 của chính nhóm thì nếu phải xem lại 100% chi phí đã là `11.743 đ` (tới `12.415 đ` nếu làm lại 15,3 phút, `simulated`) và ngày kiểm tra kế hoạch giảm xem lại tận `2026-12-21` — vậy nếu 2 tuần đầu vẫn xem lại 100%, luật dừng chi phí này có kích hoạt thu hẹp ngay trước khi nhóm kịp hạ tỉ lệ xem lại không?

**Câu trả lời của đội trình:** *(Điền trực tiếp sau khi đội Buffet trả lời tại phiên duyệt chéo Gate 2a.)*
