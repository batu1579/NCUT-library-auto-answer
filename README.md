# NCUT图书馆答题脚本

作为一名即将步入NCUT的大一新生，我对于大学生活还是蛮期待的。在拿到通知书之前我就下定决心，不管去哪儿都要努力专于学业，服从安排，遵守要求...于是我拿到学号后就按照学校的要求去图书馆官网答题，哪知我直接被一堆莫名其妙的题目劝退了（~~我真想不懂为什么我需要记得图书馆负责xx的老师姓什么~~）。看着我根本过不了的考试然后我 ~~”一气之下“~~ 决定用魔法打败魔法，于是我就用写了个自动答题的脚本。没想到效果出奇的好，居然能排到排行榜里。为了帮助同学们不被这些痛苦之题折磨，我就在原本的基础上加以改进，于是就有了这个脚本。

>   **事先声明：** 本脚本的目的在于技术交流和学习selenium使用，绝对没有反对学校工作和指责题目的意思（因为只有学校真下了心思才会弄出这么个答题功能，不得不说学校确实有心了）。另外请各位同学们最好还是先自己答一遍题以后再来尝试这个脚本，毕竟以后大学生活中要去图书馆的次数肯定不会少。这个答题的目的主要是为了让同学们能够记住其中的知识点，好在以后的学习中节省时间提高效率。

P.S. 如果有好的建议或者想反馈bug可以在新生群@我或者[提交issue](https://github.com/batu1579/NCUT-library-auto-answer/issues/new)，另外如果你喜欢这个项目记得给个`star`昂靴靴啦！

## 安装

1.  这个脚本需要安装python解释器才能使用，下载地址： [python3.9](https://www.python.org/downloads/release/python-396/)
2.  下载脚本并解压

P.S. 如果有不会安装的可以看这个[教程](https://zhuanlan.zhihu.com/p/344887837)

## 使用

### 设置

>   目前脚本只支持 `Edge` 、 `Chrome` 和 `Firefox` 浏览器，用 `safari` 、 `opera` 和国产浏览器的同学抱歉哈，之后可能会支持的。（目前下载没有使用SSL验证，需要注意一下，如果可以的话还是手动下载最保险）

在开始运行脚本前需要进行一些简单的设置：

1.  在`token.json`文件中填入自己的学号（id）和密码（password）
2.  在`./library/settings.py`文件中找到`browser`键把后面的值修改成你电脑上安装了的浏览器
3.  [可选] 如果你已经开始答题了，就需要在`./library/settings.py`文件中找到`theme`键把对应的值修改成你所选取的皮肤即可。（这一步对于已经开始答题的同学十分重要，因为这个网站更换皮肤以后所有标签的`class`和`id`甚至页面布局都会改变。这就需要通过使用不同的css选择器来定位元素）

### 运行

双击文件夹中的`run.bat`文件即可运行程序。

也可以在终端中打开文件夹通过下面的指令打开：

```shell
python main.py
```



P.S. 真不是我偷懒不想不弄成`exe`可执行文件，而是我和`pyinstaller`搏斗了一晚上，最后还是他赢了。。。他一直报错我也没办法嘛QAQ，只好麻烦想用的同学安装一下python了，所幸python装起来还比较简单。拜托有清楚的同学帮帮我蟹蟹 ！orz

## 配置文件

项目文件夹中的`./library/settings.py`文件是这个脚本的配置文件。全部的设置都在这里，除了登录信息和api信息。

```python
script_settings = {

    # 开发者模式
    # 在控制台输出更详细的日志，不过哪怕没有开也可以在运行后去 logs 文件夹中找到详细的日志文件
    "dev_mode": False,
    
    # 驱动文件地址（如果没有为空即可，会自动下载匹配的驱动）
    "driver_path": "",

    # 本机使用的浏览器（要与所使用的驱动文件对应）
    #  - edge
    #  - chrome
    #  - firefox
    "browser": "edge",

    # Github个人令牌（防止github访问限制导致的下载驱动失败）
    "GitHub_token": "",

    # 每次获取元素时等待的时间（秒）
    # 减小这个值可以进一步缩短答题时间，只要你的网和配置都足够甚至可以10秒以内完成
    "wait_time": 0.1,

    # 运行时显示浏览器窗口（如果你连看都不想看那个题就可以关上）
    "show_window": True,

    # 验证码图片地址
    "veri_code_path": ".\\src\\img\\veri_code.png",

    # 验证码图像二值化时的阈值，可以自己调整到一个合适的值来适当提高识别准确率
    # 可以在识别过程中在存放验证码的地方查看效果
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

1.  在`./library/settings.py`文件中将`use_baidu_api`键对应的值改为`true`
2.  在`api_token.json`文件中填入申请到的`app id`、`api key`、`secret key`分别填入对应的键中

## 自动安装依赖

脚本会在首次运行后安装依赖，以后的运行中不会重复安装。但是你可以手动让脚本进行一次更新：

你可以通过以下命令再次安装依赖：

```shell
pip install -r requirements.txt
```

你还可以通过将`library/run_time.json`文件中的`is_first_time`键对应的值改为`true`来使下一次运行前自动安装依赖

*悄悄告诉你，也可以通过双击`install_requirement.bat`文件再次安装依赖，~~那些不认真看文档的人肯定看不见这行~~*字

## 设置GitHub个人令牌

GitHub对于匿名访问有限制（60次每小时），可能会影响到个别需要从GitHub上下载的驱动。增加上限需要申请一个GitHub个人令牌，申请方式见[这里](https://docs.github.com/cn/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)。然后把申请到的令牌填在 `settings.py` 的 `GitHub_token` 键中。

## 特性

-   能够以飞一般的速度答题
-   自动根据网站更新题库，自动存储新题同时获取正确答案
-   在本地存储答案，节省时间
-   自动判断是否完成，如果以后增加了同一关卡中的题目数量也不会出问题
-   完美适配目前的三种皮肤，并且通过`json`文件存储css选择器，方便添加新皮肤后进行维护
-   可以手动调节每次定位前等待时间，在保证定位正常的情况下尽可能的缩短答题时间
-   使用[webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager))适配多种浏览器，并且能够自动下载对应的浏览器驱动
-   自动识别二维码
-   使用[easyocr](https://github.com/JaidedAI/EasyOCR)进行本地二维码识别
-   使用[baidu-aip](https://github.com/Baidu-AIP/python-sdk)，支持使用百度文字识别api进行二维码识别，以提高识别的准确率
-   首次使用脚本可以自动安装依赖的`pip`包
-   可以支持使用大多数主流的浏览器（edge、chrome、firefox）

## 贡献者

欢迎同学们帮我完善这个脚本！

## 开源协议

[MIT](https://github.com/RichardLitt/standard-readme/blob/master/LICENSE) © Richard Littauer