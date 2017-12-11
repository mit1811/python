import glob
path='C:\Users\Mit\PycharmProjects\untitled\wx_data*.txt'
file=glob.glob(path)
for files in file:
    f=open(files,'r')
    f.readlines()
    f.close()
