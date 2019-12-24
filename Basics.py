# ecoding=utf-8
from drivers import AppiumTest
from drivers import Element
from time import sleep
from PIL import Image

at = AppiumTest()
driver = at.get_driver()

class basics_jc():
    def screenshot(self,path,left, upper, right, lower):
        sleep(3)
        # WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name('android.view.View'))
        # self.driver.find_element_by_class_name("android.widget.FrameLayout")
        driver.get_screenshot_as_file(path)
        sleep(1)
        img = Image.open(path)
        sleep(3)
        print(img.size)
        cropped = img.crop((left, upper, right, lower))  # (left, upper, right, lower)
        cropped.save(path)

