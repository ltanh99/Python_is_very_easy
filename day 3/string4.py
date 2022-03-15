from email.policy import default


defaultString = 'Learn Python. Improve myself.'

# ---------------------------------------------------------------------------------------------------
# Các phương thức tách chuỗi
# ---------------------------------------------------------------------------------------------------

# split
# <chuỗi>.split(sep=None, maxsplit=-1)
print('split #1:', defaultString.split())
print('split #2:', defaultString.split(maxsplit=2)) # số lần phân tách lớn nhất là 2

# rsplit
# <chuỗi>.rsplit(sep=None, maxsplit=-1)
# cũng là tách chuỗi nhưng tách từ phải -> trái
print('right split #1:', defaultString.rsplit(maxsplit=1))

# splitline: tách chuỗi theo \n
print('split lines:', 'a\nb\nc\nd\ne'.splitlines())
print('split lines:', '''
a
v
cá
df
ádf
'''.splitlines())
print('split lines with keepends=true:', 'a\nb\nc\nd\ne'.splitlines(True)) # nếu set keepends là true thì sẽ giữ lại các ký tự \n

# partition
# <chuỗi>.partition(sep)
# trả về tuple 3 phần: trước chuỗi sep, chuỗi sep, sau chuỗi sep
print('split #1:', defaultString.partition('Py'))
print('split #1:', defaultString.partition('Pyádfasdf')) # trường hợp tìm k thấy chuỗi sep

# EXERCISE

s = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
a = s.lower().replace('aaaaaaa', '').replace('aooaa', '').title()
print(a)


