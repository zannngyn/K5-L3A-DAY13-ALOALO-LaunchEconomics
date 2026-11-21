# Team

## Thông tin nhóm

- Tên nhóm: ALOALO
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-ALOALO-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/zannngyn/K5-L3A-DAY13-ALOALO-LaunchEconomics · nhánh `main` · commit chốt: commit cuối trên `main` trước deadline

## Thành viên

Nhóm 3 thành viên chia 4 vai trò (Nguyễn Thế Văn kiêm Vai trò 1 và Vai trò 2).

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Thế Văn | 2A202603474 | zannngyn@gmail.com | zannngyn | Vai trò 1 — Người viết code |
|   2 | Nguyễn Thế Văn | 2A202603474 | zannngyn@gmail.com | zannngyn | Vai trò 2 — Người kiểm số |
|   3 | Nguyễn Tiến Đạt | 2A202603452 | 26ai.datnt23@vinuni.edu.vn | dat73qb | Vai trò 3 — Người gắn nhãn 1 |
|   4 | Trần Văn Tài | 2A202603506 | 26ai.taitv2@vinuni.edu.vn | iat-123 | Vai trò 4 — Người gắn nhãn 2 kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

## Cá nhân

Mỗi thành viên tạo một báo cáo riêng `report/team/MSSV_HoTen.md`:

- `report/team/2A202603474_NguyenTheVan.md`
- `report/team/2A202603452_NguyenTienDat.md`
- `report/team/2A202603506_TranVanTai.md`

## Vai trò 1 — Người viết code (Nguyễn Thế Văn)

### Phần việc phụ trách

- Nhiệm vụ A, B, D1 trong `src/lab13.py`; khởi tạo và cấu hình repo nhóm `K5-L3A-DAY13-ALOALO-LaunchEconomics`.

### Đóng góp cụ thể

- Viết ba hàm A1 (in ĐẠT 1,20 · 1,25 · 1,25), hàm `mo_hinh`, tách theo loại (A3), chi phí cố định (A4), độ nhạy B1–B4 và phần in D1.

### Bằng chứng

- Commit `2a346e4` (`src/lab13.py`, `report/team/bang_chi_phi.md`).

## Vai trò 2 — Người kiểm số (Nguyễn Thế Văn)

### Phần việc phụ trách

- Kiểm tay số A2 và điền `report/team/bang_chi_phi.md`.

### Đóng góp cụ thể

- Kiểm tay: `890 phút × 2.000 = 1.780.000 đ`; `1.132 phút × 2.000 = 2.264.000 đ`; `5.600 tool × 15 = 84.000 đ`; `4.373.585 / 978 = 4.472 đ` (`simulated`).
- Điền đủ bảng A1, A2, A3, A4, B1, B2, B3, B4 kèm nhãn `simulated` và câu trả lời ≤ 3 dòng có số.

### Bằng chứng

- Commit `2a346e4` (`report/team/bang_chi_phi.md`, mục "Kiểm số thủ công — Vai trò 2").

## Vai trò 3 — Người gắn nhãn 1 (Nguyễn Tiến Đạt)

### Phần việc phụ trách

- Nhiệm vụ C (bộ nhãn 1, bảng khắc phục 5 ca) và nhiệm vụ D (`report/team/pilot_plan.yaml`).

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca; bảng khắc phục đủ năm loại.
- Chọn chia theo nhân viên, 20 nhân viên/nhóm, MDE 6 điểm, n_eff 859/nhóm, ≥ 299 yc/nhân viên, DE 6,96; tính tỉ lệ mở lại 4,25% / 3,97%; ba luật dừng.

### Bằng chứng

- Commit `34cdf52` (`report/team/bang_loi.md`, `report/team/pilot_plan.yaml`).

## Vai trò 4 — Người gắn nhãn 2 kiêm giữ hồ sơ (Trần Văn Tài)

### Phần việc phụ trách

- Bộ nhãn 2 và so nhãn (nhiệm vụ C); nhiệm vụ E (`chi_so.md`, `ho_so_launch_v0.md`); duyệt chéo Gate 2a; `TEAM.md`, `group_report.md`, `phieu_cham.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca trước khi mở bộ nhãn 1; đồng thuận 18/20 = 90%; ghi quy tắc cho ca 6, 8 và thống nhất nhãn.
- Tính thử ba chỉ số trên 1.200 yêu cầu (82,83% · 27,12% · 4,25%) và trong phạm vi pilot (92,26% · 21,09% · 3,97%); đề xuất 3 chỉ số mới; 11 event có `trace_id`; kiểm tra chéo; 6 dòng rủi ro kinh tế.
- Hồ sơ launch v0 bảy mục, đề xuất Go có điều kiện kèm số bất lợi.
- Duyệt chéo nội bộ: phát hiện `mde: 0.05` trong `pilot_plan.yaml` không khớp `n_per_arm: 859` (ứng với 6 điểm) → sửa thành `0.06`; nêu rủi ro thiếu mẫu cho nhân viên vào ở bước rollout 0,50.

### Bằng chứng

- Commit `96eb682` (`report/team/bang_loi.md`, `chi_so.md`, `ho_so_launch_v0.md`, `group_report.md`, `phieu_cham.md`, `TEAM.md`).
