#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'rino0601'


def main():
    import sys
    import os
    from random import shuffle

    if len(sys.argv) < 3:
        print "usage : python exam_generate_from.py [resourse .csv | .dat] [number of word]"

    dat_file_path = sys.argv[1]
    number_of_line = int(sys.argv[2])
    engs=[]
    kors=[]
    with open(dat_file_path) as raw_dat:
        for i, line in enumerate(raw_dat):
            if i < number_of_line:
                engs.append(line)
            else:
                kors.append(line)

    csv_file_path = 'temp'
    with open(csv_file_path,'w') as temp:
        for e, k in zip(engs,kors):
            temp.write(e[:-1]+', '+k)
        temp.write('\n')


    with open(csv_file_path) as source:  # file read.
        mDict = {}
        for line in source:
            temp = line.split(',')
            key = temp.pop(0)
            temp = [t.strip(' ') for t in temp]  # 공백 제거
            mDict[key] = temp

    # processing
    keys = mDict.keys()
    shuffle(keys)

    result_csv = 'result%d.csv'
    varius = 0
    while os.path.isfile(result_csv % varius):
        varius += 1
        if varius == 10:
            print "TOO MANY files!"
            return 0

    with open((result_csv % varius), 'w') as result:  # file write.
        for shuffled_key in keys:
            result.write("%s:%s" % (shuffled_key, ", ".join(mDict[shuffled_key])))


if __name__ == '__main__':
    main()