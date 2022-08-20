<h1 align="center">NCUT 图书馆魔法答题 👋</h1>
<p align="center">
    <a href="#" target="_blank">
        <img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/batu1579/NCUT-library-auto-answer">
    </a>
    <a href="#" target="_blank">
        <img alt="GitHub" src="https://img.shields.io/github/license/batu1579/NCUT-library-auto-answer">
    </a>
</p>

> 使用魔法，飞一样的完成图书馆答题。\~(￣▽￣)\~\*
>
> 欢迎各位大佬帮我一起完善这个项目！如果有好的建议或者想反馈bug可以在新生群@我或者 [提交issue](https://github.com/batu1579/NCUT-library-auto-answer/issues/new) 。

## 安装依赖

> 此脚本需要安装 Python3.10 版本以上的解释器才能使用，还没有安装的同学可以看这个 [教程](https://zhuanlan.zhihu.com/p/344887837) 。

1. 下载脚本并解压。

## 使用方法

### 设置

> 目前脚本只支持 `Edge` 、 `Chrome` 和 `Firefox` 浏览器，用 `safari` 、 `opera` 和国产浏览器的同学抱歉哈，之后可能会支持的。（目前下载没有使用SSL验证，需要注意一下，如果可以的话还是手动下载最保险）。

在开始运行脚本前需要进行一些简单的设置：

1. 在 `token.json` 文件中填入自己的学号（ `id` ）和密码（ `password` ）。
2. 在 `./library/settings.py` 文件中找到 `browser` 键把后面的值修改成你电脑上安装了的浏览器。
3. [可选] 如果你已经开始答题了，就需要在 `./library/settings.py` 文件中找到 `theme` 键把对应的值修改成你所选取的皮肤即可（这一步对于已经开始答题的同学十分重要，因为这个网站更换皮肤以后所有标签的 `class` 和 `id` 甚至页面布局都会改变。这时需要通过使用不同的 CSS 选择器来定位元素）。

### 运行

双击文件夹中的 `run.bat` 文件即可运行程序。

也可以在终端中打开文件夹通过下面的指令打开：

```shell
python main.py
```

## 配置文件

项目文件夹中的 `./library/settings.py` 文件是这个脚本的配置文件。全部的设置都在这里，除了登录信息和 API 信息。

```python
# 开发者模式
# 在控制台输出更详细的日志，不过哪怕没有开也可以在运行后去 logs 文件夹中找到详细的日志文件
dev_mode = False

# 驱动文件地址（如果没有为空即可，会自动下载匹配的驱动）
driver_path = ""

# 本机使用的浏览器（要与所使用的驱动文件对应）
#  - edge
#  - chrome
#  - firefox
browser = "edge"

# Github个人令牌（防止github访问限制导致的下载驱动失败）
GitHub_token = ""

# 每次获取元素时等待的时间（秒）
# 减小这个值可以进一步缩短答题时间，只要你的网和配置都足够甚至可以10秒以内完成
wait_time = 0.1

# 运行时显示浏览器窗口（如果你连看都不想看那个题就可以关上）
show_window = True

# 验证码图片地址
veri_code_path = ".\\src\\img\\veri_code.png",

# 验证码图像二值化时的阈值，可以自己调整到一个合适的值来适当提高识别准确率
# 可以在识别过程中在存放验证码的地方查看效果
threshold_value = 130,

# 使用百度api识别验证码
use_baidu_api = False,

# api认证信息存放位置
api_token_path = ".\\api_token.json",

# 调用api时重试的次数
retry_num = 3,

# 使用的皮肤（如果已经登录选择过皮肤则必须与当前的皮肤一致）
#  - school: 校园版
#  - student: 书生版
#  - warrior: 战士版
theme = "student"
```

## 提高识别准确度

脚本使用了百度文字识别api来提高验证码识别的准确度（主要是因为可以白嫖），需要到 [百度AI开放平台](https://ai.baidu.com/tech/ocr/general) 申请，申请方法见 [这篇文章](https://ai.baidu.com/ai-doc/OCR/dk3iqnq51) 。

1. 在 `./library/settings.py` 文件中将 `use_baidu_api` 键对应的值改为`true` 。
2. 在 `api_token.json` 文件中填入申请到的 `app id` 、`api key` 、`secret key` 分别填入对应的键中。

## 自动安装依赖

脚本会在首次运行后安装依赖，以后的运行中不会重复安装。但是你可以手动让脚本进行一次更新：

你可以通过以下命令再次安装依赖：

```shell
pip install -r requirements.txt
```

你还可以通过将`library/run_time.json`文件中的`is_first_time`键对应的值改为`true`来使下一次运行前自动安装依赖

_悄悄告诉你，也可以通过双击`install_requirement.bat`文件再次安装依赖， ~~那些不认真看文档的人肯定看不见这行字。~~_

## 设置 GitHub 个人令牌

GitHub 对于匿名访问有限制（60次每小时），可能会影响到个别需要从 GitHub 上下载的驱动。增加上限需要申请一个 GitHub 个人令牌，申请方式见 [这里](https://docs.github.com/cn/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) 。然后把申请到的令牌填在 `settings.py` 的 `GitHub_token` 键中。

## 特性

- 能够使用魔法以飞一般的答题。
- 自动根据网站更新题库，自动存储新题同时获取正确答案。
- 在本地存储答案，节省时间。
- 自动判断是否完成，如果以后增加了同一关卡中的题目数量也不会出问题。
- 完美适配目前的三种皮肤，并且通过 `json` 文件存储 CSS 选择器，方便添加新皮肤后进行维护。
- 可以手动调节每次定位前等待时间，在保证定位正常的情况下尽可能的缩短答题时间。
- 使用 [webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager) 适配多种浏览器，并且能够自动下载对应的浏览器驱动。
- 自动识别二维码。
- 使用 [easyocr](https://github.com/JaidedAI/EasyOCR) 进行本地二维码识别。
- 支持使用 [baidu-aip](https://github.com/Baidu-AIP/python-sdk) 提高二维码识别的准确率。
- 首次使用脚本可以自动安装依赖的 `pip` 包。
- 可以支持使用大多数主流的浏览器（edge、chrome、firefox）。

## 声明

此脚本的目的在于技术交流和学习 Selenium 使用。请勿用于其他目的。具体内容请查看 [开源协议](https://github.com/batu1579/NCUT-library-auto-answer/blob/main/LICENSE) 。

## 作者

👤 **BATU1579**

- Github: [@batu1579](https://github.com/batu1579)

## 支持

如果有帮到你的话，帮我点颗小星星叭~ ⭐️

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
