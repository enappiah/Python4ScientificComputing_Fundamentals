# How to import a function..this is called a module in Python
import os
os.chdir("C:\Users\Akwesi\Dropbox\EETBS 2017-2018 POLIMI-PIACENZA\3 Python Files and Guidelines")
# first way: import 
import functionsCommands

#optional
import functionsCommands as FC  #to recall it as FC

layers_wall = ["faceBreak_100mm","woodFiberboard_13mm"]
results = FC.wall_calc(layers_wall)


# use os option

