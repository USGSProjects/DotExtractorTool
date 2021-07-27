Before running these files you will need to set up your programming language (python in this case) and coding environment.
For downloading python, just go to the python website (https://www.python.org/) and download python. When downloading python, 
make sure you select add to PATH. This will ensure that the computer terminal can automatically access and use python and its package
manager pip without being in the folder which it is contained and can also sometimes aid coding text editors or IDEs(Integrated Development System) 
to automatically run python as they know its folder location.

Next you want to choose an advanced text editor or IDE to use to read and edit the code. If you are not familiar with coding, I would 
recommend an IDE as it has all the tools necessary to start coding where as text editors usually requires additional plugins 
to do certain stuff like debugging and running code. The IDE I recommend for python is PyCharm (https://www.jetbrains.com/pycharm/download). 

If you are on a government network and you are getting a strange popup every few seconds about some certificate error, follow the instructions in 
this paragraph. Otherwise, you may go to the next paragraph. To fix the error go to the top and select PyCharm < Preferences < Tools < Server Certificates on 
a mac or File < Settings < Tools < Server Certificates on Windows and Linux and select the option "accept all untrusted certificates automatically." Make sure to press
apply and okay. This should fix the error.

Once you download PyCharm, you have to link the python downloaded earlier with the PyCharm so PyCharm can understand and run python code.
To do this, you must go to the top and get to PyCharm < Preferences < Project<project name> < Python Interpreter on a mac or 
File < Settings < Project<project name> < Python Interpreter on Windows and Linux and select the gear button and press add. 
From there you should select System Interpreter instead of Virtualenv Environment. Although Virtualenv Environment can be used, 
it can be inconvenient and confusing as any packages you download will only be applied to that project and if you work on 
another project you may accidentally add a package to the wrong project. In addition, you may need a special command besides "pip 
install <package name>" to download packages from the terminal. After selecting System Interpreter, click the three ellipsis button
and find/enter/drag the path of the python.exe downloaded. Click Ok to get back to the Python Interpreter screen. In the place where 
you can choose a python interpreter, select the python interpreter that you just added. Press Apply and Ok. You should now be set up 
on PyCharm.

Once importing a python project or writing some code, press the run button. Make sure that the path of the file you want to run is properly set. You can check if 
it is properly set if the file you want to run is written to the left of the run button. If not you need to click that and press "edit configurations..." Edit the Script 
Path to the desired file location that you want to run and press apply and okay. 

If you get some error regarding a package not being found, you can install a package by going to PyCharm < Preferences < Project<project name> < Python Interpreter 
on a mac or File < Settings < Project<project name> < Python Interpreter on Windows and Linux and pressing the add button. Search for the package that is needed. 
One thing to keep in mind is that the import statement package name is not necessarily the name of the package. You will have to do a quick google search to find out 
the true package name before installing it. Once you find the package you need, install package and you will be notified if/when the package has been successfully installed.

If there is an issue downloading certain files, especially in a government network, run this command in the command terminal:
"pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package_name>". It is important that you select add to PATH when downloading
python or else the computer will not know what pip is referring to if you are not in the same directory it is contained in.

The files in this folder are gooeys so no variable initializations have to be made as variables are adjusted in the gooey.
Just run the specific script that corresponds to the desired program to use a specific gooey.

For certain applications, you may want to create an exe file for a script that has a gooey system which can make it easier for others to use a program without any 
coding knowledge. If you would like to do this, I recommend following the video (https://www.youtube.com/watch?v=Y0HN9tdLuJo&t=166s). To sum up how to make the conversion,
you must first download the python program auto-py-to-exe. Remember, if you are on a government network, you might have to run "pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package_name>"
in the terminal instead of just pip install <package name>. Once the code is downloaded, type in auto-py-to-exe in the terminal. This will pop up a python to exe conversion screen. In the first field, Script Path, you must select
the path of the code (which will be run) that you want to turn into an exe file. Any supporting files(other python files that have classes or functions that are used in the python file that will be run) will be added in the
Additional Files section. For the Onefile section, you must choose whether your code is contained in a directory, usually with supporting files, or just a single script. The Console Window section is the place where you
select whether or not you want the exe file to have a console to print out statements like in the IDE. The Icon section is optional but highly recommended as it helps distinguish your program from other exe files. To create 
an Icon, I would recommend finding a picture supported by a Creative Commons license to avoid any potential legal trouble. After obtaining a photo, I recommend going to convertico.com and uploading the photo you want to be 
the icon and downloading the corresponding ico file. When you have the ico file, you can select the file of that file in the Icon section in auto-py-to-exe. The Advanced section is also optional and should be used if there are any 
complications when converting a python file. In the Output section, select the place you want the exe file to be put. When all settings are set correctly, press Convert .PY to .EXE. Your exe file should appear in its respective 
location shortly after.





