
updateIsRunning = False

def getState():
    return updateIsRunning

def setStateTrue():
    global updateIsRunning 
    updateIsRunning = True
def setStateFalse():
    global updateIsRunning 
    updateIsRunning = False