# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 04:15:23 2021

@author: UBTOHTS
"""

import sys
import re
import time
import datetime

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchWindowException, NoAlertPresentException, NoSuchFrameException, NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException
from PyQt5 import QtTest
from main import MainWindow
import sqlite3
class antar_yami2(MainWindow):
    def ubtohts(self, enable):
        if enable:
            global new_min_join
            global new_min_leave
            global new_min_join_lab
            global new_min_leave_lab
            global new_max_thread
            
            min_join = self.ui.c_lec_join.text()
            min_leave = self.ui.c_lec_leave.text()
            min_join_lab = self.ui.c_lec_join_2.text()
            min_leave_lab = self.ui.c_lab_leave.text()
            max_thread = self.ui.c_thread_time.text()
            
            if re.search('^\d\d.*', min_join):
                new_min_join = int(min_join)
            elif min_join == '':
                new_min_join = 10
            else:
                new_min_join = 10
            
            if re.search('^\d\d.*', min_leave):
                new_min_leave = int(min_leave)
            elif min_join == '':
                new_min_leave = 10
            else:
                new_min_leave = 7
                
            if re.search('^\d\d.*', min_join_lab):
                new_min_join_lab = int(min_join_lab)
            elif min_join == '':
                new_min_join_lab = 5
            else:
                new_min_join_lab = 5
                
            if re.search('^\d\d.*', min_leave_lab):
                new_min_leave_lab = int(min_leave_lab)
            elif min_join == '':
                new_min_leave_lab = 3
            else:
                new_min_leave_lab = 3
                
                
            if re.search('^\d\d.*', max_thread):
                new_max_thread = int(max_thread)
            elif min_join == '':
                new_max_thread = 15
            else:
                new_max_thread = 15
                
#--------------------------------------------------------------------------------------------------------first close driver if its open
            try:
                driver.close()
            except:
                pass
#--------------------------------------------------------------------------------------------------------outputshown method
            self.ui.c_error.clear()
            def outputshown(x):                
                self.ui.c_error.append(x)

#--------------------------------------------------------------------------------------------------------second grab data from database
            
            def getdata(self):
                global uniqueusename
                global uniqueusepaswword
                getdata = []
                try:
                    conn = sqlite3.connect(self.resource_path('sqldata/epassdata.db'))
                    c = conn.cursor()
                    sqlstr = 'select * from students'

                    results = c.execute(sqlstr)                    
                    for row in results:
                        getdata.append(row)
                        
                    try:
                        uniqueusename = tuple(getdata[0])[0]
                        uniqueusepaswword = tuple(getdata[0])[1]
                        if len(uniqueusename) and len(uniqueusepaswword) != 0:
                            return True
                        elif len(uniqueusename) and len(uniqueusepaswword) == 0:
                            uniqueusename = tuple(getdata[1])[0]
                            uniqueusepaswword = tuple(getdata[1])[1]
                            if len(uniqueusename) and len(uniqueusepaswword) == 0:
                                print('second field is also empty')
                                return False
                        else:
                            return False
                    except:
                        print('idk something going wrong')
                        outputshown("BUDDY YOUR PASSWORD AND DATABASE FIELD ARE EMPTY\nPLEASE CLICK ON \"ID_PASS\" MENU AND ENTER YOUR DATA THEIR")
                    c.close()
                    conn.close()
                except Exception as E:
                    print(E)
                    return False
                except:
                    outputshown("HMMM, SOMETHING IS GROING WRONG\nI THINK YOU FORGOT TO BUILT USERNAME AND PASSWORD DATABSE")
                    return False

#--------------------------------------------------------------------------------------------------------login

            def login(self):
                global driver
                opt = Options()
                opt.add_argument("--disable-infobars")
                opt.add_argument("start-maximized")
                opt.add_argument("--disable-extensions")
                # Pass the argument 1 to allow and 2 to block
                opt.add_experimental_option("prefs", { \
                    "profile.default_content_setting_values.media_stream_mic": 1, 
                    "profile.default_content_setting_values.media_stream_camera": 1,
                    "profile.default_content_setting_values.geolocation": 2, 
                    "profile.default_content_setting_values.notifications": 1 
                  })
                driver = webdriver.Chrome(options=opt, executable_path=self.resource_path('driver/chromedriver.exe'))
                try:
                    
                    driver.get('https://teams.microsoft.com')
                    QtTest.QTest.qWait(5000)
                    WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))
                    if("login.microsoftonline.com" in driver.current_url):
                        emailField = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'i0116')))
                        emailField.click()
                        emailField.send_keys(uniqueusename)
                        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click() #Next button
                        
                        try:
                            driver.find_element_by_id('usernameError')
                            print("please enter valid email adress")
                            return False
                        except:
                            pass
                            
                        passwordField = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'i0118')))
                        passwordField.click()
                        passwordField.send_keys(uniqueusepaswword)
                        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()
                    
                        try:
                            driver.find_element_by_id('passwordError')
                            print("please enter valid password")
                            return False
                        except:
                            pass
            
                        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click() #remember login
                        QtTest.QTest.qWait(5000)
                        outputshown('SUCESSFULLY LOGIN')
                except Exception as e:
                    print("Error:-\t",e)
                    print("Somthing bad happen at login time")
                    return False
                except WebDriverException or TimeoutException or NoSuchWindowException or NoAlertPresentException or NoSuchFrameException or NoSuchElementException or ElementNotVisibleException or ElementNotSelectableException:
                    outputshown("WHY YOU ASSHOLE SHUT THE CHROME!!!")
                return True

#--------------------------------------------------------------------------------------------------------lec finder
            
            def lec_finder(self):
                global driver
                
                try:
                    conn = sqlite3.connect(self.resource_path('sqldata/lectable.db'))
                    c = conn.cursor()
                    sql = ('select * from lecdata')
                    grab_result = c.execute(sql)
                    #------------------------------------------------------------store all the mactching result in the list
                    print(str(self.lec))
                    for row in grab_result:
                        if str(row[1]) == str(self.lec):
                            lec_name = row[2]
                            lec_classname = row[3]
                            
                    print(lec_name, lec_classname)
                    
                    c.close()
                    conn.close()
                except:
                    print('lec database not load successful')
                    outputshown('MS LECTURE NAME DATABASE NOT LOADED\nOR MAY BE NAME SAVE IN DATABASE ARE NOT MATCH WITH THE INPUT')
        
                #---------------------------------------------------------------------------------------grab all the class + sub class list
                QtTest.QTest.qWait(18000)
                classes_available = driver.find_elements_by_class_name("name-channel-type")
        
                def classes_len_checker(classes_available):
                    if not len(classes_available) > 0:
                        return False
                    return True
        
                while not classes_len_checker(classes_available):
                    # print("inner page not load succesfull")  #uncomment
                    QtTest.QTest.qWait(3500)
                    classes_available = driver.find_elements_by_class_name("name-channel-type")
                    classes_len_checker(classes_available)
                #------------------------------------------------------------------------------------------------ click on your input class
                pr_class_name = lec_name
                prcl_classname = lec_classname
                
                def sub_class_clicker():
                    for i in range(len(classes_available)):
                        try:
                            class_name = classes_available[i].get_attribute('innerHTML').lower()
                            subclass_name = classes_available[i+1].get_attribute('outerHTML').lower()
                            print(f"its classname\n{class_name}")
                            if pr_class_name.lower() in classes_available[i].get_attribute('innerHTML').lower():
                                class_name = re.findall('">(.*)</', class_name)
                                print("its subclassname",subclass_name, "click sucessfully")
                                if 'clc.isk2channellie(channel)' in subclass_name:
                                    for z in range(i+1, len(classes_available)):
                                        subclass_name = classes_available[z].get_attribute('innerHTML').lower()
                                        print("subcalssname",subclass_name)
                                        if 'class="truncate"' in classes_available[z].get_attribute('innerHTML').lower():
                                            subclass_name = re.findall('">(.*)</', subclass_name)
                                            print("subcalssname",subclass_name)
                                            if str(subclass_name[0]) == prcl_classname:
                                                classes_available[z].click()
                                                print(f"{subclass_name}0 click sucessful ")
                                                return True
                        except IndexError or StaleElementReferenceException:
                            pass
                
                def class_sub_clicker():
                    QtTest.QTest.qWait(2000)
                    classes_available = driver.find_elements_by_class_name("name-channel-type")
                    QtTest.QTest.qWait(2000)
                    for i in range(len(classes_available)):
                        try:
                            class_name = classes_available[i].get_attribute('innerHTML').lower()
                            subclass_name = classes_available[i+1].get_attribute('outerHTML').lower()
                            print(f"its classname\n{class_name}")
                            if pr_class_name.lower() in classes_available[i].get_attribute('innerHTML').lower():
                                class_name = re.findall('">(.*)</', class_name)
                                classes_available[i].click()
                                print(f"{class_name} click successfull")
                                QtTest.QTest.qWait(2000)
                                classes_available = driver.find_elements_by_class_name("name-channel-type")
                                QtTest.QTest.qWait(2000)
                                subclass_name = classes_available[i+1].get_attribute('outerHTML').lower()
                                
                                if 'clc.isk2channellie(channel)' in subclass_name:
                                    for z in range(i+1, len(classes_available)):
                                        subclass_name = classes_available[z].get_attribute('innerHTML').lower()
                                        print(subclass_name)
                                        if 'class="truncate"' in classes_available[z].get_attribute('innerHTML').lower():
                                            subclass_name = re.findall('">(.*)</', subclass_name)
                                            print(subclass_name)
                                            if str(subclass_name[0]) == prcl_classname:
                                                classes_available[z].click()
                                                print(f"{subclass_name}1 click sucessful ")
                                                return True
                        except IndexError or StaleElementReferenceException:
                            pass
                def answer_checker():
                    try:
                        print("try block running")
                        result = sub_class_clicker()
                        if result == None:
                            result1 = class_sub_clicker()
                            if result1 == True:
                                return True
                        elif result == True:
                            return True
                    except:
                        print("except block running")
                        return False
                raja = answer_checker()
                print(raja)
                
                if raja == True:
                    outputshown("ENTERING IN THE CLASS LOBBY AND FIND DOES CLASS AE START OR NOT")
                
                return True

#--------------------------------------------------------------------------------------------------------condition checker
            
            def condition_chekcer(self):
                
                z = new_max_thread
                tt = round(int(new_max_thread)/3)
                
                
                
                outputshown("15 MINS SEARCHING IF THERE IS NOT ANY CLASS THEN AUTOMATICALLY LOGOUT")
                def join_button_checker():
                    start = time.time()
                    QtTest.QTest.qWait(5000)
                    while (time.time() - start < int(tt)):
                        print(time.time()-start)
                        for i in range(100):
                            try:
                                no = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/middle-messages-stripe/div/messages-header/div[2]/div/message-pane/div/div[1]/div/div/message-list/div/virtual-repeat/div').text
                                no = no.split('\n')
                                if 'Join' in no:
                                    if 'Meeting now' in no:
                                        print("le bhai ho gaya lec chalu, ready ho jao")
                                        outputshown('YOUR LEC IS START BUDDY')
                                        return False
                                print("Metting is not start right now") #uncomment pls
                            except Exception as e:
                                Error = str(e)
                                if Error.startswith("Message"):
                                    print("funcation restart himself something wrong check pls")
                                    time.sleep(10)
                            i += 1
            #             print(i)
                join_button_checker()
                print("no of people start")
                def no_of_people_checker():
                    start = time.time()
                    QtTest.QTest.qWait(5000)
                    while (time.time() - start < int(tt)):
                        print(time.time()-start)
                        for i in range(100):
                            no = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/middle-messages-stripe/div/messages-header/div[2]/div/message-pane/div/div[1]/div/div/message-list/div/virtual-repeat/div').text
                            no = no.split('\n')
            #                 print(no)
                            for i in range(len(no)):
                                try:
                                    if re.findall('^\+.*', no[i]):
                #                         print(re.findall('^\+.*', no[i]))
                #                         print(no[i+1])
                                        if no[i+1] == 'Join':
                                            f_no = no[i]
                                            f_no = int(str(f_no[1:]))
                                            print(f_no) #uncomment
                #------------------------------------------------------------------------------------------ if you want to change no of people                     
                                            if f_no >= new_min_join:
                                                print("people are more, class with more student")
                                                outputshown('10+ STUDENTS IN THE CLASS SO I START THE MEETING')
                                                return False
                                            else:
                                                print("people are less, class with less student")
                                                outputshown('HERE ARE LESS THAN 10+ STUDENTS SO I AM NOT STARTING MEETING')
                                except IndexError:
                                    QtTest.QTest.qWait(5000)
                                    no_of_people_checker()
                                except Exception as E:
                                    print("hii i am error,", E)
                                except:
                                    pass
                                    
                                    
                            i += 1
                no_of_people_checker()
                print('join button start')
                def join_button_checker():
                    i = 0
                    QtTest.QTest.qWait(5000)
                    start = time.time()
                    while (time.time() - start < int(tt)):
                        print(time.time()-start, "its me time wala")
                        for i in range(1):
                            try:
                                joinbtn = driver.find_element_by_class_name("ts-calling-join-button")
                                joinbtn.click()
                                print("hurrreh class he bhau")
                                return False
                            except:
                                QtTest.QTest.qWait(60000)
                            i += 1
                fuq = join_button_checker()
                
                if fuq != False:
                    outputshown("I AM SHUT THE BROWSER COZ, I AM NOT FOUND ANY MEETING STILL, LAST 15 MINS")
                    return False
                if fuq != None:
                    outputshown("ENTERING IN THE CLASS PLS DONT TOUCH FOR A WHILE\nBOT AUTOMATICALLY TURN OFF EVERYTHING")

#--------------------------------------------------------------------------------------------------------class joining
                    
            def class_joining(self):
                self.ui.c_error.clear()
                try:
                    QtTest.QTest.qWait(5000)
                    webcam = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')
                    microphone = driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]')
                    def sweta_checker(webcam, microphone):
                        if(webcam.get_attribute('title')=='Turn camera off'):
                            webcam.click()
                            QtTest.QTest.qWait(2000)
                            if(microphone.get_attribute('title')=='Mute microphone'):
                                microphone.click()
                                print("Okk, Mike and Webcam are Turn Off so you are not next shweta")
                                outputshown("OK, MIC AND WEBCAM IS OFF SO YOU DON'T BECOME SHWETA")
                                return True
                            elif(webcam.get_attribute('title')=='Turn camera on') & (microphone.get_attribute('title')=='Unmute microphone'):
                                print("Okk, Mike and Webcam are Turn Off so you are not next shweta")
                                outputshown("OK, MIC AND WEBCAM IS OFF SO YOU DON'T BECOME SHWETA")
                                return True
                        else:
                            print(webcam.get_attribute('title'))
                            print(microphone.get_attribute('title'))
                            outputshown("OK, MIC AND WEBCAM IS OFF SO YOU DON'T BECOME SHWETA")
                            return True

                    while sweta_checker(webcam, microphone):
                        if(webcam.get_attribute('title')=='Turn camera on') & (microphone.get_attribute('title')=='Unmute microphone'):
                            print("yooo bou i am coming")
                            joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
                            joinnowbtn.click()
                            print('finally apun ne click kiya bhau')
                            return True
                        else:
                            sweta_checker(webcam, microphone)
        
                except WebDriverException or TimeoutException or NoSuchWindowException or NoAlertPresentException or NoSuchFrameException or NoSuchElementException or ElementNotVisibleException or ElementNotSelectableException:
                    print("Webbrowser not load, May be coz of net issue\nKindly check your network")
                    outputshown("WEBBROWSER NOT LOAD, MAY BE COZ OF NET ISSUE\nKINDLY CHECK YOUR NETWORK")
                    return False
                return True

#--------------------------------------------------------------------------------------------------------leave by people
                    
            def leave_by_people(self):
                print("entering in leave by people ")
                self.ui.c_error.clear()
                def chat_section_opener():
                    try:
                        button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'roster-button')))
                        driver.execute_script("arguments[0].click();", button)
                        return True
                    except:
                        return False
        
                def heavy_driver():
                    while not chat_section_opener():
                        try:
                            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'ts-calling-screen'))).click()
                        except:
                            leave_by_people(self)
                        chat_section_opener()
                    return True
                
                if heavy_driver() == True:
                    pass
                        
                def leave_checker():
                    try:
                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="teams-app-bar"]/ul/li[3]'))).click() #come back to homepage
                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hangup-button"]'))).click()
                        print("I am attending your meeting and Finally i am going to sleep")
                        outputshown(self, "I AM ATTENDING YOUR MEETING AND FINALLY I AM GOING TO SLEEP")
                        QtTest.QTest.qWait(2000)
                        return True
                    except:
                        return False
            
                def aletring():
                    try:
                        no_of_people_info = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-roster/div/div[3]/div/div[1]/accordion/div/accordion-section[2]/div/calling-roster-section/div/div[2]/div/ul'))).text
                        no_of_people_info = no_of_people_info.split('\n')
                        print(f" {no_of_people_info} are present")
                        outputshown(f" {no_of_people_info} ARE PRESENT")
                        if len(no_of_people_info) <= new_min_leave:
            #                     print(len(no_of_people_info))
                            if len(no_of_people_info[0]) == 0:
                                heavy_driver()
                            leave_checker()
                            QtTest.QTest.qWait(2000)
                            return True
                        elif 5 < len(no_of_people_info) <15 :
                            outputshown(f"here are only {len(no_of_people_info)-2}+ students are present")
                        elif 15 < len(no_of_people_info) <25 :
                            outputshown(f"Here are {len(no_of_people_info)-2}+ students are present")
                        elif 25 < len(no_of_people_info) < 50 :
                            outputshown(f"Ohhhhh, Here are {len(no_of_people_info)-2}+ students are present\nMean class instructor are very clear to understabale for students")
                        elif 50 < len(no_of_people_info) < 75 :
                            outputshown(f"OMG!!, Here are {len(no_of_people_info)-5}+ students are present\nBahut garmi ho rahi he bhai A.C chalu karna aaj public jyada lag rahi he..")
                        elif 75 < len(no_of_people_info) < 100 :
                            outputshown(f"What the heck dude!!!, litterly here are {len(no_of_people_info)-2}+ students are present\nI am glad that i am attending this type of big meeting..\nThanks it's my plasure")
                        return False
                    except WebDriverException or TimeoutException or NoSuchWindowException or NoAlertPresentException or NoSuchFrameException or NoSuchElementException or ElementNotVisibleException or ElementNotSelectableException:
                        print("There is button not interacting so retrying to get the button")
                        outputshown("There is button not interacting so retrying to get the button")
                        self.leave_by_people()
                        return False
            
                while not aletring():
                    QtTest.QTest.qWait(120000)
                    aletring()
                print("leaving in leave by people")
                return True

#--------------------------------------------------------------------------------------------------------leave time

            def leave_by_time(self):
                print("entering in leave by time")
                try:
                    e_time = str(datetime.datetime.now())
                    e_min = e_time[-12:-10]
                    e_hour = e_time[-15:-13]
                    e_time = e_hour + ":" + e_min
        
                    datetime2 = datetime.datetime.strptime(self.end_time,"%H:%M")
                    datetime1 = datetime.datetime.strptime(e_time,"%H:%M")
        
                    t_diff = str(datetime2 - datetime1)
                    print(t_diff)
                    while True:
                        if re.search("^-\d.*", t_diff):
                            print("Meeting is end")
                            outputshown('YOUR MEETING IS END')
                            break
                        elif re.search("^\d{1}|\d{2}:\d{1}|\d{2}:\d{1}|\d{2}", t_diff):
                            print(f"There is time, so i am sleep for {t_diff} hour")
                            QtTest.QTest.qWait((int(t_diff[-5:-3]) + int(t_diff[-len(t_diff):-6]) *60)*60000)
                            print('OK, as your instructing time i am end this meet')
                            outputshown('AS YOUR INSTRUCTION I AM ATTEND THE MEETING AND NOW I AM GOING TO SLEEP')
                            break
                        else:
                            print("ye time me ku6 locha he re bawa")
                            outputshown('THERE IS SOMETHING PROBLEM IN TIMES')
                            return False
                        return True
                except ValueError:
                    print("Providing time is not valid")
                    outputshown("PROVIDED ENDING TIME IS NOT RIGHT")
                    return False
                print("laving laeve by time")
            def auotmsboat(lecturename, starttimeoflec, endtimeoflec):
        
                #-----------------------------------------------------------------------------initilize all the predefine value----            
                    
                self.start_time = starttimeoflec
                self.lec = lecturename
                self.end_time = endtimeoflec
                
                #------------------------------------------------------------------------------------------------------                

                while True:
                    t1_time = str(datetime.datetime.now())
                    t1_min = t1_time[-12:-10]
                    t1_hour = t1_time[-15:-13]
                    t1_time = t1_hour + ":" + t1_min

                    ghost = getdata(self)
                    if ghost == True:
                        pass
                    elif ghost == False:
                        break
                    try:
                        if("teams.microsoftonline.com" in driver.current_url):
                            pass
                    except:
                        charli = login(self)
                        if charli == True:
                            pass
                        elif charli == False:
                            try:
                                driver.close()
                                break
                            except:
                                print("charli is not is dont want to close ku6 karo")
                                outputshown("SORRY USER SOMETHING BAD HAPPEN AT CLOSING TIME, WHICH I COULD NOT CONTROL SO, PLS SHUT THE APP AND RESTART IT")
                    
                #------------------------------------------------------------------------------------------------------

                    alpha = lec_finder(self)
                    if alpha == True:
                        pass
                    elif alpha == False:
                        try:
                            driver.close()
                            break
                        except:
                            print("alpha is not is dont want to close ku6 karo")
                            outputshown("SORRY USER SOMETHING BAD HAPPEN AT CLOSING TIME, WHICH I COULD NOT CONTROL SO, PLS SHUT THE APP AND RESTART IT")
                #------------------------------------------------------------------------------------------------------
                    rider = condition_chekcer(self)
                    if rider == True:
                        pass
                    elif rider == False:
                        try:
                            driver.close()
                            break
                        except:
                            print("rider is not is dont want to close ku6 karo")
                            outputshown("SORRY USER SOMETHING BAD HAPPEN AT CLOSING TIME, WHICH I COULD NOT CONTROL SO, PLS SHUT THE APP AND RESTART IT")
                        
                    delta = class_joining(self)
                    if delta == True:
                        pass
                    elif delta == False:
                        try:
                            driver.close()
                            break
                        except:
                            print("delta is not is dont want to close ku6 karo")
                            outputshown("SORRY USER SOMETHING BAD HAPPEN AT CLOSING TIME, WHICH I COULD NOT CONTROL SO, PLS SHUT THE APP AND RESTART IT")
                        
                    provider = leave_by_people(self)
                    if provider == True:
                        pass
                    elif provider == False:
                        try:
                            driver.close()
                            break
                        except:
                            print("provider is not is dont want to close ku6 karo")
                            outputshown("SORRY USER SOMETHING BAD HAPPEN AT CLOSING TIME, WHICH I COULD NOT CONTROL SO, PLS SHUT THE APP AND RESTART IT")
                        
                    bravo = leave_by_time(self)
                    if bravo == True:
                        pass
                    elif bravo == False:
                        try:
                            driver.close()
                            break
                        except:
                            print("bravo is not is dont want to close ku6 karo")
                            outputshown("SORRY USER SOMETHING BAD HAPPEN AT CLOSING TIME, WHICH I COULD NOT CONTROL SO, PLS SHUT THE APP AND RESTART IT")
                    

                        
                    t2_time = str(datetime.datetime.now())
                    t2_min = t2_time[-12:-10]
                    t2_hour = t2_time[-15:-13]
                    t2_time = t2_hour + ":" + t2_min
        
                    time2 = datetime.datetime.strptime(t2_time,"%H:%M")
                    time1 = datetime.datetime.strptime(t1_time,"%H:%M")
        
                    totaltime = str(time2 - time1)
                    print(f"So your script take {totaltime} mins")
                    break

            def lecfinder():
                global start_lec_time
                global end_lec_time
                global current_lecture_name
                def cdateandtimefinder():
                    date = datetime.datetime.now()
                    # print(f'current date is {date}')
                    dayname = (date.date().strftime("%A")).lower()
                    print(f'#############################################\nTo day is a {dayname}')
                    
                    c_time = str(datetime.datetime.now())
                    c_min = c_time[-12:-10]
                    c_hour = c_time[-15:-13]
                    c_time = c_hour + ":" + c_min
                    print(f"current time = {c_time}")
                    return dayname, c_time
                
                # -------------------------------------------------------------grab the data from the sql database
                conn = sqlite3.connect(self.resource_path('sqldata/timetablev1.db'))
                c = conn.cursor()
                sql = ('select * from tb where day=?')
                day, ctime = cdateandtimefinder()
                grab_result = c.execute(sql, (day,))
                #------------------------------------------------------------store all the mactching result in the list
                lectimedata = []
                
                for row in grab_result:
                    print(row)
                    new_string = f"{row[0]},{row[1]},{row[2]},{row[3]}"
                    lectimedata.append(new_string)
                # print(lectimedata)
                day_checker = []
                for row in grab_result:
                    if len(row[0]) > 1:
                        day_checker.append(0)
                    else:
                        day_checker.append(1)
                if day_checker.count(0) == len(day_checker):
                    print("bhai aaj koi lec hi nahi he..")
                    outputshown('NOT ANY LEC FOUND TODAY..')
                else:
                    print("wait rukja ..")
                c.close()
                conn.close()
                # day, ctime = cdateandtimefinder()
                # lectimedata = ['WC,03:00,03:59,thursday','IML,06:00,06:20,thursday', 'IAI,06:20,06:59,thursday', 'DIVP,05:55,09:50,thursday']
                #--------------------------------------------------------------now close the sql database
                #-------------------------------------------------------------- start time differnce chacker
                for i in range(len(lectimedata)):
                # for i in range(1):
                    current_lecture_name = str(lectimedata[i].split(',')[0])
                    current_lec_end_time = str(lectimedata[i].split(',')[2])
                    current_lec_start_time = str(lectimedata[i].split(',')[1])
                    print("lec start time", current_lec_start_time)
                    print(current_lecture_name, current_lec_end_time, current_lec_start_time)
                    start_lec_time = datetime.datetime.strptime(str(lectimedata[i].split(',')[1]),"%H:%M")
                    current_time = datetime.datetime.strptime(ctime,"%H:%M")
                    t_diff = str(start_lec_time - current_time)
                    
                    print(f'differnce  = {t_diff}')
                    
                    #finding total len of lecture for seeing how much time are left
                    len_of_lecture = datetime.datetime.strptime(str(lectimedata[i].split(',')[2]),"%H:%M") - datetime.datetime.strptime(str(lectimedata[i].split(',')[1]),"%H:%M")
                    print(f'len_of_lec{len_of_lecture}')
                    len_of_lec_values = re.findall('([\d{1}|\d{2}]:\d\d:\d\d)', str(len_of_lecture))
                    len_of_lec_minute = len_of_lec_values[0][-5:-3]
                    len_of_lec_hour = len_of_lec_values[0][-len(len_of_lec_values[0]):-6]
                    total_lec_mins = ((int(len_of_lec_minute) + int(len_of_lec_hour) *60))
                    
                    print(f"total lec mins:-{total_lec_mins}")
                    
                    
                    values = re.findall('([\d{1}|\d{2}]:\d\d:\d\d)', str(t_diff))
                    minute = values[0][-5:-3]
                    hour = values[0][-len(values[0]):-6]
                    
                    # print(f'min:-{minute}, hour:-{hour}')
                #-------------------------------------------------------------- end time differnce chacker 
                    
                    if re.search('^-\d\s\w.*', t_diff):
                        print("lec end time", str(lectimedata[i].split(',')[2]))
                        end_lec_time = datetime.datetime.strptime(str(lectimedata[i].split(',')[2]),"%H:%M") #lec_end_time
                        t_diff = str(end_lec_time - current_time)
                        print(f"lec end vs cuurent time diff {t_diff}")
                    
                        values = re.findall('([\d{1}|\d{2}]:\d\d:\d\d)', str(t_diff))
                        # print(values)
                        minute = values[0][-5:-3]
                        hour = values[0][-len(values[0]):-6]
                        total_left_mins = ((int(minute) + int(hour) *60))
                        total_waste_mins = int(total_lec_mins) - int(total_left_mins)
                        
                        print(f"total left mins:-{total_left_mins}, total waste mins:- {total_waste_mins}")
                        print(f'min:-{minute}, hour:-{hour}')
                        
                        if re.search('^-\d\s\w.*', t_diff):
                            print('assign a next time\n\n')
                            # return False
                            
                        elif re.search('^([\d{1}|\d{2}]:\d\d:\d\d)', t_diff):
                            if (total_lec_mins - total_waste_mins) > 2:
                                print("#---------------------------------------------\nthere are still some time remaining so i start metting")
                                outputshown("YOU ARE TOO LATE BUT DONT WORY I START METTING IN HIGH SPEED\nFASTER MODE ON DONT TOUCH PC FOR WHILE")
                                auotmsboat(current_lecture_name, current_lec_start_time, current_lec_end_time)
                                # return True
                                
                            else:
                                print("less than 15 mins remaining so i cant start meeting")
                                outputshown('THERE ARE NO MORE TIME LEFT TO ATTEND CURRENT METTING SO I TRY TO FIND NEXT ONE..')
                                # return False
                        else:
                            print("start the current time meeting")
                            # return False
                    elif int(minute) > 45 or int(hour) > 1:
                        print("i cant wait too much so i shut the script")
                        outputshown('I CAN\'T WAIT SO MUCH SO I SHUT THE SCRIPT NOW YOU AGAIN NEED TO CLICK UP')
                        break
                    
                    elif re.search('^(\d{1}|\d{2}:\d\d:\d\d)', t_diff):
                        def meet_stater():
                            try:
                                c_time = str(datetime.datetime.now())
                                c_min = c_time[-12:-10]
                                c_hour = c_time[-15:-13]
                                c_time = c_hour + ":" + c_min
            
                                datetime1 = datetime.datetime.strptime(str(c_time),"%H:%M")
                                datetime2 = datetime.datetime.strptime((current_lec_start_time),"%H:%M")
                                
                                t_diff = str(datetime2 - datetime1)
                                values = re.findall('([\d{1}|\d{2}]:\d\d:\d\d)', str(t_diff))
                                minute = values[0][-5:-3]
                                hour = values[0][-len(values[0]):-6]
            
                                print((t_diff))
                                if re.search("^-\d.*", t_diff):
                                    print("Meeting is starting")
                                    return True
                                elif re.search("^\d{1}|\d{2}:\d{1}|\d{2}:\d{1}|\d{2}", t_diff):
                                    print(f"Okk, at {current_lec_start_time} this time i pass this funcation")
                                    outputshown(f'THERE ARE STILL SOME TIME TO ATTEND LEC\nAT {current_lec_start_time} I START THE MEETING')
                                    QtTest.QTest.qWait((int(minute) + int(hour) *60)*60000)
                                    auotmsboat(current_lecture_name, current_lec_start_time, current_lec_end_time)
                                    print(f'Okk, so {current_lec_start_time} are done and i pass this funcation')
                                    outputshown('UFFF !!! I FINALLY ATTEND YOUR MEETING AND SEARCH FOR THE NEXT ONE..')
                                    return True
                                else:
                                    print("Something bad happen")
                                    return False
                            except ValueError:
                                print("Providing time is not valid")
                                return False
                        meet_stater()
                    else:
                        break
            
            lecfinder()
                




