import subprocess

# 执行 shell 命令
command = "ls -l;pwd;du -sh *|sort -h"
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# 获取命令的返回值和输出
return_code = result.returncode
output = result.stdout

# 打印结果
print(f"Return Code: {return_code}")
print(f"Output:\n{output}")

'''
docker exec python380_c python3 demo/shell.py
'''