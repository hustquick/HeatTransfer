import os

folder = 'Examples'
files = os.listdir('../' + folder)
files.sort()
os.chdir(f'../{folder}')
for file in files:
    if file.endswith(".pdf"):
        continue
    os.system(r'python3 ' + file)
    print(f'--------{file}--------')
os.chdir('../test')
print('-------------------运行完毕-------------------')
