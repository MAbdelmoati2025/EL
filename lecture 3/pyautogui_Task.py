import pyautogui
from time import sleep
import webbrowser

# فتح الرابط في نافذة جديدة
webbrowser.open_new_tab("https://drive.google.com/drive/folders/1bWC1vrs4NwLqyS5tnQ_2SjdwJIMhUNsE")
sleep(5)  # زيادة وقت الانتظار لضمان تحميل الصفحة بشكل كامل

while True:
    try:
        # انقر على الصورة الأولى
        print("start..")
        pyautogui.click('F:\\courses\\معتصم\\projects\\some projects\\img111.png')
        pyautogui.doubleClick()
        sleep(2)  # الانتظار قليلاً للتأكد من تنفيذ النقرات

        # انقر على الصورة الثانية
        print("next..")
        pyautogui.click('F:\\courses\\معتصم\\projects\\some projects\\img11.png')
        pyautogui.doubleClick()

        # انتقل إلى الإحداثيات المحددة وانقر مرتين
        print("next..")
        pyautogui.moveTo(993, 452, duration=2)
        pyautogui.doubleClick()
        sleep(4)

        pyautogui.press('f')
        pyautogui.press('f')
        pyautogui.press('f')

        print("done")
        break  # إذا تمت العملية بنجاح، نخرج من الحلقة

    except pyautogui.ImageNotFoundException as e:
        print(f'خطأ: {e}')
        sleep(5)  # الانتظار قبل المحاولة مجدداً في حالة عدم العثور على الصورة
    except Exception as e:
        print(f'حدث خطأ غير متوقع: {e}')
        sleep(5)  # الانتظار قبل المحاولة مجدداً في حالة حدوث خطأ غير متوقع
