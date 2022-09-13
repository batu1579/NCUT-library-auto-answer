#!/usr/bin/env python
# coding=utf-8
'''
Author: BATU1579
Date: 2021-08-08 17:00:33
LastEditors: BATU1579
LastEditTime: 2021-09-04 17:52:28
Description: file content
'''
import library.const as g
from time import sleep
from PIL import Image
from aip import AipOcr
from os.path import exists
from library.easyocr import easyocr
from library.get_driver import get_broswer
from library.use_data import get_file_data, get_json_data, save_json_data


def is_exist(css_selector: str) -> bool:
    try:
        browser.find_element_by_css_selector(css_selector)
        return True
    except Exception:
        return False


def click_element(css_selector: str):
    g.LOG.debug("click element: %s" % css_selector)
    browser.find_element_by_css_selector(css_selector).click()


def get_element_text(css_selector: str) -> str:
    return browser.find_element_by_css_selector(css_selector).text


def is_veri_code_correct() -> bool:
    # 检测验证码是否正确
    try:
        text = get_element_text("div.layui-layer-msg > div")
        if text == "图片验证码不正确":
            g.LOG.debug("验证码错误 ！")
            return False
        else:
            g.LOG.error("账号密码有误 ！")
            browser.quit()
            g.LOG.info("浏览器已关闭 ！")
            exit()
    except Exception:
        return True


def preprocessing_img():
    # 获取验证码图片
    veri_code_img = browser.find_element_by_id("vcodeimg")
    veri_code_img.screenshot(g.VERI_CODE_PATH)

    # 处理图片
    img = Image.open(g.VERI_CODE_PATH)
    img = img.convert("L")
    img = img.point(lambda x: 0 if x < g.THRESHOLD_VALUE else 255)
    img.save(g.VERI_CODE_PATH)


def ident_veri_code_api() -> bool:
    preprocessing_img()

    # 识别验证码
    api_token = get_json_data(g.API_TOKEN_PATH)
    client = AipOcr(api_token["id"], api_token["key"], api_token["secret_key"])
    img = get_file_data(g.VERI_CODE_PATH)
    veri_code = client.basicAccurate(img, options={"language_type": "ENG",})
    if len(veri_code) == 2 and veri_code["error_code"] == 18:
        # 超过频率限制
        sleep(3)
        g.LOG.debug("超出api频率限制，等待中...")
        return False
    elif "error_code" in veri_code:
        # 其他错误
        g.LOG.warning(veri_code["error_msg"])
        return False
    elif veri_code["words_result_num"] == 0:
        g.LOG.debug("未识别出字符")
        return False
    veri_code = veri_code['words_result'][0]['words'].replace(" ", "")

    # 填写验证码并登录
    g.LOG.debug("识别结果： %s" % veri_code)
    browser.find_element_by_id("pVCode").send_keys(veri_code)
    click_element("#btnLogin")

    return is_veri_code_correct()


def ident_veri_code_local() -> bool:
    preprocessing_img()

    # 识别验证码
    reader = easyocr.Reader(["en",])
    veri_code = reader.readtext(g.VERI_CODE_PATH)
    veri_code = veri_code[0][1]

    # 填写验证码并登录
    g.LOG.debug("识别结果： %s" % veri_code)
    browser.find_element_by_id("pVCode").send_keys(veri_code)
    click_element("#btnLogin")

    return is_veri_code_correct()


def api_reco() -> bool:
    g.LOG.info("正在调用百度api识别验证码...")
    for retry_time in range(g.RETRY_NUM ):
        if ident_veri_code_api():
            return True
        else:
            g.LOG.debug("[api] 正在重试 %d/%d..." % (retry_time + 1, g.RETRY_NUM))
        sleep(3)
    return False


def local_reco():
    g.LOG.debug("正在本地识别验证码...")
    while ident_veri_code_local() == False:
        g.LOG.debug("[本地] 正在重试 ...")
        sleep(3)
    else:
        return True


def manually_reco():
    g.LOG.debug("正在使用手动输入验证码...")
    veri_code = input("请输入验证码：")
    browser.find_element_by_id("pVCode").send_keys(veri_code)
    click_element("#btnLogin")
    return is_veri_code_correct()


def login() -> bool:
    # 输入用户名和密码
    token = get_json_data(".\\token.json")
    browser.find_element_by_id("userid").send_keys(token["id"])
    browser.find_element_by_id("pwd").send_keys(token["password"])

    # 填写验证码(直到输对)
    g.LOG.info("正在尝试登录...")

    # 手动输入验证码
    if g.USE_INPUT_VERI:
        return manually_reco()

    # 使用百度api识别
    if not g.USE_BAIDU_API:
        pass
    elif not exists(g.API_TOKEN_PATH):
        g.LOG.warning("未找到api_token文件，无法调用api ！")
    else:
        if api_reco():
            return True

    # 本地识别
    if local_reco():
        return True


def get_selections() -> dict:
    # 判断题目类型
    data = {}
    # 检测选项数量
    li = browser.find_elements_by_css_selector(g.THEME["all_selections"])
    num_list = [i + 1 for i in range(len(li))]
    # 获取全部选项内容
    for num in num_list:
        index =  num + 3 if g.THEME_NAME == "student" else num
        data[get_element_text(g.THEME["selection"] % index)] = num
    return data


def trans(data: str or int) -> int or str:
    '''
    转换选项与序号
    '''    
    code_list = ["A", "B", "C", "D"]
    if type(data) == str:
        assert data in code_list
        return code_list.index(data) + 1
    elif type(data) == int:
        assert 1 <= data <= 4
        return code_list[data - 1]


def select_answer(ans: int):
    """
    ans = 1 or 2 or 3 or 4
    """
    ans_amend = (ans + 3) if g.THEME_NAME == "student" else ans
    click_element(g.THEME["check_box"] % ans_amend)
    g.LOG.debug("选择选项： %s" % trans(ans))
    click_element("#btnSubmit")


def ans_question() -> bool:
    global ans_dict
    # 读取题目
    question = get_element_text(g.THEME["question"]).split("\n")
    question = question[-1]
    g.LOG.debug("当前题目： %s" % question)
    selections = get_selections()
    # 查询答案
    try:
        select_answer(selections[ans_dict[question]])
        g.LOG.debug("读取答案： %s" % ans_dict[question])
        return True
    except Exception:
        # 没有记录就选A
        select_answer(1)
        # 记录正确答案
        correct_ans = get_element_text("#correctAns")
        correct_ans = correct_ans[-1]
        ans_index = list(selections.values()).index(trans(correct_ans))
        ans_dict[question] = list(selections.keys())[ans_index]
        return False


def start_ans() -> bool:
    
    browser.execute_script("isVisitAll = \"True\";")
    
    # 点击闯关
    if g.THEME_NAME == "warrior":
        sleep(2)
    click_element(g.THEME["start_test"])
    # 曾经答过则跳出
    if is_exist("body > div.middle-box > a.btn"):
        click_element("body > div > a")
        return True
    while ans_question():
        # 下一题
        click_element("#qd")
        # 检查是否答完
        if is_exist(g.THEME["finished_img"]):
            click_element(g.THEME["collect_item_button"])
            click_element(g.THEME["next_level_button"])
            return True
        elif is_exist(g.THEME["next_level_button"]):
            click_element(g.THEME["next_level_button"])
            return True
    else:
        # 无论对错都回退
        g.LOG.debug("未查询到答案，正在重试...")
        browser.back()


def select_level(level_name: str):

    global ans_dict

    # 进入关卡
    sleep(0.5)
    click_element(".%s" % level_name)

    # 读取答案
    ans_file_path = ".\\src\\answers\\%s.json" % level_name
    ans_dict = get_json_data(ans_file_path)

    origin_num = len(ans_dict)

    # 开始答题
    while not start_ans(): pass

    # 保存答案
    if origin_num != len(ans_dict):
        save_json_data(ans_file_path, ans_dict)
        g.LOG.debug("新增 %d 条数据" % (len(ans_dict) - origin_num))
    g.LOG.info("关卡 %s 已完成 ！" % level_name)

    # 退回选择界面
    click_element("div.back")


def main():
    # 打开网页
    browser.get("http://bfgydxrgjy7.zhixinst.com")
    click_element("img.kscgbtn")

    # 登录
    click_element("div.left_nav > div.zhuangshiborder")
    login()
    g.LOG.info("登陆成功 ！")

    # 重新考试
    if is_exist("div.layui-layer > div.layui-layer-btn > a"):
        click_element("div.layui-layer > div > a.layui-layer-btn0")

    # 选择界面
    if browser.find_element_by_id("btnTheme").is_displayed():
        theme_list = ["student", "warrior", "school"]
        selector = ".items > ul > li:nth-child(%d) > a > input" % (
            theme_list.index(g.THEME_NAME) + 1)
        click_element(selector)
        click_element("#btnTheme")

    for step in g.THEME["level_list"]:
        select_level(step)
    
    # 读取成绩
    click_element("div.left_nav > div.zhuangshiborder")
    click_element("#operatelist > a:nth-child(3)")
    text = get_element_text("#xxtr")
    text = text.split(" ")
    g.LOG.info("当前排名： %s" % text[0])
    g.LOG.info("答题用时： %s" % text[-1])

    return True


# --------------------运行--------------------

# 初始化
ans_dict = {}
browser = get_broswer()

try:
    main()
    g.LOG.info("Done !")
except Exception as error_info:
    # 浏览器截屏
    browser.save_screenshot(".\\logs\\error_screenshot.png")

    # 记录错误信息
    g.LOG.exception("错误信息：")
    g.LOG.error("出现错误，请重试或提交 log 文件夹下最新的日志文件与浏览器截图到 issue 页面 ！")

browser.quit()
g.LOG.info("浏览器已关闭 ！")
