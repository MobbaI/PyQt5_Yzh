import re
import openpyxl
from openpyxl.styles import Alignment

# pattern = '.*?你好啊.*?'
# str_1 = 'sdasda哈哈哈你好啊lkjskda'
# str_2 = 'sdasda你好是的dasd'
# result = re.match(pattern, str_1)
# result2 = re.match(pattern, str_2)
# if result:
#     print(1)
# else:
#     print(0)
# if result2:
#     print(1)
# else:
#     print(0)

ws = openpyxl.load_workbook('C:/Users/Administrator/Desktop/11/test.xlsx')
wb = ws['测试记录']
a = wb['U136'].value
print(a == 'U')
center = Alignment(horizontal='center', vertical='center')
wb['V136'].value = '√'
wb['V136'].alignment = center
print(wb['V136'].value == wb['T136'].value)

# pattern = '.*?运行\(P.*?'
# result = re.match(pattern, a)
# if result:
#     print('存在')
# else:
#     print('None')
# wb['AQ137'].value = '你好啊！'
ws.save('C:/Users/Administrator/Desktop/11/test.xlsx')