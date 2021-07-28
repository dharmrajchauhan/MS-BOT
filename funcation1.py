# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 04:19:17 2021

@author: Ubtohts
"""
import sys
import os
import re
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchWindowException, NoAlertPresentException, NoSuchFrameException, NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from PyQt5 import QtTest
from main import MainWindow
from subprocess import CREATE_NO_WINDOW
import sqlite3
# from Exception import UnboundLocalError
# from exceptions import ValueError, TypeError
class UIFunctions(MainWindow):
# =============================================================================
#     starting of main funcation
# =============================================================================
    def weblinkopener(self, enable):
    # =============================================================================
    #   True command given by the ui's page 1 command
    # =============================================================================
        if enable:
            self.ui.textEdit.clear()
            print('Ui send start command')
            # =============================================================================
            #   For output print in the window
            # =============================================================================
            
            def outputshown(y):
                x = y.upper()
                self.ui.textEdit.append(x)          
            try:
                driver.close()
            except:
                pass
            
            # =============================================================================
            #             importing CH_PATH from the app
            # =============================================================================
            
            def resource_path(relative_path):
                try:
                    base_path = sys._MEIPASS
                except Exception:
                    base_path = os.path.dirname(__file__)
                return os.path.join(base_path, relative_path)
            
            # =============================================================================
            #             Data load from user database to see their I'd and Pass
            # =============================================================================
            
            def getdata(self):
                global uniqueusename
                global uniqueusepaswword
                getdata = []
                try:
                    conn = sqlite3.connect(resource_path('sqldata/epassdata.db'))
                    c = conn.cursor()
                    sqlstr = 'select * from students'
                    
                    results = c.execute(sqlstr)                    
                    for row in results:
                        getdata.append(row)
                        
                    try:
                        uniqueusename = tuple(getdata[0])[0]
                        uniqueusepaswword = tuple(getdata[0])[1]
                        
                        if len(uniqueusename) and len(uniqueusepaswword) == 0:
                            uniqueusename = tuple(getdata[1])[0]
                            uniqueusepaswword = tuple(getdata[1])[1]
                                
                            if len(uniqueusename) and len(uniqueusepaswword) == 0:
                                print('second field is also empty')
                        else:
                            pass
                    except:
                        print('idk something going wrong')
                        outputshown("buddy your password and database field are empty\nPlease click on \"id_pass\" menu and enter your data their")
                    c.close()
                    conn.close()

                except Exception as E:
                    print(E)
                except:
                    outputshown("hmmm something is groing wrong\ni think you forgot to built username and password databse")
            
            # =============================================================================
            #       initlize some values to acces global
            # =============================================================================
            getdata(self)                        
            mslink = self.ui.ms_link.text()
            start_time = self.ui.s_time.text()
            print(start_time)
            end_time = self.ui.e_time.text()
            print(end_time)
            print(len(end_time))
            self.start_time = start_time
            self.end_time = end_time
            self.ui.textEdit.clear()

            #------------------------------------------------------------------------------------ GUI CHECKING ------------------------------------------------------            
            # =============================================================================
            #  GUI checking --> given and ms link is right or not --> if right then move to step two/ otherwise/ break the loop and close the app for 
            #  If provide start and end time so they check both are right are not
            # =============================================================================
            
            def time_checker1(time1, time2):
                print('time_checker1 is start')
                try:
                    if re.search('\d\d:\d\d', time1):
                        if re.search('\d\d:\d\d', time2):
                            print("Format of time is right")
                            outputshown("Format of time is right")
                            
                            datetime1 = datetime.datetime.strptime(time1,"%H:%M")
                            datetime2 = datetime.datetime.strptime(time2,"%H:%M")
    
                            time_difference = datetime2 - datetime1
                            values = re.findall('([\d{1}|\d{2}]:\d\d:\d\d)', str(time_difference))
                            minute = values[0][-5:-3]
                            hour = values[0][-len(values[0]):-6]
                            
                            if int(minute) > 0 or int(hour) > 0:
                                print('Providing interval is also right')
                                outputshown("Providing interval is also right")
                                
                                if int(hour) > 2:
                                    print("More thn two hour of meet..\nhii topper..")
                                    outputshown("More thn two hour of meet..\nhii topper..")
                                return True
                            else:
                                print('ye interval me ku6 locha he')
                                outputshown('ye interval me ku6 locha he')
                                return False
                    else:
                        print("hmmm something is groing wrong\nkindly provide input time in 22:10 format")
                        outputshown("hmmm something is groing wrong\nkindly provide input time in 22:10 format")
                        return False
                except Exception as E:
                    print(f"Exception of timechecker-1:- {E}")
            
            # =============================================================================
            #       If user only provide start time            
            # =============================================================================
            
            def time_checker2(time1, time2):
                print('time_checker2 is start')
                try:
                    if re.search('\d\d:\d\d', time1):
                        print("Format of time is right")
                        outputshown("Format of time is right")
                        return True
                    else:
                        print("hmmm something is groing wrong\nkindly provide input time in 22:10 format")
                        outputshown("hmmm something is groing wrong\nkindly provide input time in 22:10 format")
                        return False
                except Exception as E:
                    print(f"Exception of timechecker2:-{E}")
                    return False
            
            # =============================================================================
            #       Its check weather enter ms-link is right or not
            # =============================================================================
            
            def link_varify(link):
                self.ui.textEdit.clear()
                if re.search('^https://teams.microsoft.com/.*', link):
                    self.url = link
                    if len(link) == 235:
                        print("\nohhh, Normal class link he ye to ")
                        outputshown("\nohhh, Normal class link he ye to ")
                    elif len(link) > 235:
                        print("\nhmmm, let me check\nYe apne class ki link to nahi lag rahi\nMatlab bahot tej ho rahe ho ")
                        outputshown("\nhmmm, let me check\nYe apne class ki link to nahi lag rahi\nMatlab bahot tej ho rahe ho ")
                    return True
                else:
                    print("\nkindly check your link again")
                    outputshown("\nkindly check your link again")
                    return False
            
            # =============================================================================
            #       This is main funcation of checking ms-link, time (input-checker loop)
            # =============================================================================
            
            # try:
            #     if len(start_time) > 1 & len(end_time) == 0:
            #         t_checker = time_checker2(start_time,end_time)
            #     elif len(start_time) > 1 & len(end_time) > 1:
            #         t_checker = time_checker1(start_time, end_time)
            #     else:
            #         outputshown("Format of time is not right")
            #     if t_checker & link_varify(mslink) == True:
            #         print("Your meeting is starting right now..")    
            #         outputshown("Your meeting is starting right now..")    
            #     else:
            #         print("\n\n")
            #         outputshown("\n\n")
            # except TypeError:
            #     print("hmmm something is groing wrong\nkindly provide input time in 22:10 format")
            #     outputshown('hmmm something is groing wrong\nkindly provide input time in 22:10 format')
            #     print("\n")
            #     outputshown('\n')
            #     # return False
            # except ValueError or UnboundLocalError:
            #     print("hmmm something is groing wrong\nkindly provide input time in 22:10 format")
            #     print("\n")
            #     outputshown('hmmm something is groing wrong\nkindly provide input time in 22:10 format')
            #     outputshown('\n')
            #------------------------------------------------------------------------------------- SELENIUM START ------------------------------------------------
            # =============================================================================
            #       Meet_start pass command that when chromedriver will start
            # =============================================================================
                
            def meet_stater(self):
                self.ui.textEdit.clear()
                try:
                    c_time = str(datetime.datetime.now())
                    c_min = c_time[-12:-10]
                    c_hour = c_time[-15:-13]
                    c_time = c_hour + ":" + c_min
        
                    datetime2 = datetime.datetime.strptime(self.start_time,"%H:%M")
                    datetime1 = datetime.datetime.strptime(c_time,"%H:%M")
                    t_diff = str(datetime2 - datetime1)
                    values = re.findall('([\d{1}|\d{2}]:\d\d:\d\d)', str(t_diff))
                    minute = values[0][-5:-3]
                    hour = values[0][-len(values[0]):-6]
        
                    
        #             print((t_diff))
                    if re.search("^-\d.*", t_diff):
                        print("Meeting is starting")
                        outputshown("Meeting is starting")
                        return True
                    elif re.search("^\d{1}|\d{2}:\d{1}|\d{2}:\d{1}|\d{2}", t_diff):
                        print(f"Okk!! at {self.start_time}, i start metting")
                        outputshown(f"Okk, at {self.start_time}, i start the metting")
                        QtTest.QTest.qWait((int(minute) + int(hour) *60)*60000)
                        print(f'Okk, so {self.start_time} are done and i start meeting')
                        outputshown(f'Okk, so {self.start_time} are done, and i start the meeting')
                        return True
                    else:
                        print("Something bad happen")
                        outputshown("Something bad happen")
                        return False
                except ValueError:
                    print("Providing time is not valid")
                    outputshown("Providing time is not valid")
                    return False
                except:
                    return False
                
            # =============================================================================
            #       Login start the chromedriver and login enterd user id, pass
            # =============================================================================
    
            def login(self):
                self.ui.textEdit.clear()
                global driver
                global final_link
                opt = Options()
                # opt.add_argument("--headless")
                opt.add_argument('--disable-blink-features=AutomationControlled')
                opt.add_argument("--disable-infobars")
                opt.add_argument("--disable-notifications")
                opt.add_argument("start-maximized")
                opt.add_argument("--disable-extensions")
                opt.add_argument("--in-process-gpu")
                opt.add_argument("--log-level=OFF")
                opt.add_experimental_option('excludeSwitches', ['enable-logging'])
                # opt.add_experimental_option("excludeSwitches", ["enable-automation"])
                # Pass the argument 1 to allow and 2 to block
                opt.add_experimental_option("prefs", { \
                    "profile.default_content_setting_values.media_stream_mic": 1, 
                    "profile.default_content_setting_values.media_stream_camera": 1,
                    "profile.default_content_setting_values.geolocation": 0, 
                    "profile.default_content_setting_values.notifications": 1 
                  })
                
                # driver = webdriver.Chrome(options=opt, executable_path=r'F:/drivers/chromedriver.exe')
                # driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'))
                driver = webdriver.Chrome(options=opt, executable_path=self.resource_path('driver/chromedriver.exe'))
                try:
                    if re.search('^(https://teams.microsoft.com/l).*', self.url):
                        final_link = re.sub('https://teams.microsoft.com/l', 'https://teams.microsoft.com/_#/l', self.url)
                        # print(final_link)
                        print("Link is fine")
                        outputshown("Link is fine")
                    elif re.search('^(https://teams.microsoft.com/_#/l).*', self.url):
                         final_link = (self.url)
                    else:
                        print("There is issue with link\nKindly again check link")
                        outputshown("There is issue with link\nKindly again check link")
                        return False
                    
                    driver.get(final_link)
                    WebDriverWait(driver,20000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))
                    if("login.microsoftonline.com" in driver.current_url):
                        emailField = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'i0116')))
                        emailField.click()
                        emailField.send_keys(uniqueusename)
                        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click() #Next button
                        
                        try:
                            driver.find_element_by_id('usernameError')
                            print("please enter valid email adress")
                            outputshown("Please enter a valid email address")
                            return False
                        except:
                            pass
                            
                        passwordField = WebDriverWait(driver, 10000).until(EC.element_to_be_clickable((By.ID, 'i0118')))
                        passwordField.click()
                        passwordField.send_keys(uniqueusepaswword)
                        WebDriverWait(driver, 10000).until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click()
                    
                        try:
                            driver.find_element_by_id('passwordError')
                            print("please enter valid password")
                            outputshown("Please enter a valid password")
                            return False
                        except:
                            pass
            
                        WebDriverWait(driver, 10000).until(EC.element_to_be_clickable((By.ID, 'idSIButton9'))).click() #remember login
                        QtTest.QTest.qWait(5000)
        
                except Exception as e:
                    print("Error:-\t",e)
                    print("Somthing bad happen at login time")
                    outputshown("Somthing bad happen at login time")
                    return False
                except WebDriverException or TimeoutException or NoSuchWindowException or NoAlertPresentException or NoSuchFrameException or NoSuchElementException or ElementNotVisibleException or ElementNotSelectableException:
                    outputshown("WHY YOU ASSHOLE SHUT THE CHROME!!!")
                    return False
                return True
            
            # =============================================================================
            #       class_joining mute mike and turn of cam, and click on the join button
            # =============================================================================
                
            def class_joining(self):
                try:
                    QtTest.QTest.qWait(5000)
                    webcam = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')))
                    print(webcam.get_attribute('title'))
                    microphone = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="preJoinAudioButton"]/div/button/span[1]')))
                    print(microphone.get_attribute('title'))
                    def sweta_checker(webcam, microphone):
                        if(webcam.get_attribute('title')=='Turn camera off'):
                            webcam.click()
                            QtTest.QTest.qWait(2000)
                            if(microphone.get_attribute('title')=='Mute microphone'):
                                microphone.click()
                                print("Okk, Mike and Webcam are Turn Off so you are not next shweta")
                                outputshown("Okk, Mike and Webcam are Turn Off so you are not next shweta")
                                return True
                            return False
        
                    QtTest.QTest.qWait(5000)
                    while sweta_checker(webcam, microphone):
                        if(webcam.get_attribute('title')=='Turn camera on') & (microphone.get_attribute('title')=='Unmute microphone'):
                            joinnowbtn = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')))
                            joinnowbtn.click()
                        else:
                            sweta_checker(webcam, microphone)
    
                except WebDriverException or TimeoutException or NoSuchWindowException or NoAlertPresentException or NoSuchFrameException or NoSuchElementException or ElementNotVisibleException or ElementNotSelectableException:
                    print("Webbrowser not load, May be coz of net issue\nKindly check your network")
                    outputshown("Webbrowser not load, May be coz of net issue\nKindly check your network")
                    return False
                except Exception as E:
                    print("\n\n",E,"\n\n")                    
                return True
            
            # =============================================================================
            #       its check how many students are present in the class and according to that take action
            # =============================================================================

            def leave_by_people(self):
                self.ui.textEdit.clear()
                def chat_section_opener():
                    try:
                        button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'roster-button')))
                        driver.execute_script("arguments[0].click();", button)
                        print("Clicked on roster button")
                        return True
                    except WebDriverException or TimeoutException or NoSuchWindowException or NoAlertPresentException or NoSuchFrameException or NoSuchElementException or ElementNotVisibleException or ElementNotSelectableException:
                        print("Not clickable coz calling screen is not intractable")
                        return False
                    except:
                        return False
        
                def heavy_driver():
                    while not chat_section_opener():
                        try:
                            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'ts-calling-screen'))).click()
                            print("Trying to click on calling-screen")
                        except:
                            self.leave_by_people()
                        chat_section_opener()
                        print("Again call the chat_section_opener")
                    return True
                
                if heavy_driver() == True:
                    print("I am clicked and stop my working")
                    pass
                
        
                def leave_checker(i):
                    self.ui.textEdit.clear()
                    try:
                        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="teams-app-bar"]/ul/li[3]'))).click() #come back to homepage
                        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hangup-button"]'))).click()
                        if i != 0:
                            print("I am attending your meeting and Finally i am going to sleep")
                            outputshown("I am attending your meeting and Finally i am going to sleep")
                        else:
                            print("start after 15 mins")
                        return True
                    except:
                        return False
                
                j = 0
                def aletring():
                    i = 0
                    print("calling to alerting")
                    print(f"i = {i} and j = {j}")
                    try:
                        no_of_people_info = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-roster/div/div[3]/div/div[1]/accordion/div/accordion-section[2]/div/calling-roster-section/div/div[2]/div/ul'))).text
                        no_of_people_info = no_of_people_info.split('\n')
                        print(f" {no_of_people_info} are present")
                        
                        if len(no_of_people_info) < 10:
                            if len(no_of_people_info[0]) == 0:
                                heavy_driver()
                                return False
                            outputshown(f"Only {no_of_people_info} are present\nSo, i desided to leave")
                            outputshown("again after 10 mins i am join the meeting and check..")
                            leave_checker(i)
                            QtTest.QTest.qWait(900000)
                            if j <= 5 and i == 0:
                                print("i am call the first loop")
                                bypass_login(self)
                                print("i am exit from the first loop")
                            else:
                                pass

                            try:
                                leave_checker(i)
                                driver.close()
                                return True
                            except:
                                return True
                            return True
                        elif 5 < len(no_of_people_info) <15 :
                            if i == 0:
                                outputshown(f"here are only {len(no_of_people_info)-2}+ students are present")
                            else:
                                pass
                        elif 15 < len(no_of_people_info) <25 :
                            if i == 0:
                                outputshown(f"Here are {len(no_of_people_info)-2}+ students are present")
                            else:
                                pass
                        elif 25 < len(no_of_people_info) < 50 :
                            if i == 0:
                                outputshown(f"Ohhhhh, Here are {len(no_of_people_info)-2}+ students are present\nMean class instructor are very clear to understabale for students")
                            else:
                                pass
                        elif 50 < len(no_of_people_info) < 75 :
                            if  i == 0:
                                outputshown(f"OMG!!, Here are {len(no_of_people_info)-5}+ students are present\nBahut garmi ho rahi he bhai A.C chalu karna aaj public jyada lag rahi he..")
                            else:
                                pass
                        elif 75 < len(no_of_people_info) < 100 :
                            if i == 0:
                                outputshown(f"What the heck dude!!!, litterly here are {len(no_of_people_info)-2}+ students are present\nI am glad that i am attending this type of big meeting..\nThanks it's my plasure")
                            else:
                                pass
                        i += 1
                        return False
                    # except Exception as E:
                    #     print(E)
                    except NoSuchElementException:
                        print("entering in no such element Exception")
                        try:
                            actions = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "actions"))).text
                            print(actions)
                            if (actions[0], actions[1]) == ("Rejoin", "Dismiss"):
                                try:
                                    print("sucessfull try kiya bhai")
                                    bypass_login(self)
                                except:
                                    print("bypass ")
                        except:
                            return False
                    except WebDriverException or TimeoutException or NoAlertPresentException or NoSuchFrameException or ElementNotVisibleException or ElementNotSelectableException:
                        print("There is button not interacting so retrying to get the button")
                        return False
                        outputshown("There is button not interacting so retrying to get the button")
                    except:
                        leave_by_people(self)
                        return False
                j+=1
                
                l = 0
                while not aletring():
                    if l == 0:
                        QtTest.QTest.qWait(5000)    
                    else:
                        QtTest.QTest.qWait(120000)
                    l+=1
                    print(l)
                    aletring()
                return True
            
            # =============================================================================
            #       its combination of class_joninig and leave by people 
            #       i do that coz, direct funcation calling give me some error (self) error so rather thn creating new class i am just increase the code's byte
            #       if someone figure out thn pull out requests
            # =============================================================================
            
            def bypass_login(self):
                self.ui.textEdit.clear()
                driver.get(final_link)
                QtTest.QTest.qWait(5000)
                WebDriverWait(driver,20000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))
                if("login.microsoftonline.com" not in driver.current_url):
                    def class_joining1():
                        try:
                            webcam = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')
                            microphone = driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]')
                            print(f"webcam {webcam.get_attribute('title')}, mike {microphone.get_attribute('title')}")
                            def sweta_checker1(webcam, microphone):
                                if(webcam.get_attribute('title')=='Turn camera off'):
                                    webcam.click()
                                elif(microphone.get_attribute('title')=='Mute microphone'):
                                    microphone.click()
                                    print("Okk, Mike and Webcam are Turn Off so you are not next shweta")
                                    outputshown("OK, MIC AND WEBCAM IS OFF SO YOU DON'T BECOME SHWETA")
                                else:
                                    print(webcam.get_attribute('title'))
                                    print(microphone.get_attribute('title'))
                                    outputshown("OK, MIC AND WEBCAM IS OFF SO YOU DON'T BECOME SHWETA")
                                return True
                            while sweta_checker1(webcam, microphone):
                                if(webcam.get_attribute('title')=='Turn camera on') & (microphone.get_attribute('title')=='Unmute microphone'):
                                    joinnowbtn = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
                                    joinnowbtn.click()
   
                                    return True
                                else:
                                    sweta_checker1(webcam, microphone)
                        except WebDriverException or TimeoutException or NoSuchWindowException or NoAlertPresentException or NoSuchFrameException or NoSuchElementException or ElementNotVisibleException or ElementNotSelectableException:
                            print("Webbrowser not load, May be coz of net issue\nKindly check your network")        
                            outputshown("WEBBROWSER NOT LOAD, MAY BE COZ OF NET ISSUE\nKINDLY CHECK YOUR NETWORK")
                            return False
                        except Exception as E:
                            print(E)
                        
                    def leave_by_people1():
                        try:
                            QtTest.QTest.qWait(2000)
                            def chat_section_opener1():
                                try:
                                    button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'roster-button')))
                                    driver.execute_script("arguments[0].click();", button)
                                    print("Clicked on roster button")
                                    return True
                                except WebDriverException or TimeoutException or NoSuchWindowException or NoAlertPresentException or NoSuchFrameException or NoSuchElementException or ElementNotVisibleException or ElementNotSelectableException:
                                    print("Not clickable coz calling screen is not intractable")
                                    return False
                                except:
                                    return False
                    
                            def heavy_driver1():
                                while not chat_section_opener1():
                                    try:
                                        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'ts-calling-screen'))).click()
                                        print("Trying to click on calling-screen")
                                    except:
                                        self.leave_by_people1()
                                    chat_section_opener1()
                                return True
                            
                            if heavy_driver1() == True:
                                print("I am clicked and stop my working")
                                pass
                            
                            def leave_checker1():
                                try:
                                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="teams-app-bar"]/ul/li[3]'))).click() #come back to homepage
                                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hangup-button"]'))).click()
                                    print("I am attending your meeting and Finally i am going to sleep")
                                    outputshown("I am attending your meeting and Finally i am going to sleep")
                                    return True
                                except:
                                    return False
                    
                            def aletring1():
                                try:
                                    no_of_people_info = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-roster/div/div[3]/div/div[1]/accordion/div/accordion-section[2]/div/calling-roster-section/div/div[2]/div/ul'))).text
                                    no_of_people_info = no_of_people_info.split('\n')
                                    print(f" {no_of_people_info} are present")
                                    
                                    if len(no_of_people_info) <= 5:
                    #                     print(len(no_of_people_info))
                                        if len(no_of_people_info[0]) == 0:
                                            heavy_driver1()
                                            return False
                                        outputshown(f"Only {no_of_people_info} are present\nSo, i desided to leave\nmere ko risk nahi lene ka he..")
                                        leave_checker1()
                                        driver.close()
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
#                                     outputshown("There is button not interacting so retrying to get the button")
                                except:
                                    leave_by_people1()
                                    return False
                    
                            while not aletring1():
                                i = 0
                                if i == 0:
                                    QtTest.QTest.qWait(1000)    
                                else:
                                    QtTest.QTest.qWait(120000)
                                i+=1
                                print(i)
                                aletring1()
                                break
                            # return True
                        except WebDriverException or TimeoutException or NoSuchWindowException or NoAlertPresentException or NoSuchFrameException or NoSuchElementException or ElementNotVisibleException or ElementNotSelectableException:
                            print("Webbrowser not load, May be coz of net issue\nKindly check your network")
                            
                            outputshown("WEBBROWSER NOT LOAD, MAY BE COZ OF NET ISSUE\nKINDLY CHECK YOUR NETWORK")
                            QtTest.QTest.qWait(120000)
                            bypass_login(self)
                            return False
                        except Exception as E:
                            print(E)

                class_joining1()
                leave_by_people1()
            
            # =============================================================================
            #       leave by time active if user enter exit time
            # =============================================================================
            
            def leave_by_time(self):
                self.ui.textEdit.clear()
                try:
                    def leave_checker():
                        try:
                            WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="teams-app-bar"]/ul/li[3]'))).click() #come back to homepage
                            WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hangup-button"]'))).click()
                            print("I am attending your meeting and Finally i am going to sleep")
                            outputshown("I am attending your meeting and Finally i am going to sleep")
                            try:
                                driver.close()
                            except:
                                pass
                            return True
                        except WebDriverException or TimeoutException or NoSuchWindowException or NoAlertPresentException or NoSuchFrameException or NoSuchElementException or ElementNotVisibleException or ElementNotSelectableException:
                            return False
                        except:
                            return False
                    
                    e_time = str(datetime.datetime.now())
                    e_min = e_time[-12:-10]
                    e_hour = e_time[-15:-13]
                    e_time = e_hour + ":" + e_min
                    print(self.end_time)
                    datetime2 = datetime.datetime.strptime(self.end_time,"%H:%M")
                    datetime1 = datetime.datetime.strptime(e_time,"%H:%M")
                    print(datetime2, datetime1)
                    t_diff = str(datetime2 - datetime1)
                    values = re.findall('([\d{1}|\d{2}]:\d\d:\d\d)', str(t_diff))
                    minute = values[0][-5:-3]
                    hour = values[0][-len(values[0])+1:-6]
                    
                    print(t_diff)
                    while True:
                        if re.search("^-\d.*", t_diff):
                            print("According to your providing time meeting is already end")
                            leave_checker()
                            break
                        elif re.search("^\d{1}|\d{2}:\d{1}|\d{2}:\d{1}|\d{2}", t_diff):
                            print(f"There is time, so i am sleep for {t_diff} mins")
                            outputshown(f"There is time, so i am sleep for {t_diff} mins")
                            print((int(minute) + int(hour) *60)*60000)
                            QtTest.QTest.qWait((int(minute) + int(hour) *60)*60000)
                            leave_checker()
                            print('OK, as your instructing time i am end this meet')
                            # outputshown('OK, as your instructing time i am end this meet')
                            break
                        else:
                            print("ye time me ku6 locha he re bawa")
                            outputshown("ye time me ku6 locha he re bawa")
                            return False
                        return True
                except ValueError as e:
                    print(e)
                    print("Ending time is not right provided")
                    outputshown("Ending time is not right provided")
                    return False
                except WebDriverException or TimeoutException or NoSuchWindowException or NoAlertPresentException or NoSuchFrameException or NoSuchElementException or ElementNotVisibleException or ElementNotSelectableException or TypeError:
                    outputshown("WHY YOU ASSHOLE SHUT THE BROWSER!!!")
                    driver.close()
                    return False
            
            # =============================================================================
            #       #engine its main loop that call all the funcaiton
            #       
            #       ''' Edit in this loop if you want to modify something in class
            #           When they need to break and continue its all argument pass by this main loop
            #       '''
            # =============================================================================
            print("at ending time")
            print(len(start_time))
            print(len(end_time))
            print(int(len(start_time)) + int(len(end_time)))
            if len(start_time) > 1 & len(end_time) == 0:
                print('enterin this loop')
                t_checker = time_checker2(start_time, end_time)
                print('exit this loop')
            elif (int(len(start_time)) + int(len(end_time))) == 10:
                print('entering this loop1')
                t_checker = time_checker1(start_time, end_time)
                print('exit this loop1')
            else:
                outputshown("Format of time is not right")        
            if t_checker & link_varify(mslink) == True:
                while True:
                    t1_time = str(datetime.datetime.now())
                    t1_min = t1_time[-12:-10]
                    t1_hour = t1_time[-15:-13]
                    t1_time = t1_hour + ":" + t1_min
            
                    alpha = meet_stater(self)
                    if alpha == True:
                        pass
                    elif alpha == False:
                        try:
                            break
                        except:    
                            outputshown("SORRY USER SOMETHING BAD HAPPEN AT CLOSING TIME, WHICH I COULD NOT CONTROLLED SO PLS SHUT THE APP AND RESTART IT")

                    charli = login(self)
                    if charli == True:
                        pass
                    elif charli == False:
                        try:
                            driver.close()
                            break
                        except:
                            outputshown("SORRY USER SOMETHING BAD HAPPEN AT CLOSING TIME WHICH, I COULD NOT CONTROLLED SO PLS SHUT THE APP AND RESTART IT")

                    delta = class_joining(self)
                    if delta == True:
                        pass
                    elif delta == False:
                        try:
                            driver.close()
                            break
                        except:
                            print("delta is dont want to close, ku6 karo")
                            outputshown("SORRY USER SOMETHING BAD HAPPEN AT CLOSING TIME WHICH, I COULD NOT CONTROLLED SO PLS SHUT THE APP AND RESTART IT")
                        
                    if len(end_time) != 0:
                        bravo = leave_by_time(self)
                    else:
                        bravo = leave_by_people(self)
                    if bravo == True:
                        pass
                    elif bravo == False:
                        try:
                            driver.close()
                            break
                        except:
                            outputshown("SORRY USER SOMETHING BAD HAPPEN AT CLOSING TIME WHICH, I COULD NOT CONTROLLED SO PLS SHUT THE APP AND RESTART IT")
                        
                    t2_time = str(datetime.datetime.now())
                    t2_min = t2_time[-12:-10]
                    t2_hour = t2_time[-15:-13]
                    t2_time = t2_hour + ":" + t2_min
        
                    time2 = datetime.datetime.strptime(t2_time,"%H:%M")
                    time1 = datetime.datetime.strptime(t1_time,"%H:%M")
        
                    totaltime = str(time2 - time1)
                    print(f"So you are attending {totaltime} mins")
                    break
                
                



