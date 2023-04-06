from setup import setup
from output import output
from mainloop import mainloop
from interface import hi


startCheck = setup()

while True:
    if startCheck[0] == True:
        mainloop(startCheck)
