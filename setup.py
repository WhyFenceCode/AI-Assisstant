import os
import time

def setup():

loginarry = login()

if loginarry[0] != False:
    email = loginarry[0]
    username = loginarry[1]

setupFinished = True

setupArray = [setupFinished, email, username]

return setupArray

def register():

    emailreg = True
    usernamereg = True
    firstnamereg = True
    agereg = True
    pronounsreg = True
    birthdayreg = True


    with open('users.txt', 'a') as y:
    y.write('\n')
    y.write(emailreg + "|" + usernamereg + "|" + firstnamereg + "|" + agereg + "|" + pronounsreg + "|" + birthdayreg)
    y.close

def login():
    users = open("users.txt").read().split("|")
    if users[0] != "":
        loginarryInternal[i] = users[i]
        return loginarryInternal
    else:
        register()
