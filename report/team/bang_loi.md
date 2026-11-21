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

Người gắn nhãn 1: Vai trò 3 (bộ nhãn độc lập do Vai trò 3 thực hiện) · Người gắn nhãn 2: Thành viên C/Vai trò 4 (chưa điền — cần gắn độc lập trước khi so)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | — | Chưa so | — |
| 2 | Hệ thống | — | Chưa so | — |
| 3 | Ngữ cảnh | — | Chưa so | — |
| 4 | Giới hạn hệ thống | — | Chưa so | — |
| 5 | Ngầm | — | Chưa so | — |
| 6 | Ngữ cảnh | — | Chưa so | — |
| 7 | Hệ thống | — | Chưa so | — |
| 8 | Ngầm | — | Chưa so | — |
| 9 | Do người dùng | — | Chưa so | — |
| 10 | Ngữ cảnh | — | Chưa so | — |
| 11 | Giới hạn hệ thống | — | Chưa so | — |
| 12 | Ngầm | — | Chưa so | — |
| 13 | Giới hạn hệ thống | — | Chưa so | — |
| 14 | Do người dùng | — | Chưa so | — |
| 15 | Hệ thống | — | Chưa so | — |
| 16 | Ngữ cảnh | — | Chưa so | — |
| 17 | Ngầm | — | Chưa so | — |
| 18 | Ngữ cảnh | — | Chưa so | — |
| 19 | Giới hạn hệ thống | — | Chưa so | — |
| 20 | Hệ thống | — | Chưa so | — |

**Tỉ lệ đồng thuận:** Chưa tính — cần bộ nhãn độc lập của Người gắn nhãn 2; không được suy diễn đồng thuận từ một bộ nhãn.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Chưa so nhãn; sau khi hai người hoàn tất độc lập, mỗi ca không trùng phải ghi một câu quy tắc phân biệt trước khi thống nhất nhãn.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | `input_validation_failed` theo từng yêu cầu; cảnh báo ngay khi thiếu 2 chữ số | Bắt buộc xác nhận/kiểm tra checksum trước khi tạo lệnh hoàn; chuyển nhân viên nếu vẫn không hợp lệ | Vai trò 1 — viết code |
| 7 | Hệ thống | `refund_write_failed` hoặc HTTP 503; cảnh báo tức thời và rà soát 100% lỗi ghi | Không thông báo thành công nếu chưa có xác nhận ghi; retry có backoff và chuyển nhân viên sau 3 lần | Vai trò 1 — viết code |
| 10 | Ngữ cảnh | So khớp `delivery_promise`, thời tiết và lý do từ chối; kiểm tra mẫu hàng ngày | Hiển thị điều khoản bất khả kháng cùng cam kết giao hàng và cho phép nhân viên xem lại ca tranh chấp | Vai trò 4 — giữ hồ sơ |
| 11 | Giới hạn hệ thống | `input_modality=audio` và tỉ lệ chuyển nhân viên; báo cáo hàng ngày | Nói rõ chưa hỗ trợ âm thanh, cung cấp đường dẫn nhập văn bản hoặc chuyển nhân viên | Vai trò 2 — kiểm số |
| 17 | Ngầm | Đối soát giá áp dụng với bảng giá hiệu lực; cảnh báo khi lệch >0 trong 1 ngày | Bắt buộc kiểm tra phiên bản bảng giá trước khi tính và bù/hoàn các ca bị ảnh hưởng | Vai trò 3 — gắn nhãn 1 |
