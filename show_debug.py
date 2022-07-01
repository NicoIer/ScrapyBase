from selenium import webdriver

# 调试模式? 能否看见输出
DEBUG = True
# EDGE webdriver启动位置
EDGE_PATH = r'E:\Learning\PythonLearning\ScrapyBase\JDSPider\msedgedriver.exe'

if __name__ == '__main__':
    options = webdriver.EdgeOptions()
    if DEBUG is False:
        options.add_argument('headless')
    driver = webdriver.Edge(EDGE_PATH, options=options)
    driver.get('https://item.jd.com/100019386660.html#comment')
    while True:
        pass