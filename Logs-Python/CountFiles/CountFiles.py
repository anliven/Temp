# -*- coding: utf-8 -*-
import os
import sys

word_list = ["effect", "supplementaryInformationFields", "instructions"]
style_list = ['=', '="" ']
count_list = {
    'None': '',
    'Empty': '',
    'Have': ''
}

in_dir = ''
man_files = None

if len(sys.argv) == 2:
    if os.path.isdir(sys.argv[1]):
        in_dir = sys.argv[1]
        man_files = os.listdir(in_dir)
    else:
        print("this is not directory: %s " % in_dir)
        exit()
else:
    in_dir = os.getcwd() + '\\'
    man_files = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.man']

if format(str(man_files), 's').count('.man') == 0:
    print("! No man files in this directory: '%s'" % in_dir)
    exit()
print("The sum total of man files: ", len(man_files))


def get_count_num(file, word):
    with open(in_dir + file, encoding="utf-8") as source:
        content = source.read()
        if format(content, 's').count(word + style_list[0]) == 1:
            if word + style_list[1] in content:
                count_list['Empty'] += " " + file
            else:
                count_list['Have'] += " " + file
        else:
            count_list['None'] += " " + file


for w in word_list:
    print("\n### Fragment - %s " % w)
    for f in man_files:
        get_count_num(f, w)
    for key, value in count_list.items():
        print('*** count:{} - {}:\n{}'.format(format(value, "s").count('.man'), key, value))
    for key in count_list.keys():
        count_list[key] = ''
        