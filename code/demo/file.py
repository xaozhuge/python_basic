
file_path = 'demo/remark'

# 读取文件的所有内容
try:
    with open(file_path, 'r') as file:
        file_contents = file.read()
        print(file_contents)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")


# 按行读取
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            print(line.strip())  # strip() 方法用于去除行尾的换行符

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

'''
docker exec python380_c python3 demo/file.py
'''
