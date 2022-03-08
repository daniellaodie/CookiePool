# 配置文件

# Chrome

CHROME = {
    'add_argument': ['window-size=1920x3000', '--disable-gpu',
                     '--hide-scrollbars', 'blink-settings=imagesEnabled=false',
                     ]  # '--headless'
}

# 配置测试环境的redis地址
REDIS_URL = 'redis://:a123456@10.2.145.115:6379/2'

