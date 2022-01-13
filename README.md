# Class Enrollment Utility

A Python script using a Selenium Chrome Driver to enroll McGill students into desired classes.

## Why
The first two weeks of every semester at McGill is called the add/drop period. During this time, students are able to change their classes and finalize their schedules. Throughout the add/drop period, class seats are constantly being opened and quickly taken by students eager to get into their desired classes. Include this script in a crontab bash script that runs every 20 seconds to secure a spot in a desired class as soon as one opens. 

## Requirements:
1. valid McGill email and password
2. python (install: https://www.python.org/downloads/)
3. selenium `pip3 install selenium`
4. chrome driver in package folder (install: https://sites.google.com/a/chromium.org/chromedriver/downloads)
