import os
from pathlib import Path
import runpy
import sys
import traceback

import matplotlib.pyplot as plt


def main():
    problems_dir = Path(__file__).resolve().parents[1] / 'Problems'
    original_cwd = Path.cwd()
    original_path = sys.path[:]
    original_argv = sys.argv[:]
    original_show = plt.show
    failures = []

    # 每道题只生成图，全部运行完后再统一显示，避免逐题等待关窗。
    plt.show = lambda *args, **kwargs: None
    try:
        sys.path.insert(0, str(problems_dir.parent))
        sys.path.insert(0, str(problems_dir))
        for file in sorted(problems_dir.glob('*.py')):
            print('*' * 10 + f' {file.name} ' + '*' * 10, flush=True)
            os.chdir(problems_dir)
            sys.argv = [str(file)]
            try:
                runpy.run_path(str(file), run_name='__main__')
            except SystemExit as exc:
                if exc.code not in (None, 0):
                    failures.append(file.name)
                    traceback.print_exc()
            except Exception:
                failures.append(file.name)
                traceback.print_exc()
    finally:
        plt.show = original_show
        os.chdir(original_cwd)
        sys.path[:] = original_path
        sys.argv = original_argv

    print('-' * 20 + '运行完毕' + '-' * 20, flush=True)
    if failures:
        print('运行失败的题目：' + '、'.join(failures), flush=True)
    if plt.get_fignums():
        original_show()


if __name__ == '__main__':
    main()
