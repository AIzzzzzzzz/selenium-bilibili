from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from chaojiying import Chaojiying_Client
from selenium import webdriver
import time


chaojiying = Chaojiying_Client('13353610096', 'a84526381', '925686')

user=input("请输入你的B站账号")
possword=input("请输入你的B站密码")
web=Chrome()

web.get('https://www.bilibili.com/')
time.sleep(1)
web.find_element(By.XPATH,'//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/span[1]/div/span/div').click()
web.switch_to.window(web.window_handles[-1])
time.sleep(1)
web.find_element(By.XPATH,'//*[@id="login-username"]').send_keys(user)
web.find_element(By.XPATH,'//*[@id="login-passwd"]').send_keys(possword)
time.sleep(0.5)
web.find_element(By.XPATH,'//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()
print("正在识别验证码")
time.sleep(3)
print("程序还在运行，请不要关闭\n")
print("正在寻找验证码坐标，需要5秒左右")
png=web.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[6]/div/div')
png_1=png.screenshot_as_png
dis=chaojiying.PostPic(png_1,9004)
result=dis['pic_str']
print(result)
li_list=result.split('|')
for i in li_list:
    x=i.split(',')[0]
    y=i.split(',')[1]
    ActionChains(web).move_to_element_with_offset(png,x,y).click().perform()

web.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[6]/div/div/div[3]/a').click()
time.sleep(2)



a=['硬币-2','经验+20']

web.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]').click()#刷新
time.sleep(2)
video_1=web.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a')
ActionChains(web).move_to_element(video_1).click().perform()#正常点击被拦截，使用动作链点击

time.sleep(3)
web.switch_to.window(web.window_handles[-1])


web.find_element(By.XPATH,'//*[@id="arc_toolbar_report"]/div[1]/span[2]/canvas').click()
time.sleep(2)
web.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[3]/div/div/div[4]/span').click()
time.sleep(1)
for i in a:
    print(f'\r{i}',end="")
    time.sleep(0.7)

web.close()
web.switch_to.window(web.window_handles[-1])

#第二次投币
web.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]').click()#刷新
time.sleep(1)
video_1=web.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a')
ActionChains(web).move_to_element(video_1).click().perform()#正常点击被拦截，使用动作链点击
time.sleep(3)
web.switch_to.window(web.window_handles[-1])
web.find_element(By.XPATH,'//*[@id="arc_toolbar_report"]/div[1]/span[2]/canvas').click()
time.sleep(2)
web.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[3]/div/div/div[4]/span').click()
time.sleep(1)
for i in a:
    print(f'\r{i}',end="")
    time.sleep(0.7)
web.close()
web.switch_to.window(web.window_handles[-1])

#第三次投币，加转发
web.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]').click()#刷新
time.sleep(1)
video_1=web.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a')
ActionChains(web).move_to_element(video_1).click().perform()#正常点击被拦截，使用动作链点击
time.sleep(3)
web.switch_to.window(web.window_handles[-1])
web.find_element(By.XPATH,'//*[@id="arc_toolbar_report"]/div[1]/span[2]/canvas').click()
time.sleep(2)
web.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[3]/div/div/div[2]/div[1]').click()
time.sleep(0.5)
web.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[3]/div/div/div[4]/span').click()
time.sleep(1)
b=['硬币-1','经验+10','今日投币经验已完成50/50，进入转发链接，将会转发至B站动态']
for i in b:
    print(f'\r{i}',end="")
    time.sleep(0.5)

time.sleep(1)
#转发到动态
zhuanfa=web.find_element(By.XPATH,'//*[@id="arc_toolbar_report"]/div[1]/span[4]/i')#鼠标悬停
ActionChains(web).move_to_element(zhuanfa).perform()
web.find_element(By.XPATH,'//*[@id="arc_toolbar_report"]/div[1]/span[4]/div/div/div[1]/div/div/span[1]/i').click()#点击动态
time.sleep(3)#等待动态加载

web.switch_to.frame(web.find_element(By.XPATH,'/html/body/div[5]/iframe'))#进入嵌入框架
time.sleep(2)


web.find_element(By.XPATH,'//*[@id="editor"]').send_keys('每天转发一条视频多得5经验，真好')

time.sleep(1)
web.find_element(By.XPATH,'//*[@id="app-container"]/div/div/div[5]/button').click()#↑这三行，为转发,进入后进行转发
time.sleep(1)
web.close()
web.switch_to.window(web.window_handles[-1])
c=['每日登录5经验已获得','观看视频5经验已获得',"投币50经验已获得","转发5经验已获得","今日经验已满共得65经验"]
for i in c:
    print(f'\r{i}',end="")
    time.sleep(0.5)
print("距离六级遥遥无期/(ㄒoㄒ)/~~")
print("哭~哭~")

