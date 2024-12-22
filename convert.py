import os
from PIL import Image


def convert_jpg_to_jpeg():
    # 检查给定的文件夹路径是否存在
    if not os.path.exists(original_folder_path):
        print("指定的文件夹不存在")
        return

    # 获取文件夹中的所有文件
    files = os.listdir(original_folder_path)

    # 遍历文件夹中的文件
    for file in files:
        # 检查文件是否为JPG文件
        if file.lower().endswith('.jpg'):
            file_path = os.path.join(original_folder_path, file)
            # 打开JPG图像
            with Image.open(file_path) as img:
                # 构造新的JPEG文件名
                new_file = file.rsplit('.', 1)[0] + '.jpeg'
                new_file_path = os.path.join(target_folder_path, new_file)
                # 将图像保存为JPEG格式
                img.convert('RGB').save(new_file_path, 'JPEG')
            print(f'{file} 已转换为 {new_file}')


# 指定图片文件夹路径
original_folder_path = '/Users/zhangrui/Temp/convert/original'
target_folder_path = '/Users/zhangrui/Temp/convert/target'
convert_jpg_to_jpeg()
