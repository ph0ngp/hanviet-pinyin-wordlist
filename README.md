# Danh sách từ vựng Hán Việt Pinyin

## Giới Thiệu

Đây là danh sách từ vựng Hán Việt được phân loại theo pinyin.

Các từ điển Hán Việt khác thường chỉ có phiên âm Hán Việt ứng với từng chữ, mà đôi khi một chữ lại có nhiều cách đọc pinyin khác nhau, nên không phân biệt được âm Hán Việt nào tương ứng với âm pinyin nào. Danh sách từ Hán Việt này giải quyết vấn đề đó.

Ví dụ: `中` có 2 pinyin là `zhōng` và `zhòng`, thì `zhōng` ứng với âm Hán Việt là `trung` và `zhòng` ứng với âm Hán Việt là `trúng`.  Hoặc `降` có 2 pinyin là `jiàng` và `xiáng`, thì `jiàng` ứng với âm Hán Việt là `giáng` và `xiáng` ứng với âm Hán Việt là `hàng`.

Dữ liệu chỉ hỗ trợ các chữ Hán phồn thể, không hỗ trợ giản thể vì độ phân biệt của các chữ Hán phồn thể cao hơn giản thể (một chữ Hán giản thể có thể đại diện cho nhiều chữ Hán phồn thể khác nhau). Nếu muốn sử dụng cho giản thể có thể dùng các tool hoặc database khác để convert giữa giản thể - phồn thể.

## Cấu trúc danh sách:

Danh sách được viết dưới dạng file `.csv`, gồm 3 cột: `char`, `hanviet`, `pinyin`.

- `char`: chữ Hán phồn thể.
- `hanviet`: âm Hán Việt tương ứng với chữ đó và pinyin trong dòng đó.
- `pinyin`: âm pinyin của chữ Hán đó. Nếu cột này có giá trị `*` thì có nghĩa là chữ đó luôn chỉ phiên ra âm Hán Việt tương ứng ở cột `hanviet`.

## Đóng góp

Dữ liệu do cá nhân mình thu thập và phân loại dựa trên nhiều nguồn khác nhau, không tránh khỏi thiếu sót, rất mong các bạn đóng góp bằng cách mở issue hoặc pull request cho repo này.

## Tham khảo

Dữ liệu được xây dựng tham khảo dựa trên các nguồn từ điển sau:

- [Trang web Từ điển Hán Nôm](https://hvdic.thivien.net/)
- Hán Việt Từ Điển Trích Dẫn - Đặng Thế Kiệt
- Từ điển Hán Việt, Trần Văn Chánh, NXB Trẻ, TP Hồ Chí Minh, 1999.
- Hán Việt tân từ điển, Nguyễn Quốc Hùng, NXB Khai Trí, Sài Gòn, 1975.
- Hán Việt tự điển, Thiều Chửu, Hà Nội, 1942.

## API liên quan:
- npm package: https://github.com/ph0ngp/hanviet-pinyin-words

## License

Project này được phát hành dưới [MIT License](LICENSE)

Copyright (c) 2024 Phong Phan