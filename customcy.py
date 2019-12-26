# author: my
# date: 2019/12/26

import jieba  # 分词
from wordcloud import WordCloud  # 词云图
import matplotlib.colors as colors  # 处理图片相关内容
import numpy
from PIL import Image
import matplotlib.pyplot as plt

# 生成词云方法(以庆余年小说为例)
def get_wcloud():
	# 读取小说内容
    with open(r'庆余年.txt', 'r', encoding='gbk') as txt:
        data = txt.read()
    # 加载词典
    jieba.load_userdict('scel_to_text.txt')
    # 也可以添加自定义词典
    jieba.add_word('范慎')
    jieba.add_word('范闲')
    # 将文件中所有文字分词
    words_list = jieba.lcut(data)
    # 用空格分隔词语
    tokenstr = ' '.join(words_list)
    # 打开背景图片
    color_mask = numpy.array(Image.open('man.png'))
    # 自定义文字颜色
    colormaps = colors.ListedColormap(['#FF0000','#FF7F50','#FFE4C4'])
    # 生成词云（默认样式）
    # mywc1 = WordCloud().generate(tokenstr)
    # 生成词云（自定义样式）
    mywc1 = WordCloud(
        mask=color_mask,  # 指定背景图形状
        colormap=colormaps,  # 指定颜色
        # font_path='C:/Windows/Fonts/simkai.ttf',  # 指定字体
        background_color='white',  # 指定背景颜色，默认黑色
        width=800,  # 指定宽度
        height=600  # 指定高度
    ).generate(tokenstr)
    # 显示词云
    plt.imshow(mywc1)
    plt.axis('off')
    plt.show()
    mywc1.to_file('庆余年.png')  # 生成词云图片


if __name__== '__main__':
    get_wcloud()

