# 讀取檔案
def read_file(filename):	
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: #-sig是可以去除怪符號的編碼
		for line in f:
			lines.append(line.strip())
	return lines		


# 轉換語句
def convert(lines):
	person = None
	allen_word_count = 0
	viki_wor_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for msg in s[2:]:
					allen_word_count += len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:	
				for msg in s[2:]:
					viki_wor_count += len(msg)
	print('allen說了', allen_word_count, '個字') 
	print('傳了', allen_sticker_count, '個貼圖')
	print('傳了', allen_image_count, '個圖片' )

	print('viki說了', viki_wor_count, '個字')
	print('傳了', viki_sticker_count, '個貼圖')
	print('傳了', viki_image_count, '個圖片' )



# 寫入檔案
def write_file(newfilename, news):
	with open(newfilename, 'w', encoding = 'utf-8') as f:
		for new in news:
			f.write(new + '\n')


 # 執行主程式
def main():	
	filename = 'LINE-Viki.txt'
	# newfilename = 'output.txt'
	import os
	if os.path.isfile(filename):
		lines = read_file(filename)
		news = convert(lines)
		# write_file(newfilename, news)
	else:
		print('找不到檔案!')

	
main()


















