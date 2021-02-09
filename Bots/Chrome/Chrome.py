from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver = webdriver.Chrome('D:\Python Files\Projects\Bots\Chrome\chromedriver_win32\chromedriver.exe')

def attach(executor_url,session_id):
    original=WebDriver.execute
    def new_command_execute(self,command,params=None):
        if command == 'newsession':
            return {'Success':0,'value': None, 'sessionId': session_id}
        else:
            return original(self,command,params)
    WebDriver.execute = new_command_execute
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver.session_id = session_id
    WebDriver.execute = original
    return driver

executor_url=driver.command_executor._url
session_id=driver.session_id
browser = attach(executor_url,session_id)
browser.get('https://www.youtube.com')