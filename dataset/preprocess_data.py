import re
import json
def read_txt(file_path):
    with open(file_path, 'r') as file:
        # 读取文件内容
        file_contents = file.read()
    # print(file_contents)
    return file_contents
    
def split_txt(txt):
    pattern = r'(第[一二三四五六七八九十百]+回)'
    # pattern = r"(第[\u4e00-\u9fff\d]+集)"
    # 使用正则表达式替换全角空格字符
    # txt = re.sub('\u3000', '', txt)
    # pattern = r'(^\d.*?(?=\n|$))'
    # 使用 re 模块进行匹配
    title = re.findall(pattern, txt,re.MULTILINE) 
    print(title)
    # 根据标题切分
    segments = re.split(pattern, txt, flags=re.MULTILINE)
    # segments = [segment.strip() for segment in segments]
    # print(segments)
    # 创建一个空字典
    result_dict = {}
    # 如果头那部分没有标题
    if segments.index(title[0]) > 0:
        result_dict['header'] = segments[0]
    # 使用循环将列表B的元素作为字典的键，列表A中对应位置的元素作为值
    for i in range(len(title)):
        if i < len(segments) - 1:
            result_dict[title[i]] = segments[segments.index(title[i]) + 1]

    # 创建一个新的字典来存储包含'黛玉'的键-值对
    filtered_dict = {}

    for key, value in result_dict.items():
        if '黛玉' in value:
            filtered_dict[key] = value


    format_file='./data/novel_data/stone_daiyu.txt'
    # 打开文件以写入字典数据
    with open(format_file, 'w') as file:
        for key, value in filtered_dict.items():
            # 将键和值格式化为字符串，并写入文件
            file.write(f'{key}: {value}\n')

    
def format_txt(txt):
    # txt = re.sub('\u3000\u3000', ' ', txt)
        # 使用 splitlines() 方法拆分文本成行
    lines = txt.splitlines()

    # 去掉每一行开头的空格
    lines = [line.lstrip() for line in lines]
    # 去掉空白行
    cleaned_lines = [line for line in lines if line.strip()]
    # 将处理后的行重新组合成文本
    cleaned_text = '\n'.join(cleaned_lines)
    # 打开文件以写入匹配的文本
    with open('./data/novel_data/stone_format.txt', 'w') as file:
        file.write(cleaned_text)
        
if __name__ == '__main__':
    file = './data/novel_data/stone_format.txt'
    txt  = read_txt(file)
    # format_txt(txt)
    split_txt(txt)
    