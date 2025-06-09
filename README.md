🖥️ Monitor Brightness Automation

Automatically adjust your monitor's brightness and contrast according to the time of day using Python and the Windows Task Scheduler.

📌 What This Does

This script uses ClickMonitorDDC to control your monitor’s brightness and contrast. It switches to:

1. 🌞 Day mode (e.g., Brightness 40, Contrast 60) during daytime hours (8 AM to 6 PM)

2. 🌙 Night mode (e.g., Brightness 10, Contrast 40) during evening and night (6 PM to 8 AM)

It also shows a toast notification only when the mode changes and logs every run.

✅ Features

1. Automatically adjusts monitor brightness & contrast

2. Day and night profile switching based on system time

3. Hourly checks using Task Scheduler

4. Toast notifications for mode switches

5. Execution log saved locally

🛠 Requirements

1. Windows OS

2. Python 3.10+

3. ClickMonitorDDC

4. win10toast Python package

💡 To install the toast notifier, run (using command prompt or powershell): 

        pip install win10toast

🚀 Setup Instructions

1. Download & Set Up ClickMonitorDDC

Download from: [ClickMonitorDDC - MajorGeeks](https://www.majorgeeks.com/files/details/clickmonitorddc.html)

Extract it to a path like:

        C:\Users\YourUsername\ClickMonitorDDC_7_2\

2. Get the Script Files

You can either:

🔁 Clone with Git (for developers):

        git clone https://github.com/pra-bean/monitor-brightness-automation.git
        cd monitor-brightness-automation

📦 Or download as a ZIP:

Click the green “Code” button at the top of this page

Select “Download ZIP”

Extract to a folder like C:\MonitorAutomation\

3. (Optional) Edit the Brightness Settings

Open monitor_switcher.py and customize:

        DAY_MODE = (40, 60)    # Brightness, Contrast for daytime

        NIGHT_MODE = (10, 40)  # Brightness, Contrast for nighttime
        
🕒 Scheduling the Script with Task Scheduler

To make the script run automatically every hour:

A. Open Task Scheduler on your system.

Click Create Basic Task

Name: Auto Monitor Profile Switch (choose any name you want)

Description: This task adjusts the screen brightness automatically. 

B. Set the Trigger

Choose Daily, start at 8:00 AM

Under Advanced Settings:

✅ Check "Repeat task every 1 hour"

✅ Set duration to "1 day"

✅ Check "Enabled"

C. Set the Action

Action: Start a program

Program/script: full path to your Python interpreter (e.g., C:\Users\YourName\AppData\...\python.exe)

Add arguments: full path to monitor_switcher.py (in quotes)

Start in: path to the folder where your .py file lives

D. Finalize

✅ Check "Run with highest privileges"

Click Finish
