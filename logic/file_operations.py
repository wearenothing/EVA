# 文件：logic/file_operations.py

def open_file(filepath):
    """打开文件，读取内容"""
    with open(filepath, 'r') as file:
        data = file.read()
    return data

def save_file(filepath, data):
    """保存数据到文件"""
    with open(filepath, 'w') as file:
        file.write(data)
