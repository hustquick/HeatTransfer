import os

folder = 'Problems'
files = os.listdir('../' + folder)
files.sort()
os.chdir(f'../{folder}')
for file in files:
    if file.endswith(".pdf"):
        continue
    print('*'*10 + f' {file} ' + '*'*10)
    os.system(r'python ' + file)
os.chdir('../test')
print('-'*20 + '运行完毕' + '-'*20)
