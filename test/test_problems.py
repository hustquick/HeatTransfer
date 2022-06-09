import os

folder = 'Problems'
files = os.listdir('../' + folder)
files.sort()
os.chdir(f'../{folder}')
for file in files:
    if file.endswith(".pdf"):
        continue
    print(f'--------{file}--------')
    os.system(r'python ' + file)
os.chdir('../test')
print('-------------------运行完毕-------------------')
