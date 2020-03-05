#!/usr/bin/python3
import sys
import os


def createPlaylist(filepath:str):
	try:
		for root1, dirs1, files1 in os.walk(filepath): #遍历整个母文件夹
			for dir1 in dirs1: #各个歌单
				filename = os.path.join(root1, dir1) + ".M3U8"
				with open(filename, 'w', encoding='utf-8') as playlistfile:
					playlistfile.write("#EXTM3U\n")
					for root2, dirs2, files2 in os.walk(os.path.join(root1, dir1)): #各个歌单
						for file2 in files2: #各首歌
							temppath = os.path.join(root2, file2)
							temppath = temppath[(len(filepath)+1) : len(temppath)]  # 去头
							playlistfile.write("#EXTINF:,\n")
							playlistfile.write(temppath)
							playlistfile.write('\n')
	except Exception as e:
		print("Create playlist error.")
	else:
		print("Created lastest playlist, enjoy it.")


def main():
	try:
		filepath = str(sys.argv[1])
	except IndexError as e:
		print('Usage: \npython3 ' + os.path.basename(__file__) + ' [music dir]')
		return
	print('The path should be like \'D:\MUSIC\'')
	print('Your input music path is ' + filepath)
	check = input('Create? [Y/n] ').lower()
	if 'n' == check or 'no' == check:
		return
	createPlaylist(filepath)


if __name__ == '__main__':
	main()
