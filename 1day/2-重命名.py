import os
dir_name = input("请输入文件夹名字")

files = os.listdir(dir_name)

os.chdir(dir_name)#改变到3文件目录
print(os.getcwd())
for file in files:
    position = file.rfind(".")
    new_name = file[:position]+"-pya"+file[position:]
    #old_name = dir_name+"/"+file
    #new_name = dir_name+"/"+new_name
    #os.rename(old_name,new_name)
    os.rename(file,new_name)
