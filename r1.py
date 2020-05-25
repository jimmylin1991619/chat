# 讀取檔案
def read_file(filename):	
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: #-sig是可以去除怪符號的編碼
		for line in f:
			lines.append(line.strip())
	return lines		

# 轉換語句
def convert(lines):
	news = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue

		if person:
			news.append(person + ': ' + line)

	print(news)
	return news

# 寫入檔案
def write_file(newfilename, news):
	with open(newfilename, 'w', encoding = 'utf-8') as f:
		for new in news:
			f.write(new + '\n')

 # 執行主程式

def main():	
	filename = 'input.txt'
	newfilename = 'output.txt'
	import os
	if os.path.isfile(filename):
		lines = read_file(filename)
		news = convert(lines)
		write_file(newfilename, news)
	else:
		print('找不到檔案!')

	
main()






