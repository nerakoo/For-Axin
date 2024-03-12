def count_word_frequency(text):
    # 将文本转换为小写，以便统计时不区分大小写
    text = text.lower()
    # 使用非字母字符分割文本为单词列表
    words = re.findall(r'\b[a-z]+\b', text)
    # 初始化一个字典来存储单词频率
    frequency = {}
    # 遍历单词列表，统计每个单词出现的次数
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# 示例文本
text = "This is a simple example. This example is simple."
# 调用函数并打印结果
frequency = count_word_frequency(text)
for word, count in frequency.items():
    print(word, ":", count)
