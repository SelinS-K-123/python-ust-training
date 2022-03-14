import subprocess
res=subprocess.run(['cat','Selin.txt'],stderr=subprocess.PIPE,text=True)
print(res.stderr)