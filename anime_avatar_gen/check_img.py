import os
from PIL import Image
# 读取所有文件
for file in os.listdir("data/faces"):
    filename = "data/faces/%s" % file
    try:
        Image.open(filename)
    except:
        os.remove(filename)
        print("%s错误" % filename)
    
print("mission completed!")