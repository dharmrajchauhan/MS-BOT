<h1 align="center"> MICROSOFT TEAMS AUTOMATION </h1>
<div align= "center">
  <img src="https://www.scnsoft.com/blog-pictures/testing/mobile-automated-testing-with-selenium-01.png" width="350" height="200"/>
  <h3>Microsoft Teams Automation systeam built with Selenium using Chromedriver. Sqlite3 and Pandas use for Data Mangemant and PyQt5 use for convert script into a beautiful GUI.</h3>
</div><br>
<div align="center">

[![Python](https://img.shields.io/badge/python-3.8-brightgreen)](https://www.python.org)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15.4-orange)](https://www.qt.io)
[![selenium](https://img.shields.io/badge/SELENIUM-3.14-blue)](https://www.selenium.dev)
[![anaconda](https://img.shields.io/badge/Anaconda.org-1.3.1-blue)](https://www.anaconda.com/open-source)
![bug](https://img.shields.io/badge/bug%2024-fixed-green)
[![pandas](https://img.shields.io/badge/pandas-1.1.3-blue)](https://pandas.pydata.org)
[![sqlite](https://img.shields.io/badge/sqlite-3.36.0-blue)](https://www.sqlite.org/index.html)<br>

![relase](https://img.shields.io/badge/release-v0.0.64-red)
![contib](https://img.shields.io/badge/contributions-welcome-brightgreen)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555)](https://www.linkedin.com/in/dharmrajchauhan/)<br>
</div>

---
## :innocent: Motivation
In the present scenario, schools-colleges are closed due to Covid-19. That's why studies are going on online platforms like ZOOM, GMEET, MS-TEAMS, CISCO, etc. So sometimes maybe we busy in our tight schedule, but attending the meeting is so important. Also sometimes students are sleeping in the lectures and your "meeting" is continuously run inside your phone or pc. And when you wake up and see, you loosed your charge as well as your mobile data and it's totally worst situation.

---
## :hourglass: Project Demo
:movie_camera: [YouTube Demo Link](https://youtu.be/)

:computer: [Software Link](https://drive.google.com/file/d/1rzxosnwBokQ6JddCnKN5v6L3Oqq5T69H/view?usp=sharing)

---
## :warning: TechStack/framework used

- [selenium](https://www.selenium.dev)
- [PyQt5](https://www.qt.io)
- [pandas](https://pandas.pydata.org)
- [sqlite3](https://www.sqlite.org/index.html)
- [pyinstaller]()

---
## :sleeping: Working
<h4><ins>1. For MS-TEAM link</ins></h4>
1.  Provide teams URL <u> and </u> START-TIME, END-TIME(!=complusory)<br>
2.  Then it will join the meet at your given time, and find if student's are less thn 10 thn it will leave the class.<br>
3.  Again after 10 minutes, they will join the class and check students are more thn previous one. if yes thn stay in the meet and if no thn left the meeting.<br>
4.  And continuously after certain amount of time bot will count the student and if they notice there are not more thn 5 thn leave it.<br><br>


<h4><ins>2. For MS-TEAM daily lecture</ins></h4>
1.  Create TimeTable and LEC_NAME dataset. (How to use it is written below)<br>
2.  After creating dataset they grab the data from the table and join in the lec at given time.<br>
3.  Same process apply here. Here also they check if students are more or less. for joining 10+ or removing 10-<br>
4.  Its fully automatic Process which handle every situations.<br>
5.  Also don't worry about the mike and webcam, coz i use shweta_checker which is 101% accurate.<br>

---
## :mask: How to Use
<h4>1. For MS-TEAM link</h4>
<div>

- First step is you need to enter your Id'Pass in The GUI.<br>
  - For creating USER_ID_PASS database.<br>

- Second step is provide your meeting URL and start and end time.<br>
  - So at the "Start_Time" selenium will commanding to the chromedriver login into user account and attend their meeting in given time and left at End_Time.<br>
  - If you are not provide ending time then, it will automatically detect the presence of student and leave the meeting by itself.<br>

</div>

-------

<div>
<h4>2. For TEAMS daily lecture</h4>

- If you are not store your Id'Pass then do it first.

- Provide your COLLEGE/SCHOOL time-table in GUI and press CONFIRM to store data.

- Third most important work is provide your team's lecture name infront of your subject name.
  - Don't worry, i explain.
  - Let's consider for a while that you are in college. Due to somework you have not time to attend lecture, but it's necessary to attend lecture on Monday. Assume your time-table it's look like this.<br><br>

| Day/Time     | Monday | Tuesday | wednesday  |
| ------------ | ------ | ------  | -----------|
| 10:30-11:30  | AI     | DIVP    | IOT-LAB    |
| 11:30-12:30  | IOT    | IOT     | DIVP-LAB   |

AI(Artificial Intelligence) start at 10:30 and IOT(Internet of things) start at 11:30. 
Note:
> It is not necessary to provide subject name same as written in your timetable. Set name as your wish. If you have one subject in which labs/pracs are come and for that your sir make a different class so pls provide diff name like as i proide IOT (For leacture) and IOT-LAB (For Iot'lab). But if lab and lecture are happen in the one class then it not necessary.
<br><h4>So, in my GUI's "TIMETABLE" menu you write your time-table like this.</h4>

<img src="https://user-images.githubusercontent.com/84271454/127255444-1d51e264-2377-4089-bbff-b3de158c1525.jpg" width="1000" height="500">

<br><br><h4>Let's clear your doubt, what's mean of class and what is lec/lab/pracs..</h4>

|CLASS_NAME|LEC_NAME|
|:---:|:---:|
|<img src="https://user-images.githubusercontent.com/84271454/127236580-fd54e79c-910e-45df-b898-ec0934214f50.jpg" width="450" height="500">|<img src="https://user-images.githubusercontent.com/84271454/127237279-41ef0e53-4895-4768-9af1-7ab510050e8c.jpg" width="450" height="500">|<br><br>

In the first column if you see, there are total 6 class(WC, AI, DIVP, DSP, IOT, IML). But if i click on "2021_EC_7_A_3171004_WC" then it have 6 different sub section.First sub section is "general" in which all general types activities are done. Then after some sub section are for different bacthes(A1,A2,A3,A4), if you are from A1 batch then you need to join in "BATCH_A1". And last sub section is "LECTURE". In which daily lecture are done.<br><br>

</h5>I know i am create so much confusion..</h5>

- In simple word, in the "LECTURE NAME" write a lecture name which you write in previous "TIMETABLE" table.<br>
  - Assume the lecture name is "WC".

- In the "MS-SUB NAME" write a class name.
  - For "WC" it's : "2021_ec_7_a_3171104_WC"(#write all in small latter)

- In the "MS-LEC NAME" write a class's sub-class(leb/lec/pracs) name.
  - For "WC"(lecture) it is "lecture"
  - For "WC-LAB"(lab) it is "batch_a1"

<img src="https://user-images.githubusercontent.com/84271454/127242128-42e715b7-4c72-4316-a019-0f33ecb8970f.jpg" width="1000" height="500">
I put this all information in GUI's info section. so don't worry.
If you still have doubt, then be patient i upload the video soon....
<br><br>

------
