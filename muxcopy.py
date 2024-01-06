import os
import shutil

def find_files_with_h(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".m4s") and "h" in file:
                print(os.path.join(root, file))
            else:
                print("不符合命名条件，跳过！")
                
root_directory = "./"

find_files_with_h(root_directory +'Cache/')

cache_directory = os.path.join(root_directory +'Cache/')
output_file = os.path.join(root_directory + 'muxvideo_hls')

# 获取Cache目录下所有以.m4s结尾的文件
m4s_files = [f for f in os.listdir(cache_directory) if f.endswith(".m4s")]

# 根据文件名进行排序
m4s_files.sort()

# 合并文件
with open(output_file, 'wb') as outfile:
    for m4s_file in m4s_files:
        file_path = os.path.join(cache_directory, m4s_file)
        with open(file_path, 'rb') as infile:
            outfile.write(infile.read())

# 将合并后的文件拷贝到根目录
output_path = os.path.join(root_directory, f"{os.path.basename(output_file)}.mp4corrupted")
os.rename(output_file, output_path)

print("视频文件合完成并已拷贝到根目录。")

folder_path = "./Cache"  # 删除文件夹路径，清理Cache下载

shutil.rmtree(folder_path)