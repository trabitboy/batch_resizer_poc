# batch_resizer_poc
proof of concept of a pygame batch resize for the great M

the most up to date prototype is in 2stepsgui folder

install python36 for windows ( any 3 should be fine )
if you do not add your python globally to the path( which I do not recommend ),

open a cmd shell in 
yourpythoninstall/Scripts/

here, install required packages

pip install pygame

pip install wxpython

you should see progress bars and success messages

now to run the tool,
open idle ,

and with idle open 
batchresizedndwrkrnd.py

run with f5

create exe version:

open a cmd shell in 

yourpythoninstall/Scripts/

here, install required packages

pip install cx_freeze

I do not know how to pass arguments to a 
python program through idle 

so I do it from the windows cmd but I need to add python from 
the path, 

so it is runnable from the project folder in the cmd shell

set PATH=%PATH%;C:\whereyouputpython\python36

then from 2 steps gui folder

python setup.py build

a new folder will be created with the executable version

