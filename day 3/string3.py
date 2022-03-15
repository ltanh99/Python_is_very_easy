normalStr = '  StrIng Is very NorMal'

print('normal string:', normalStr)

# ---------------------------------------------------------------------------------------------------
# Các phương thức biến đổi chuỗi
# ---------------------------------------------------------------------------------------------------

# capitalize: sử dụng để biến đổi chuỗi -> viết hoa chữ đầu + các chữ còn lại viết thường
# Nếu ký tự đầu tiên là khoảng trắng thì bỏ qua và viết thường hết chữ còn lại
print('String with capitalize: ', normalStr.capitalize()) 

# upper: sử dụng để viết hoa toàn bộ chuỗi
print('String with upper', normalStr.upper())

# lower: sử dụng để viết thường toàn bộ chuỗi
print('String with lower', normalStr.lower())

# swapcase: chuỗi: thường -> hoa, hoa -> thường
print('String with swapcase', normalStr.swapcase())

# title: viết hoa các chữ cái đầu của từng từ
print('String with title:', normalStr.title())

# ---------------------------------------------------------------------------------------------------
# Các phương thức định dạng
# ---------------------------------------------------------------------------------------------------

# center: căn giữa theo chiều rộng đã quy định <chuỗi>.center(width, [fillchar] -> k có thì mặc định là khoảng trắng)
print('String with center:', normalStr.center(30,'*'))

# rjust: căn phải
print('String with rjust:', normalStr.rjust(30, '*'))

# ljust: căn trái
print('String with ljust:', normalStr.ljust(30, '*'))

# ---------------------------------------------------------------------------------------------------
# Các phương thức xử lý
# ---------------------------------------------------------------------------------------------------

# encode & decode
print('String with encode', normalStr.encode())

# join: trả về chuỗi bằng cách nối các phần tử trong iterable bằng ký tự nối.

