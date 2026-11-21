# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (ĐẠT) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (ĐẠT) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (ĐẠT) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | tổng 4 khoản trên | simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 | `4.373.585 / 978` | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | `(245.585 + 84.000) / 1.200` | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Gấp **16,3 lần** (`4.472 / 274,7`, `simulated`). Nếu tính cả 222 ca không thành công để nhân viên tự làm (`12.000 đ/ca`), chi phí cả hệ thống là **5.865 đ/yêu cầu = 0,49×** mức `12.000 đ` (`simulated`).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại** chiếm lớn nhất với **51,8%** (`2.264.000 / 4.373.585`, `simulated`), tiếp theo là **xem lại 40,7%** (`simulated`); tổng giờ nhân viên chiếm **92,5%** (`simulated`).

*(Kiểm số thủ công — Vai trò 2: `890 phút × 2.000 = 1.780.000 đ`; `1.132 phút × 2.000 = 2.264.000 đ`; `5.600 tool × 15 = 84.000 đ`; `(245.585 + 84.000 + 1.780.000 + 2.264.000) / 978 = 4.472,0 đ`.)*

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (`simulated`) | 0,22× (`simulated`) |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (`simulated`) | 0,69× (`simulated`) |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (`simulated`) | 1,88× (`simulated`) |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (`simulated`) | 0,85× (`simulated`) |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **`quoc_te`** không đáng xử lý vì tốn **22.515 đ/việc thành công = 1,88×** mức `12.000 đ` (`simulated`), tỉ lệ thành công chỉ **27,3%**. Chạy lại tới 3 lần **không giúp**: tỉ lệ `ok` giảm từ **30,0%** (lần 1) xuống **11,4%** (lần 2) và **2,2%** (lần 3). (`doi_tac` sát ngưỡng `0,85×` nên cũng nên loại khỏi pilot).

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (`simulated`) | 0,38× (`simulated`) |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ (`simulated`) | 0,48× (`simulated`) |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Ở quy mô đầy đủ (**45.000 yc/tháng**) hay giảm một nửa (**22.500 yc/tháng**), tổng chi phí vẫn là **4.599 đ (0,38×)** và **5.784 đ (0,48×)** (`simulated`), chưa đổi kết luận rẻ hơn `12.000 đ`. Tuy nhiên, nếu khối lượng pilot nhỏ (cố định tăng mạnh lên trên `8.586 đ/việc`), chi phí cố định sẽ làm mất lợi thế kinh tế.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (`simulated`) | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ** (`simulated`, **+46,3%**), đúng bằng tổng hai tác động riêng (`+5,6% + 40,7% = +46,3%`) do mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Số ca làm lại** (±51,8% / −25,9%) · 2. **Tỉ lệ xem lại** (+40,7% / −20,3%) · 3. **Lương nhân viên** (+23,1%).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (`simulated`) | Số yêu cầu không thành công | Chi phí cả hệ thống (`simulated`) | Chi phí mỗi việc thành công (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? Giới hạn **2 lần** rẻ nhất cho cả hệ thống (**6.901.220 đ**, `simulated`), **không trùng** với giới hạn có chi phí mỗi việc thành công thấp nhất là **1 lần** (**4.111 đ**, `simulated`) vì chạy 1 lần đẩy thêm **85 ca** sang nhân viên làm tay (`319 − 234`).

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: Với giả định 9 phút/ca làm lại, chi phí là **11.743 đ = 0,98×** mức `12.000 đ` (`simulated`, hoà vốn nếu xem lại ≤ **5,12 phút**); nếu dùng trung bình thực tế `15,30 phút/ca` (`phut_lam_lai_simulated`), chi phí lên tới **12.415 đ = 1,03×** (`simulated`, đắt hơn nhân viên tự làm, hoà vốn ≤ **4,80 phút**).
- Kết quả này nói gì về thứ pilot cần học được? Nếu giữ xem lại 100% thì gần như không tiết kiệm được chi phí; pilot cần đo xem **có thể giảm tỉ lệ xem lại xuống mức an toàn nào** và **mỗi lần xem lại có rút ngắn dưới 4,8–5,1 phút** được không.
