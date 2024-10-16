'''
Author: MichLiu
Date: 2024-10-16 10:25:18
Description: 
LastEditTime: 2024-10-16 11:34:22
LastEditors: MichLiu
'''
import time
import json
from DrissionPage import ChromiumPage

print("start to upload to kuaishou")

def ks_browser_initial():
    try:
        browser = ChromiumPage()
        browser.get('https://passport.kuaishou.com/pc/account/login/')
        time.sleep(5)
        return browser
    except Exception as e:
        print("Error initializing browser:", str(e))
        return None

def ks_log(browser):
    """
    Load cookies from a local file and refresh the page to log in.
    """
    try:
        with open('kuaishou_cookies.txt', 'r', encoding='utf8') as f:
            listCookies = json.loads(f.read())
    
        for cookie in listCookies:
            cookie_dict = {
                'domain': '.kuaishou.com',
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                "expires": '',
                'path': '/',
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False
            }
            print(cookie_dict)
            browser.set.cookies(cookie_dict)
        time.sleep(2)
        browser.refresh()
        time.sleep(10)
    except Exception as e:
        print("Error logging in:", str(e))

# file_path
def ks_upload():
    try:
        browser = ks_browser_initial()
        if browser:
            ks_log(browser)
            browser.get("https://cp.kuaishou.com/article/publish/video")
    except Exception as e:
        print("Error uploading video:", str(e))

if __name__ == "__main__":
    ks_upload()
