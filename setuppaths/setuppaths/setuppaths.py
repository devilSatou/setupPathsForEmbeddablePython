import os
import sys

def add_project_paths():
    # カレントディレクトリを追加
    sys.path.append(os.path.abspath(os.getcwd()))

    # サブディレクトリを再帰的に追加
    for root, dirs, files in os.walk(os.path.abspath(os.getcwd())):
        for dir in dirs:
            sys.path.append(os.path.join(root, dir))