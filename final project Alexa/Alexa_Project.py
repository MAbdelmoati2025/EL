import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
from datetime import datetime
import pyautogui
import webbrowser
from googletrans import Translator
import pywhatkit



'''*********************************************************************'''


# تعريف كائن التعرف على الصوت
My_voice = sr.Recognizer()
translator = Translator()



'''***********************************************************************'''




class Alexa:
    def __init__(self):
        self.commands = {
        # Time commands
            "الساعه": lambda: self.show_time(language_choose),
            "الساعة": lambda: self.show_time(language_choose),
            "clock": lambda: self.show_time(language_choose),
            "time": lambda: self.show_time(language_choose),
            "الوقت": lambda: self.show_time(language_choose),
            "الآن": lambda: self.show_time(language_choose),
            "الوقت الآن": lambda: self.show_time(language_choose),
        # Terminal commands
            "ترمنال": lambda: self.open_terminal(language = language_choose),
            "ترمينال": lambda: self.open_terminal(language = language_choose),
            "terminal": lambda: self.open_terminal(language = language_choose),
            "open terminal": lambda: self.open_terminal(language = language_choose),
            "فتح تيرمينال": lambda: self.open_terminal(language = language_choose),
            "command line": lambda: self.open_terminal(language = language_choose),
            "سطر الأوامر": lambda: self.open_terminal(language = language_choose),
        # My name
            "اسمك اي": lambda: self.who_am_i(language_choose, myName),
            "اسمك": lambda: self.who_am_i(language_choose, myName),
            "اسم": lambda: self.who_am_i(language_choose, myName),
            "يسمي": lambda: self.who_am_i(language_choose, myName),
            "ما هو اسمك": lambda: self.who_am_i(language_choose, myName),
            "Name": lambda: self.who_am_i(language_choose, myName),
            "name": lambda: self.who_am_i(language_choose, myName),
            "What is your name": lambda: self.who_am_i(language_choose, myName),
            "My name is": lambda: self.who_am_i(language_choose, myName),
        # GitHub
            "جيت": lambda: self.open_github(language_choose),
            "hub": lambda: self.open_github(language_choose),
            "git": lambda: self.open_github(language_choose),
            "هب": lambda: self.open_github(language_choose),
            "هاب": lambda: self.open_github(language_choose),
            "موقع جيت هاب": lambda: self.open_github(language_choose),
            "جيت هاب": lambda: self.open_github(language_choose),
        # Facebook
            "فيسبوك": lambda: self.open_facebook(language_choose),
            "فيس": lambda: self.open_facebook(language_choose),
            "بوك": lambda: self.open_facebook(language_choose),
            "facebook": lambda: self.open_facebook(language_choose),
            "Facebook": lambda: self.open_facebook(language_choose),
            "Face": lambda: self.open_facebook(language_choose),
            "face": lambda: self.open_facebook(language_choose),
            "book": lambda: self.open_facebook(language_choose),
            "Book": lambda: self.open_facebook(language_choose),
        # YouTube
            "فتح يوتيوب": lambda: self.open_youtube(language_choose),
            "open youtube": lambda: self.open_youtube(language_choose),
        # ChatGPT
            "chat": lambda: self.open_chatgpt(language_choose),
            "Chat": lambda: self.open_chatgpt(language_choose),
            "Chatgpt": lambda: self.open_chatgpt(language_choose),
            "Gpt": lambda: self.open_chatgpt(language_choose),
            "gpt": lambda: self.open_chatgpt(language_choose),
            "شات جي بي تي": lambda: self.open_chatgpt(language_choose),
            "شات جى بى تى": lambda: self.open_chatgpt(language_choose),
            "جى بى": lambda: self.open_chatgpt(language_choose),
            "بى تى": lambda: self.open_chatgpt(language_choose),
        # Bye commands
            "bye": lambda: self.say_bye(language_choose, myName),
            "سلام": lambda: self.say_bye(language_choose, myName),
            "good night": lambda: self.say_bye(language_choose, myName),
            "thank you": lambda: self.say_bye(language_choose, myName),
            "exit": lambda: self.say_bye(language_choose, myName),
            "مع السلامه": lambda: self.say_bye(language_choose, myName),
            "باى باى": lambda: self.say_bye(language_choose, myName),
        # Data today
            "انهارده يوم اي": lambda: self.date_today(language_choose),
            "اليوم": lambda: self.date_today(language_choose),
            "today": lambda: self.date_today(language_choose),
            "انهارده اي": lambda: self.date_today(language_choose),
            "يوم": lambda: self.date_today(language_choose),
        # Translations
            "تترجملي": lambda: self.translate(language_choose),
            "اترجم": lambda: self.translate(language_choose),
            "Translate": lambda: self.translate(language_choose),
            "translate": lambda: self.translate(language_choose),
            "ترجم": lambda: self.translate(language_choose),
        #thanks
           "شكرا": lambda: self.speak(text="العفو",language=language_choose),
            "شكرا جزيلا": lambda: self.speak(text="العفو",language=language_choose),
            "شكرا لك": lambda: self.speak(text="العفو",language=language_choose),
            "شكرا لكم": lambda: self.speak(text="العفو",language=language_choose),
            "thanks": lambda: self.speak(text="you are welcome",language=language_choose),
            "thanks a lot": lambda: self.speak(text="you are welcome",language=language_choose),
            "thank you very much": lambda: self.speak(text="you are welcome",language=language_choose),
            "thank you": lambda: self.speak(text="you are welcome",language=language_choose),
        #Editor
            "من صنعك": lambda: self.editor(language_choose),
            "من انشائك": lambda: self.editor(language_choose),
            "who invented you": lambda: self.editor(language_choose),
            "who made you": lambda: self.editor(language_choose),
            " من انشاك": lambda: self.editor(language_choose),
            " من اخترعك": lambda: self.editor(language_choose), 
            "مين الي عملك": lambda: self.editor(language_choose),
        #screenshots
            "تصوير الشاشه": lambda: self.screenshot(language =language_choose),
            "تصوير الشاشة": lambda: self.screenshot(language =language_choose),
            "صوره الشاشه": lambda: self.screenshot(language =language_choose),
            "سكرين شوت": lambda: self.screenshot(language =language_choose),
            "سكرين": lambda: self.screenshot(language =language_choose),
            "شوت": lambda: self.screenshot(language =language_choose),
            "take a screenshot": lambda: self.screenshot(language =language_choose),
            "screenshot": lambda: self.screenshot(language =language_choose),
        #Instagram
             "Instagram": lambda: self.open_instagram(language_choose),
            "instagram": lambda: self.open_instagram(language_choose),
            "انستا": lambda: self.open_instagram(language_choose),
            "انتجرام": lambda: self.open_instagram(language_choose),
            "انستغرام": lambda: self.open_instagram(language_choose),
            "انستقرام": lambda: self.open_instagram(language_choose),
        # البحث في جوجل
            "ابحث في الانترنت":lambda: self.Search_In_Google,
            "ابحث في جوجل":lambda: self.Search_In_Google,
            "جوجل": lambda:self.Search_In_Google,
            "google": lambda:self.Search_In_Google,
            "search in google about": lambda:self.Search_In_Google,
            "search about": lambda:self.Search_In_Google,
            "searching in google": lambda:self.Search_In_Google,
            "search in google about": lambda:self.Search_In_Google,
        # Search in YouTube
            "ابحث في اليوتيوب": lambda:self.search_youtube,
            "شغلي": lambda:self.search_youtube,
            "اغنية": lambda:self.search_youtube,
            "اغنيه": lambda:self.search_youtube,
            "ابحث في يوتيوب عن":lambda: self.search_youtube,
            "search in youtube": lambda:self.search_youtube,
            "open in youtube": lambda:self.search_youtube,
            "شغلى": lambda:self.search_youtube,
            "شغل":lambda: self.search_youtube,
        }
    def speak(self, text, language):
        lang_code = 'ar' if language == '1' else 'en'
        myobj = gTTS(text=text, lang=lang_code, slow=False)
        myobj.save("audio.mp3")
        playsound("audio.mp3")
        os.remove("audio.mp3")
    def listen(self, language):
        while True:
            try:
                with sr.Microphone() as source:
                    print("Listening..." if language == '2' else " تحدث ...")
                    audio = My_voice.listen(source)
                    global_text = My_voice.recognize_google(audio, language="en-US" if language == '2' else "ar-EG")
                    print("You said: " + global_text if language == '2' else "قلت: " + global_text)
                    return global_text
            except sr.UnknownValueError:
                self.speak("Sorry, I can't understand what you said. " if language == '2' else "اسف لم استطع فهم ما تقول", language)
    def respond_to_speech(self, text, language):
        for keyword, action in self.commands.items():
            if keyword in text:
                action(text)
                return
        self.speak("Sorry, I didn't understand. Please try again." if language == '2' else "عذرًا، لم أفهم. يرجى المحاولة مرة أخرى.", language)
        command = self.listen(language)
        self.respond_to_speech(command, language)
    def search_youtube(self, text):
        search_quer = text.replace("ابحث في يوتيوب عن ", "").replace("شغلي", "").replace("اغنية", "").replace("اغنيه", "").replace("search in youtube", "").replace("open in youtube", "").replace("شغلى", "").replace("شغل", "")
        pywhatkit.playonyt(search_quer)
        self.speak("done", language_choose)
    def Search_In_Google(self, text):
        search_query = text.replace("ابحث في جوجل عن ", "").replace("جوجل", "").replace("ابحث في الانترنت", "").replace("search in google", "").replace("search about ", "").replace("search in google about ", "").replace("search ", "").replace("search in google about ", "").replace("search ","")
        
        pywhatkit.search(search_query)
        self.speak("done", language_choose)
    def open_instagram(self, language):
        self.speak("لحظه واحدة،" if language == '1' else "Just a moment, opening instagram now", language)
        webbrowser.open_new_tab("https://www.instagram.com/mohamed.a.abdelmoat_17.5.2002/")
    def screenshot(self,language ):
        self.speak("حاضر" if language == '1' else "OK", language)
        pyautogui.hotkey("Win","prtsc") 
    def translate(self, language):
        if language == '1':
            self.speak("قول ما تريد ان يترجم ...", language)
            source_language = 'ar'
            target_language = 'en'
            text = self.listen(language)
            translated_text = translator.translate(text, src=source_language, dest=target_language).text
            self.speak(translated_text, language=1)
            print(f"Translated text: {translated_text}")
        elif language == '2':
            self.speak("tell me what you want to translate ...", language)
            source_language = 'en'
            target_language = 'ar'
            text = self.listen(language)
            translated_text = translator.translate(text, src=source_language, dest=target_language).text
            lang_code = 'ar' if language == '2' else 'en'
            myobj = gTTS(text=translated_text, lang=lang_code, slow=False)
            myobj.save("audio.mp3")
            playsound("audio.mp3")
            os.remove("audio.mp3")
            print(f"Translated text: {translated_text}")
    def date_today(self, language):
     now = datetime.now()
    # الحصول على اسم اليوم
     day_name = now.strftime('%A')
    # الحصول على التاريخ بصيغة يوم-شهر-سنة
     date_text = now.strftime('%d-%m-%Y')
    # تحويل اسم اليوم من الإنجليزية إلى العربية إذا كان باللغة العربية
     if language == '1':  # العربية
        day_names = {
            'Monday': 'الاثنين',
            'Tuesday': 'الثلاثاء',
            'Wednesday': 'الأربعاء',
            'Thursday': 'الخميس',
            'Friday': 'الجمعة',
            'Saturday': 'السبت',
            'Sunday': 'الأحد'
        }
        day_name_arabic = day_names.get(day_name, day_name)
        message = f"اليوم هو {day_name_arabic} الموافق {date_text}"
        self.speak(message, language)
        print(day_name_arabic, date_text)
     elif language == '2':  # الإنجليزية
        message = f"Today is {day_name}, and the date is {date_text}"
        self.speak(message, language)
        print(day_name, date_text)
    def open_youtube(self, language):
        self.speak("لحظه واحدة،" if language == '1' else "Just a moment, opening YouTube now", language)
        webbrowser.open_new_tab("https://www.youtube.com")
    def open_chatgpt(self, language):
        self.speak("لحظه واحدة،" if language == '1' else "Just a moment, opening ChatGPT now", language)
        webbrowser.open_new_tab("https://chatgpt.com/")
    def say_bye(self, language, myName):
        self.speak(f"سلام يا {myName}" if language == '1' else f"Goodbye {myName}", language)
        exit()
    def open_github(self, language):
        self.speak("لحظه واحدة،" if language == '1' else "Just a moment, opening GitHub now", language)
        webbrowser.open_new_tab("https://github.com/")
    def open_facebook(self, language):
        self.speak("لحظه واحدة،" if language == '1' else "Just a moment, opening Facebook now", language)
        webbrowser.open_new_tab("https://www.facebook.com/MohamedAhmedAbdelmoati1752002")
    def show_time(self, language):
        now = datetime.now()
        time_format = '%I:%M:%S %p' if language == '2' else '%I:%M:%S %p'.replace('AM', 'صباحاً').replace('PM', 'مساءً')
        time_text = now.strftime(time_format)
        self.speak(f"الوقت الحالي هو {time_text}" if language == '1' else f"The current time is {time_text}", language)
        print(time_text)
    def open_terminal(self, language):
        self.speak("حاضر" if language == '1' else "OK", language)
        pyautogui.hotkey("ctrl", "alt", "t")
    def who_am_i(self, language, myName):
        self.speak(f"انت {myName}" if language == '1' else f"You are {myName}", language)
    def editor(self, language):
        self.speak("انشائني الطالب محمد احمد عبد المعطي طالب في كلية الهندسة جامعة حلوان " if language == '1' else "A student in the Faculty of Engineering at Helwan University, his name is Mohamed Ahmed Abdelmoti", language=language_choose)
# تشغيل الكود
if __name__ == "__main__":
    language_choose = input("Choose language (1 for Arabic, 2 for English):\n ")

    alexa = Alexa()

    if language_choose in ['1', '2']:
        if language_choose == '1':
            alexa.speak("ما اسمك", language_choose)
            myName = alexa.listen(language_choose)
            alexa.speak(f"مرحبا {myName}", language_choose)
            alexa.speak("كيف يمكنني مساعدتك ", language_choose)
        elif language_choose == '2':
            alexa.speak("What is your name?", language_choose)
            myName = alexa.listen(language_choose)
            alexa.speak(f"How can I help you, {myName}?", language_choose)

        while True:
            command = alexa.listen(language_choose)
            alexa.respond_to_speech(command, language_choose)
            if language_choose == '1':
                alexa.speak("هل تحتاج إلى مساعدة .", language_choose)
            elif language_choose == '2':
                alexa.speak(f"Do you want anything else, {myName}?", language_choose)
























# import speech_recognition as sr
# from gtts import gTTS
# from playsound import playsound
# import os
# from datetime import datetime
# import pyautogui

# # تعريف كائن التعرف على الصوت
# My_voice = sr.Recognizer()

# class Alexa:
#     def __init__(self):
#         self.commands = {
#             # Time commands
#             "الساعه": lambda: self.Time(language_choose),
#             "الساعة": lambda: self.Time(language_choose),
#             "clock": lambda: self.Time(language_choose),
#             "time": lambda: self.Time(language_choose),
#             "الوقت": lambda: self.Time(language_choose),
#             "الآن": lambda: self.Time(language_choose),
#             "الوقت الآن": lambda: self.Time(language_choose),
#             # Terminal commands
#             "ترمنال": lambda: self.openterminal(language_choose),
#             "ترمينال": lambda: self.openterminal(language_choose),
#             "terminal": lambda: self.openterminal(language_choose),
#             "open terminal": lambda: self.openterminal(language_choose),
#             "فتح تيرمينال": lambda: self.openterminal(language_choose),
#             "command line": lambda: self.openterminal(language_choose),
#             "سطر الأوامر": lambda: self.openterminal(language_choose),
#             "تيرمنال": lambda: self.openterminal(language_choose),
#             "تيرمينال": lambda: self.openterminal(language_choose),
#             "فتح ترمينال": lambda: self.openterminal(language_choose),
#             "سطر الاوامر": lambda: self.openterminal(language_choose),
#         }

#     def Speak(self, text, language):
#         """تحويل النص إلى كلام وتشغيله"""
#         if language == '1':
#             myobj = gTTS(text=text, lang="ar", slow=False)
#         elif language == '2':
#             myobj = gTTS(text=text, lang="en", slow=False)
#         else:
#             print("Invalid language choice.")
#             return

#         # حفظ الملف الصوتي وتشغيله
#         myobj.save("audio.mp3")
#         playsound("audio.mp3")
#         os.remove("audio.mp3")

#     def listen(self, language):
#         """استماع للأوامر الصوتية وتحويلها إلى نص"""
#         global_text = ""
#         while True:
#             if language == '1':
#                 with sr.Microphone() as source:
#                     print("اتفضل تحدث ...")
#                     audio = My_voice.listen(source)
#                     print("بضبط الجمل ...")
#                     try:
#                         global_text = My_voice.recognize_google(audio, language="ar-EG")
#                         print("قلت: " + global_text)
#                         break
#                     except sr.UnknownValueError:
#                         print("اسف لم استطع فهم ما تقول. يرجى المحاولة مرة أخرى.")
#                         self.Speak("اسف لم استطع فهم ما تقول. يرجى المحاولة مرة أخرى.", '1')
#                     except sr.RequestError:
#                         print("حدث خطأ في الاتصال. يرجى المحاولة مرة أخرى.")
#             elif language == '2':
#                 with sr.Microphone() as source:
#                     print("Listening...")
#                     audio = My_voice.listen(source)
#                     print("Recognizing...")
#                     try:
#                         global_text = My_voice.recognize_google(audio, language="en-US")
#                         print("You said: " + global_text)
#                         break
#                     except sr.UnknownValueError:
#                         print("Sorry, I can't understand what you said. Please try again.")
#                         self.Speak("Sorry, I can't understand what you said. Please try again.", '2')
#                     except sr.RequestError:
#                         print("There was an error with the speech recognition service. Please try again.")
#             else:
#                 print("Invalid choice. Please select '1' for Arabic or '2' for English.")
#                 break
#         return global_text

#     def Respond_to_Speech(self, text, language):
#         """الاستجابة للأوامر الصوتية"""
#         if language in ['1', '2']:
#             for keyword, action in self.commands.items():
#                 if keyword in text:
#                     action()
#                     return
#             self.Speak("Sorry, I didn't understand. Please try again.", language)
#             command = self.listen(language)
#             self.Respond_to_Speech(command, language)

#     def Time(self, language):
#         """إعطاء الوقت الحالي بصوت"""
#         now = datetime.now()
#         if language == '1':
#             arabic_time = now.strftime('%I:%M:%S %p').replace('AM', 'صباحاً').replace('PM', 'مساءً')
#             self.Speak(f"الوقت الحالي هو {arabic_time}", '1')
#             print(f"{arabic_time}")
#         elif language == '2':
#             english_time = now.strftime('%I:%M:%S %p')
#             self.Speak(f"The current time is {english_time}", '2')
#             print(f"The current time is {english_time}")

#     def openterminal(self, language):
#         """فتح ترمينال"""
#         if language == '1':
#             self.Speak("حاضر", '1')
#             pyautogui.hotkey("ctrl", "alt", "t")
#         elif language == '2':
#             self.Speak("OK", '2')
#         pyautogui.hotkey("ctrl", "alt", "t")

# # تشغيل الكود
# if __name__ == "__main__":
#     language_choose = input("Choose language (1 for Arabic, 2 for English):\n ")

#     alexa = Alexa()

#     if language_choose == '1':
#         alexa.Speak("ما اسم حضرتك", language_choose)
#         print("ما اسم حضرتك")
#         myName = alexa.listen(language_choose)
#         alexa.Speak(f"مرحبا {myName}", language_choose)
#         alexa.Speak("كيف يمكنني مساعدتك اليوم", language_choose)
#         print("كيف يمكنني مساعدتك اليوم")
#         command = alexa.listen(language_choose)

#     elif language_choose == '2':
#         alexa.Speak("What is your name?", language_choose)
#         print("What is your name?")
#         myName = alexa.listen(language_choose)
#         alexa.Speak(f"How can I help you, {myName}?", language_choose)
#         print("How Can I help You?")
#         command = alexa.listen(language_choose)

#     if command:
#         while True:
#          alexa.Respond_to_Speech(command, language_choose)
#          if language_choose == '1':
#           alexa.Speak("هل تريد شئ اخر", language_choose)
#           print("هل تريد شئ اخر")
#           command = alexa.listen(language_choose)
 
#          elif language_choose == '2':
#           alexa.Speak(f"do you want anything else, {myName}?", language_choose)
#           print("do you want anything else, {myName}?", language_choose)
#           command = alexa.listen(language_choose)
