import kk

previuosWay = "none"
axisToUse = "x"

def findWayAndGo(xPos, yPos, spaceWidth, spaceHeight):
    global previuosWay
    global axisToUse
    print(previuosWay)
    if (axisToUse == "x"):
        if (xPos < spaceWidth // 2): 
            kk.pressKeyAndRelease(kk.a)
            if(previuosWay == "right"): 
                print("the way is changed")
                axisToUse = "y"
                return
            previuosWay = "left"
        elif (xPos > spaceWidth // 2): 
            kk.pressKeyAndRelease(kk.d)
            if(previuosWay == "left"): 
                print("the way is changed")
                axisToUse = "y"
                return
            previuosWay = "right"
    elif(axisToUse == "y"):
        if (yPos < spaceHeight // 2): 
            kk.pressKeyAndRelease(kk.w)
            if(previuosWay == "down"): 
                print("the way is changed")
                axisToUse = "x"
                return
            previuosWay = "up"
        elif (yPos > spaceHeight // 2): 
            kk.pressKeyAndRelease(kk.s)
            if(previuosWay == "up"): 
                print("the way is changed")
                axisToUse = "x"
                return
            previuosWay = "down"
