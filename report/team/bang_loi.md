# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

## Trích xuất 20 ca lỗi từ đề bài

| Ca | Mô tả |
| --: | --- |
| 1 | Khách nhập số tài khoản nhận hoàn thiếu hai chữ số; trợ lý tạo lệnh hoàn và ngân hàng trả lỗi. |
| 2 | Kiện nội địa 28 kg; trợ lý tra bảng giá hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ; khách mở lại sau 2 ngày. |
| 3 | Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút; khách chờ tiền về tài khoản ngân hàng và báo chưa được hoàn. |
| 4 | Khách yêu cầu hoàn phí cho chặng do hãng nước ngoài giao; LogiX không có dữ liệu chặng này; trợ lý không xác định được trạng thái và chuyển nhân viên. |
| 5 | Kiểm tra cuối tuần phát hiện 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ mỗi đơn; không khách nào báo và không có cảnh báo. |
| 6 | Khách chọn “Hoàn phí giao trễ” nhưng mô tả hàng bị vỡ; trợ lý xử lý theo luồng giao trễ và từ chối vì đơn giao đúng hạn. |
| 7 | API sổ cái trả lỗi 503 khi ghi hoàn tiền; trợ lý thử lại 3 lần rồi vẫn báo khách đã hoàn tiền thành công. |
| 8 | Trợ lý dẫn “Điều 7.2 chính sách hoàn phí” làm căn cứ, nhưng chính sách hiện hành không có điều 7.2; số tiền hoàn vẫn đúng. |
| 9 | Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn; trợ lý báo mã không hợp lệ rồi dừng, không gợi ý gì. |
| 10 | Đơn giao trễ do bão; trợ lý từ chối hoàn theo điều khoản bất khả kháng, đúng chính sách, nhưng khách thấy vô lý vì ứng dụng vẫn hiện cam kết giao 24 giờ. |
| 11 | Khách gửi tin nhắn thoại 40 giây; trợ lý không xử lý được âm thanh và yêu cầu nhập bằng chữ. |
| 12 | Tool tra đơn depot D05 thiếu một trường; trợ lý vẫn ra kết quả đúng sau nhiều lần gọi, khiến chi phí token D05 gấp 3 lần depot khác trong 3 tuần mà không ai phát hiện. |
| 13 | Khách hỏi hoàn phí bảo hiểm hàng hóa của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý; trợ lý trả lời chung chung về phí vận chuyển, không nói rõ giới hạn xử lý. |
| 14 | Khách bấm nhầm “Xác nhận đã nhận tiền” khi chưa nhận; yêu cầu bị đóng. |
| 15 | Đơn trễ 26 giờ; chính sách trễ 24–48 giờ hoàn 50%, nhưng trợ lý tính hoàn 100%; nhân viên xem lại bắt được trước khi gửi. |
| 16 | Theo thiết kế “gửi ngay khi xong”, trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng; khách phản ánh bị làm phiền. |
| 17 | Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg; lệch 1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày không ai mở lại. |
| 18 | Trợ lý tính đúng phí giao 30.000 đ và hoàn 50%, nhưng tin nhắn chỉ ghi “Đã hoàn 15.000 đ”, không kèm cách tính; khách cho là hoàn thiếu và mở lại yêu cầu. |
| 19 | Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước; trợ lý chỉ truy cập được dữ liệu 12 tháng, nói rõ không tra được và chuyển nhân viên kèm tóm tắt. |
| 20 | Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi; trợ lý hoàn hai lần cho cùng một đơn vì lệnh thứ hai không có khóa chống trùng. |

Người gắn nhãn 1: Vai trò 3 (bộ nhãn độc lập do Vai trò 3 thực hiện) · Người gắn nhãn 2: Thành viên C — Vai trò 4 (gắn độc lập cả 20 ca từ mô tả trong đề bài, ghi chốt trước khi mở cột nhãn 1; không sửa cột nhãn 1)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Ngữ cảnh | Do người dùng | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Ngầm | Hệ thống | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** **18/20 = 90%** (≥ 80%, không cần viết lại định nghĩa). Hai ca không trùng: ca 6 và ca 8.

Phân bố nhãn thống nhất: Do người dùng 4 (1, 6, 9, 14) · Hệ thống 5 (2, 7, 8, 15, 20) · Ngữ cảnh 4 (3, 10, 16, 18) · Giới hạn hệ thống 4 (4, 11, 13, 19) · Ngầm 3 (5, 12, 17).

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

| Ca | Nhãn 1 | Nhãn 2 | Nhãn thống nhất | Quy tắc phân biệt (một câu) |
| --: | --- | --- | --- | --- |
| 6 | Ngữ cảnh | Do người dùng | **Do người dùng** | Nếu đầu vào khách chọn/nhập (mục "Hoàn phí giao trễ") mâu thuẫn với nội dung thật (hàng vỡ) thì gốc lỗi là người dùng; việc trợ lý không đối chiếu mô tả là việc cải thiện, ghi ở cột khắc phục chứ không đổi nhãn. |
| 8 | Ngầm | Hệ thống | **Hệ thống** | Chỉ gắn Ngầm khi không ai nhận ra cho tới lúc kiểm tra mẫu; trích dẫn "Điều 7.2" hiện ngay trong tin nhắn và trái chính sách hiện hành nên là lỗi Hệ thống đã lộ ra, dù số tiền vẫn đúng. |

Các ca dễ lẫn khác đã trùng nhãn, giữ quy tắc chung: ca 13 ngoài phạm vi là Giới hạn hệ thống kể cả khi trợ lý xử lý giới hạn kém; ca 15 nhân viên bắt được nên là Hệ thống, không phải Ngầm; ca 12 sai về chi phí, không ai thấy suốt 3 tuần nên là Ngầm.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | `input_validation_failed` theo từng yêu cầu; cảnh báo ngay khi thiếu 2 chữ số | Bắt buộc xác nhận/kiểm tra checksum trước khi tạo lệnh hoàn; chuyển nhân viên nếu vẫn không hợp lệ | Vai trò 1 — viết code |
| 7 | Hệ thống | `refund_write_failed` hoặc HTTP 503; cảnh báo tức thời và rà soát 100% lỗi ghi | Không thông báo thành công nếu chưa có xác nhận ghi; retry có backoff và chuyển nhân viên sau 3 lần | Vai trò 1 — viết code |
| 10 | Ngữ cảnh | So khớp `delivery_promise`, thời tiết và lý do từ chối; kiểm tra mẫu hàng ngày | Hiển thị điều khoản bất khả kháng cùng cam kết giao hàng và cho phép nhân viên xem lại ca tranh chấp | Vai trò 4 — giữ hồ sơ |
| 11 | Giới hạn hệ thống | `input_modality=audio` và tỉ lệ chuyển nhân viên; báo cáo hàng ngày | Nói rõ chưa hỗ trợ âm thanh, cung cấp đường dẫn nhập văn bản hoặc chuyển nhân viên | Vai trò 2 — kiểm số |
| 17 | Ngầm | Đối soát giá áp dụng với bảng giá hiệu lực; cảnh báo khi lệch >0 trong 1 ngày | Bắt buộc kiểm tra phiên bản bảng giá trước khi tính và bù/hoàn các ca bị ảnh hưởng | Vai trò 3 — gắn nhãn 1 |
