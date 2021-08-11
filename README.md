# NCUT图书馆答题脚本

作为一名即将步入NCUT的大一新生，我对于大学生活还是蛮期待的。在拿到通知书之前我就下定决心，不管去哪儿都要努力专于学业，服从安排，遵守要求。于是我拿到学号后就按照学校的要求去图书馆官网答题，哪知我直接被一堆莫名其妙的题目劝退了（~~我真想不懂为什么我需要记得图书馆负责xx的老师姓什么~~）。看着我根本过不了的考试然后我~~“一气之下”~~决定用魔法打败魔法，于是我就用写了个自动答题的脚本。没想到效果出奇的好，居然能排到排行榜里（虽然前面还有3个人）。为了帮助同学们不被这些痛苦之题折磨，我就在原本的基础上加以改进就有了这个脚本。

P.S. 如果有问题可以在新生群@我或者[提交issue](https://github.com/batu1579/NCUT-library-auto-answer/issues/new)，另外如果你喜欢这个项目记得给个star昂thx！

## 安装

1.  这个脚本只需要安装python解释器才能使用，下载地址： [python3.9]([Python Release Python 3.9.6 | Python.org](https://www.python.org/downloads/release/python-396/))
2.  下载脚本并解压

P.S. 如果有不会安装的可以看这个[教程]([全网最详细的Python安装教程（Windows） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/344887837))

## 使用

### 设置

在开始运行脚本前需要进行一些简单的设置：

1.  在`token.json`文件中填入自己的学号（id）和密码（password）
2.  在`settings.py`文件中找到`browser`键把后面的值修改成你电脑上安装了的浏览器（目前只支持使用相同内核的`edge`和`chrome`浏览器，计划过两天添加对`firefox`的支持）
3.  [可选] 如果你已经开始答题了，就需要在`settings.py`文件中找到`theme`键把对应的值修改成你所选取的皮肤即可。（这一步对于已经开始答题的同学十分重要，因为这个网站更换皮肤以后所有标签的`class`和`id`甚至页面布局都会改变。这就需要通过使用不同的css选择器来定位元素）

### 运行

双击文件夹中的`run.bat`文件即可运行程序。

P.S. 真不是我偷懒不想不弄成`exe`可执行文件，而是我和`pyinstaller`搏斗了一晚上，最后还是他赢了。。。他一直报错我也没办法嘛QAQ，只好麻烦想用的同学安装一下python了，所幸python装起来还比较简单。拜托有清楚的同学帮帮我蟹蟹 ！orz

## 配置文件

项目文件夹中的`settings.py`文件是这个脚本的配置文件。全部的设置都在这里，除了登录信息和api信息。

```python
script_settings = {

    # 开发者模式（输出更详细的日志）
    "dev_mode": False,
    
    # 驱动文件地址（如果没有为空即可，会自动下载匹配的驱动）
    "driver_path": "",

    # 本机使用的浏览器（要与所使用的驱动文件对应）
    #  - edge
    #  - chrome
    "browser": "edge",

    # 每次获取元素时等待的时间（秒）
    "wait_time": 0.1,

    # 运行时显示浏览器窗口
    "show_window": True,

    # 缓存位置
    "cache_path": ".\\cache",

    # 缓存大小
    "cache_size": 102400,

    # 验证码图片地址
    "veri_code_path": ".\\src\\img\\veri_code.png",

    # 验证码图像阈值
    "threshold_value": 130,

    # 使用百度api识别验证码
    "use_baidu_api": False,

    # api认证信息存放位置
    "api_token_path": ".\\api_token.json",

    # 调用api时重试的次数
    "retry_num": 3,

    # 使用的皮肤（如果已经登录选择过皮肤则必须与当前的皮肤一致）
    #  - school: 校园版
    #  - student: 书生版
    #  - warrior: 战士版
    "theme": "student"
}
```

## 提高识别准确度

脚本使用了百度文字识别api来提高验证码识别的准确度（主要是因为可以白嫖），需要到[百度AI开放平台](https://ai.baidu.com/tech/ocr/general)申请，申请方法见[这篇文章](https://ai.baidu.com/ai-doc/OCR/dk3iqnq51)

1.  在`settings.py`文件中将`use_baidu_api`键对应的值改为`true`
2.  在`api_token.json`文件中填入申请到的`app id`、`api key`、`secret key`分别填入对应的键中

## 特性

-   能够以飞一般的速度答题
-   自动根据网站更新题库，自动存储新题同时获取正确答案
-   在本地存储答案，节省时间
-   自动判断是否完成，如果以后增加了同一关卡中的题目数量也不会出问题
-   完美适配目前的三种皮肤，并且通过`json`文件存储css选择器，方便添加新皮肤后进行维护
-   可以手动调节每次定位前等待时间，在保证定位正常的情况下尽可能的缩短答题时间
-   使用`web-driver-manager`适配多种浏览器，并且能够自动下载对应的浏览器驱动
-   自动识别二维码
-   使用`easyocr`进行本地二维码识别
-   使用`baidu-aip`，支持使用百度文字识别api进行二维码识别，以提高识别的准确率

## 贡献者

欢迎同学们帮我完善这个脚本！

## 开源协议

[MIT](https://github.com/RichardLitt/standard-readme/blob/master/LICENSE) © Richard Littauer