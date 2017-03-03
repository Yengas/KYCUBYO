import os
import sys

def print_directory(file_name, full_path, level):
    has_readme = os.path.isfile(os.path.join(full_path, 'README.md'))
    print(('\t' * level) + '- ' + (file_name if not has_readme else '[%s](%s)' % (file_name, full_path)))

def print_file(file_name, full_path, level):
    print(('\t' * level) + '- [%s](%s)' % (os.path.splitext(file_name)[0], full_path))

def walk_directory(path = '.', level = 0, exclude = ['.git', '.idea']):
    for file_name in os.listdir(path):
        full_path = os.path.join(path, file_name)
        if file_name in exclude: continue
        if os.path.isdir(full_path):
            print_directory(file_name, full_path, level)
            walk_directory(full_path, level + 1)
        elif file_name != 'README.md' and file_name.endswith('.md'):
            print_file(file_name, full_path, level)


walk_directory()
