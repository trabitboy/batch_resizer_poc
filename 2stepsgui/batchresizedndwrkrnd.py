# 15 min
# +10 min
# +20 min
# + 40 min
# + 45 min
# + 2H wx widg research
# +5 min

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
