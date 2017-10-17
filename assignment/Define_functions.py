# -*- coding: utf-8 -*-
# defining Funtioncs
#*****************************

def powerOfN(x,n):      #always remember the colon,: sign. Try and copy paste a variable to avoid mistakes
    """this function calculates X^n)"""
    y = x**n
    return y
    
result = powerOfN(2,5) #it is cal from the function above
#or
result = powerOfN(n=5,x=2) # we change the order

#we want to make X value as default
def powerOfN(x=2,n=3):      
    y = x**n
    return y
    
result = powerOfN(n=5,x=2)
result = powerOfN(n=3)
result = powerOfN(n=10)

#x^2+y^2
def z(x,y):
    z = x**2 + y**2
    return z

result = z(2,5) 
#.......................................................................



def wall_calc(listOfLayers):
    
    Material_library = {"stucc0_25mm":0.037,"faceBrick_100mm":0.075,"slag_13":0.067, "common_brick100mm":0.12,"wood_25mm":25, 
    "insideSurface":0.12, "outsideSurfaceSummer":0.044, "outsideSurfaceWinter":0.03,"woodFiberboard_13mm":0.23}
    
    airOnTwoSides = ["insideSurface","outsideSurfaceSummer"]
    layers_wall_complete = listOfLayers + airOnTwoSides
    Rtot = 0
    RValues_layers =[]
    
    for anyLayer in layers_wall_complete:
        RValue_layer = Material_library[anyLayer]
        Rtot = Rtot+RValue_layer
        RValues_layers.append(RValue_layer) # to list all the R values use append
    print " The total R value is "+str(Rtot) +" °C/W"
    RValues_layers.append(Rtot) # or results = {"Rtot":Rtot, "RValue of all layers":RValues_layers.append(RValue_layer)}
    results = {"Rtot":Rtot, "RValue of all layers":RValues_layers}
    return results
    
    
    #.....................................................................................................................................
def wall_calc_assignment(list_of_Layers_in_series,list_of_Layers_in_parallel,fraction ):
    """here is the doc: this fucntion receives two list of layers:parallel and series and a fraction the fractions is the ratio of area of the first layer in the layers in parallel"""
    
    Material_library = {"stucc0_25mm":0.037,"faceBrick_100mm":0.075,"slag_13":0.067, "common_brick100mm":0.12,"wood_25mm":25, 
    "insideSurface":0.12, "outsideSurfaceSummer":0.044, "outsideSurfaceWinter":0.03,"woodFiberboard_13mm":0.23}
    
    airOnTwoSides = ["insideSurface","outsideSurfaceSummer"]
    layers_wall_complete = listOfLayers + airOnTwoSides
    Rtot = 0
    RValues_layers =[]
    
    for anyLayer in layers_wall_complete:
        RValue_layer = Material_library[anyLayer]
        Rtot = Rtot+RValue_layer
        RValues_layers.append(RValue_layer) # to list all the R values use append
    print " The total R value is "+str(Rtot) +" °C/W"
    RValues_layers.append(Rtot) # or results = {"Rtot":Rtot, "RValue of all layers":RValues_layers.append(RValue_layer)}
    results = {"Rtot":Rtot, "RValue of all layers":RValues_layers}
    return results
    
    #do for the example 1 and consider its winter