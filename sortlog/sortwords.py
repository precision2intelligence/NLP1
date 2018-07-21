import json
import re
import argparse

def find_words(source_file):
    allfind = []
    with open(source_file ,encoding='UTF-8') as f:
        for line in f:
            result = re.findall('"count": (\d+), "word": "(.*?)"', line)#这里不知道如何匹配中文
            allfind.extend(result)
    return allfind
    
def checkCh(item):
    flag = True
    for char in item[1]:
        if u'\u4e00' <= char <= u'\u9fff':
            continue
        else:
            flag = False
    return flag
    
def make_dic(allfind):
    words = dict()
    for item in allfind:
        if checkCh(item):
            if item[1] in words.keys():
                words[item[1]] += int(item[0])
            else:
                words[item[1]] = int(item[0])
    return words
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', default="log.2018-05-31") 
    parser.add_argument('--target', default="words.json" )
    args = parser.parse_args()
    source_file = args.source
    target_file = args.target
    findall = find_words(source_file)
    data = make_dic(findall)
    data_sorted = sorted(data.items(), key=lambda v: v[1],reverse=True)
    with open(target_file,'w',encoding="UTF-8") as f:
        f.write(json.dumps(data_sorted,ensure_ascii=False))