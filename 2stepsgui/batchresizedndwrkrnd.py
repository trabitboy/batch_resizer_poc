#dnd to pyg with a button 3
#resize of window 3
#zooming and navigating the zoom mousewheel centré du pointeur de la souris 1
#backup last image and revert on right/middle click
#no initial selection1
#click to start selection 1
#save and crop on release1
#cancel selection in progress with another mouse button 3
#support pictures bigger than window 2
#make 3 different crops with buttons in wx widgets part 2
#save over source picture 1

# test push for M

# 15 min
# +10 min
# +20 min
# + 40 min
# + 45 min
# + 2H wx widg research
# +5 min
# +42 min refactor and go to next pic
# +1h10 zoom and scale without nav

#TODO
# scale down picture larger than viewport,
# determine zoom level
# select based on zoom level
# navigate to next slot

#poc for the great M
from wxselector import createDnd
from pygameresize import createPygameResizeWindow

##import threading


##here we will put the dropped files 
dnded=[]



 

createDnd(dnded)

print("dnd over, we have this : ")
print(dnded)

createPygameResizeWindow(dnded)
