''''import os,shutil

source_path="D:/Test"
dest_path="D:/Rehoboth"

for i in os.listdir(source_path):
    curr_path=source_path+'/'+i
    for j in os.listdir(curr_path):
        ext=os.path.splitext(j)[1]
        if ext=='.MP4':
          copying=shutil.copyfile(curr_path,dest_path)
    print("Copying Done:" +curr_path+j)'''
