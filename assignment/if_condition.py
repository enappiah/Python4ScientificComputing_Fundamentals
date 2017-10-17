# -*- coding: utf-8 -*-
# if clause
age = raw_input("please insert age ")

if (age<18):    #always remember ":"
    print "just a teen"
elif age>=18 and age<25:
    print "enjoy it"
else:
    print "sorry, the slope is downwards!"
    
# Let's creat a conditional for external Rvalue
season = "winter"
if season == "winter": # == means equal to
   print "RValue = 0.03"
elif season == "summer":
   print "RValue = 0.044"
else:
   print "you have not entered and acceptable season"

#...................................................................

# for L=90, R=0.63. L=140, R= 0.98
lengthWood = 45
if lengthWood == 90:
   RValue = 0.63
elif lengthWood == 140:
    RValue = 0.98
else:
   RValue = 0.63*float(lengthWood)/90
print "RValue= " +str(RValue)
print "I changed the standard value based on the new Length"
    
#....................................................................................................................    
Material_library = {"stucc0_25mm":0.037,"faceBrick_100mm":0.075,"slag_13":0.067, "common_brick100mm":0.12,"wood_25mm":25, 
"insideSurface":0.12, "outsideSurfaceSummer":0.044, "outsideSurfaceWinter":0.03,"woodFiberboard_13mm":0.23}

layers_wall = ["faceBrick_100mm","woodFiberboard_13mm"]
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
#the correct way instead od defining layers, u could: including length in the library
Material_library = {"stucco":{'RValue':0.037,'length':13},"faceBrick_100mm":0.075,"slag_13":0.067, "common_brick100mm":0.12,"wood_25mm":25, 
"insideSurface":0.12, "outsideSurfaceSummer":0.044, "outsideSurfaceWinter":0.03,"woodFiberboard_13mm":0.23}
layers_wall = ["faceBrick","woodFiberboard"]
layers_wall_lengths = [100,13]
layers_wall = [{"material":'facebreak','length':100},{"material":'woodFiberboard','length':13}] # note the [{}]
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

#to add another layer
airOnTwoSides = ["insideSurface","outsideSurfaceSummer"]
layers_wall_complete = layers_wall + airOnTwoSides

Rtot = 0
RValues_layers =[]
for anyLayer in layers_wall_complete:
    RValue_layer = Material_library[anyLayer]
    Rtot = Rtot+RValue_layer
    RValues_layers.append(RValue_layer) # to list all the R values use append
    print "This layer is "+anyLayer
    print " the value of R is "+ str(RValue_layer) +" °C/W"
    print"*************************************************"
print " The total R value is "+str(Rtot) +" °C/W"
#........................................................................................................................    

#Assignment: use the same to for Example 1 of file 1.3 Heat Transfer Through Walls, Simplifications- Part 1
#one insulation was not a standard..cal the insulation by ursef 