# encoding=utf-8
import re
import os

from tqdm import tqdm


def cut_sentences(para):
    """
    中文分句
    :param para: 文章
    :return: 切好的句子
    """
    para = para.replace('\n', ' ')
    para = re.sub('([。！？?])([^”’d])', r"\1\n\2", para)  # 单字符断句符
    para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)  # 英文省略号
    para = re.sub('(…{2})([^”’])', r"\1\n\2", para)  # 中文省略号
    para = re.sub('([。！？?][”’])([^，。！？?])', r'\1\n\2', para)
    # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
    para = para.rstrip()  # 段尾如果有多余的\n就去掉它
    # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
    return para.split("\n")

file_path = r'E:\文档\4.郑州大学_研究生\7.医学知识图谱\2.bestpractice_markdown\bestpractice_c\1.md'
def read_one_article(file_path):
    article = ''
    art_lst = []
    with open(file_path, encoding='utf-8') as fr:
        for line in fr:
            line = line.strip()
            if '##' in line:
                line = '。'+line+'。'
            article += line
        if article:
            ls = cut_sentences(article)
            for l in ls:
                l = l.lstrip('。')
                if l:
                    if '##' in l:
                        l = l.replace('。', '')
                    art_lst.append(l.strip().replace(' ', ''))
    return art_lst
root_dir = r'E:\文档\4.郑州大学_研究生\7.医学知识图谱\2.bestpractice_markdown\bestpractice_c'
file_lst = os.listdir(root_dir)[:]
with open('best_practice_data.txt', 'a', encoding='utf-8') as fa:
    for n in tqdm(file_lst):
        print(f'file name {n}')
        file_path = os.path.join(root_dir, n)
        lst_art = read_one_article(file_path)
        for ls in lst_art:
            fa.write(ls+'\n')
        fa.write('\n')
