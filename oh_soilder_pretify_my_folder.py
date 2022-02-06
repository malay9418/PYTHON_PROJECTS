import os
out_put_files = []
def soilder(path, file, format):
	global out_put_files
	os.chdir(path)
	files = [ file for file in os.listdir() if not file.endswith(format)]
	with open(file, "a+") as f: #opened in "a+" mode if file dosen't exist then create it
		ignore_words = f.read()
		if ignore_words == "":
			out_put_files = files.copy()
		else:
			ignores = ignore_words.split("\n")
			for file in files:
				for word in ignores:
					if word not in file:
						out_put_files.append(file)
				
					
						
soilder("/storage/emulated/0/DCIM/", "/storage/emulated/0/DCIM/PYTHON/ignore.txt", ".mp4")
print(out_put_files)