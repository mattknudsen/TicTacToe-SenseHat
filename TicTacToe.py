from sense_hat import SenseHat


sense = SenseHat()
w = (128,128,128)
r = (128,0,0)
b = (0,0,224)
o = (0,0,0)

x1 = 3
y1 = 3
x2 = 4
y2 = 3
x3 = 3
y3 = 4
x4 = 4
y4 = 4

removeLast = 'yes'

currentColor = b




def createBoard():
    sense.clear()
    board = [
        o,o,w,o,o,w,o,o,
        o,o,w,o,o,w,o,o,
        w,w,w,w,w,w,w,w,
        o,o,w,o,o,w,o,o,
        o,o,w,o,o,w,o,o,
        w,w,w,w,w,w,w,w,
        o,o,w,o,o,w,o,o,
        o,o,w,o,o,w,o,o
        ]
    
    sense.set_pixels(board)
    
def spotOpen(x,y):
    try:
        spot = sense.get_pixel(x,y)
        if (spot == [0,0,0]):
            if (x >= 0 or y >= 0):
                return True
        else:
            return False
    except:
        return 'None'
    
    
def checkDiagonal(x1,y1,direction):
    try:
        checkValues = [0,3,6]
        positionInc = 0
        positionDec = 6
        print(x1)
        print(y1)
        print(direction)
        
        if (direction == 'up'):
            while (y1 > positionInc):
                for value in checkValues:
                    print(sense.get_pixel(value, positionInc))
                    if (sense.get_pixel(value, positionInc) == [0,0,0]):
                        print(sense.get_pixel(value,positionInc))
                        newX = value
                        newY = positionInc
                        return newX, newY
                positionInc += 3
                
        elif (direction == 'down'):
            while (y1 < positionDec):
                for value in checkValues:
                    print(sense.get_pixel(value, positionDec))
                    if (sense.get_pixel(value, positionDec) == [0,0,0]):
                        print(sense.get_pixel(value,positionDec))
                        newX = value
                        newY = positionDec
                        return newX, newY
                positionDec -= 3
    
        elif (direction == 'left'):
            while (x1 > positionInc):
                for value in checkValues:
                    print(sense.get_pixel(positionInc, value))
                    if (sense.get_pixel(positionInc, value) == [0,0,0]):
                        print(sense.get_pixel(positionInc,value))
                        newX = positionInc
                        newY = value
                        return newX, newY
                positionInc -= 3
                
        elif (direction == 'right'):
            while (x1 < positionDec):
                for value in checkValues:
                    print(sense.get_pixel(positionDec, value))
                    if (sense.get_pixel(positionDec, value) == [0,0,0]):
                        print(sense.get_pixel(positionDec,value))
                        newX = positionDec
                        newY = value
                        return newX, newY
                positionDec += 3
             
        newX = 'no'
        newY = 'no'
        return newX, newY
    except:
        newX = 'no'
        newY = 'no'
        print('Error in checkDiagonal function')
        return newX, newY
        
    
def changeColor():
    global currentColor
    if (currentColor == b):
        currentColor = r
    elif (currentColor == r):
        currentColor = b
        
def checkForWinner():
    if (sense.get_pixel(0,0) == [0,0,224] and sense.get_pixel(0,3) == [0,0,224] and sense.get_pixel(0,6) == [0,0,224]):
        sense.show_message("Blue Wins!")
        print("Blue Wins")
        sense.clear()
        createBoard()
    elif (sense.get_pixel(3,0) == [0,0,224] and sense.get_pixel(3,3) == [0,0,224] and sense.get_pixel(3,6) == [0,0,224]):
        sense.show_message("Blue Wins!")
        print("Blue Wins")
        sense.clear()
        createBoard()
    elif (sense.get_pixel(6,0) == [0,0,224] and sense.get_pixel(6,3) == [0,0,224] and sense.get_pixel(6,6) == [0,0,224]):
        sense.show_message("Blue Wins!")
        print("Blue Wins")
        sense.clear()
        createBoard()
    elif (sense.get_pixel(0,0) == [0,0,224] and sense.get_pixel(3,0) == [0,0,224] and sense.get_pixel(6,0) == [0,0,224]):
        sense.show_message("Blue Wins!")
        print("Blue Wins")
        sense.clear()
        createBoard()
    elif (sense.get_pixel(0,3) == [0,0,224] and sense.get_pixel(3,3) == [0,0,224] and sense.get_pixel(6,3) == [0,0,224]):
        sense.show_message("Blue Wins!")
        print("Blue Wins")
        sense.clear()
        createBoard()
    elif (sense.get_pixel(0,6) == [0,0,224] and sense.get_pixel(3,6) == [0,0,224] and sense.get_pixel(6,6) == [0,0,224]):
        sense.show_message("Blue Wins!")
        print("Blue Wins")
        sense.clear()
        createBoard()
    elif (sense.get_pixel(0,0) == [0,0,224] and sense.get_pixel(3,3) == [0,0,224] and sense.get_pixel(6,6) == [0,0,224]):
        sense.show_message("Blue Wins!")
        print("Blue Wins")
        sense.clear()
        createBoard()
    elif (sense.get_pixel(6,0) == [0,0,224] and sense.get_pixel(3,3) == [0,0,224] and sense.get_pixel(0,6) == [0,0,224]):
        sense.show_message("Blue Wins!")
        print("Blue Wins")
        sense.clear()
        createBoard()
        
    
    if (sense.get_pixel(0,0) == [128,0,0] and sense.get_pixel(0,3) == [128,0,0] and sense.get_pixel(0,6) == [128,0,0]):
        sense.show_message("Red Wins!")
        print("Red Wins")
        sense.clear()
        createBoard()
    elif (sense.get_pixel(3,0) == [128,0,0] and sense.get_pixel(3,3) == [128,0,0] and sense.get_pixel(3,6) == [128,0,0]):
        sense.show_message("Red Wins!")
        print("Red Wins")
        sense.clear()
        createBoard()
    elif (sense.get_pixel(6,0) == [128,0,0] and sense.get_pixel(6,3) == [128,0,0] and sense.get_pixel(6,6) == [128,0,0]):
        sense.show_message("Red Wins!")
        print("Red Wins")
        sense.clear()
        createBoard()
    elif (sense.get_pixel(0,0) == [128,0,0] and sense.get_pixel(3,0) == [128,0,0] and sense.get_pixel(6,0) == [128,0,0]):
        sense.show_message("Red Wins!")
        print("Red Wins")
        sense.clear()
        createBoard()
    elif (sense.get_pixel(0,3) == [128,0,0] and sense.get_pixel(3,3) == [128,0,0] and sense.get_pixel(6,3) == [128,0,0]):
        sense.show_message("Red Wins!")
        print("Red Wins")
        sense.clear()
        createBoard()
    elif (sense.get_pixel(0,6) == [128,0,0] and sense.get_pixel(3,6) == [128,0,0] and sense.get_pixel(6,6) == [128,0,0]):
        sense.show_message("Red Wins!")
        print("Red Wins")
        sense.clear()
        createBoard()
    elif (sense.get_pixel(0,0) == [128,0,0] and sense.get_pixel(3,3) == [128,0,0] and sense.get_pixel(6,6) == [128,0,0]):
        sense.show_message("Red Wins!")
        print("Red Wins")
        sense.clear()
        createBoard()
    elif (sense.get_pixel(6,0) == [128,0,0] and sense.get_pixel(3,3) == [128,0,0] and sense.get_pixel(0,6) == [128,0,0]):
        sense.show_message("Red Wins!")
        print("Red Wins")
        sense.clear()
        createBoard()
    
    
def moveUp(event):
    if (event.action == 'pressed'):
        global x1
        global y1
        global x2
        global y2
        global x3
        global y3
        global x4
        global y4
        global removeLast
        
        x = x1
        y = y1-3
        if (spotOpen(x,y) == True):
            if (y1 != 0):
                if (removeLast == 'yes'):
                    sense.set_pixel(x1,y1,o)
                    sense.set_pixel(x2,y2,o)
                    sense.set_pixel(x3,y3,o)
                    sense.set_pixel(x4,y4,o)
                
                removeLast = 'yes'
                sense.set_pixel(x1,y1 - 3,currentColor)
                sense.set_pixel(x2,y2 - 3,currentColor)
                sense.set_pixel(x3,y3 - 3,currentColor)
                sense.set_pixel(x4,y4 - 3,currentColor)
                    
                y1 = y1 - 3
                y2 = y2 - 3
                y3 = y3 - 3
                y4 = y4 - 3
                
        elif (spotOpen(x,y) == False):     
            newX, newY = checkDiagonal(x1,y1,'up')
            if (newX != 'no'):
                if (removeLast == 'yes'):
                    sense.set_pixel(x1,y1,o)
                    sense.set_pixel(x2,y2,o)
                    sense.set_pixel(x3,y3,o)
                    sense.set_pixel(x4,y4,o)
                
                print(newX)
                print(newY)
                x1 = newX
                y1 = newY
                x2 = newX + 1
                y2 = newY
                x3 = newX
                y3 = newY + 1
                x4 = newX + 1
                y4 = newY + 1
                
                    
                removeLast = 'yes'
                sense.set_pixel(x1,y1,currentColor)
                sense.set_pixel(x2,y2,currentColor)
                sense.set_pixel(x3,y3,currentColor)
                sense.set_pixel(x4,y4,currentColor)
            
    
def moveDown(event):
    if (event.action == 'pressed'):
        global x1
        global y1
        global x2
        global y2
        global x3
        global y3
        global x4
        global y4
        global removeLast

        x = x1
        y = y1+3
        if (spotOpen(x,y) == True):
            if (y1 != 6):
                if (removeLast == 'yes'):
                    sense.set_pixel(x1,y1,o)
                    sense.set_pixel(x2,y2,o)
                    sense.set_pixel(x3,y3,o)
                    sense.set_pixel(x4,y4,o)
                
                removeLast = 'yes'
                sense.set_pixel(x1,y1 + 3,currentColor)
                sense.set_pixel(x2,y2 + 3,currentColor)
                sense.set_pixel(x3,y3 + 3,currentColor)
                sense.set_pixel(x4,y4 + 3,currentColor)
                
                y1 = y1 + 3
                y2 = y2 + 3
                y3 = y3 + 3
                y4 = y4 + 3
                
        elif (spotOpen(x,y) == False):     
            newX, newY = checkDiagonal(x1,y1,'down')
            if (newX != 'no'):
                if (removeLast == 'yes'):
                    sense.set_pixel(x1,y1,o)
                    sense.set_pixel(x2,y2,o)
                    sense.set_pixel(x3,y3,o)
                    sense.set_pixel(x4,y4,o)
                    
                print(newX)
                print(newY)
                x1 = newX
                y1 = newY
                x2 = newX + 1
                y2 = newY
                x3 = newX
                y3 = newY + 1
                x4 = newX + 1
                y4 = newY + 1
                    
                        
                removeLast = 'yes'
                sense.set_pixel(x1,y1,currentColor)
                sense.set_pixel(x2,y2,currentColor)
                sense.set_pixel(x3,y3,currentColor)
                sense.set_pixel(x4,y4,currentColor)
        
def moveLeft(event):
    if (event.action == 'pressed'):
        global x1
        global y1
        global x2
        global y2
        global x3
        global y3
        global x4
        global y4
        global removeLast

        x = x1-3
        y = y1
        if (spotOpen(x,y) == True):
            if (x1 != 0):
                if (removeLast == 'yes'):
                    sense.set_pixel(x1,y1,o)
                    sense.set_pixel(x2,y2,o)
                    sense.set_pixel(x3,y3,o)
                    sense.set_pixel(x4,y4,o)
                
                removeLast = 'yes'
                sense.set_pixel(x1 - 3,y1,currentColor)
                sense.set_pixel(x2 - 3,y2,currentColor)
                sense.set_pixel(x3 - 3,y3,currentColor)
                sense.set_pixel(x4 - 3,y4,currentColor)
                
                x1 = x1 - 3
                x2 = x2 - 3
                x3 = x3 - 3
                x4 = x4 - 3
                
        elif (spotOpen(x,y) == False):     
            newX, newY = checkDiagonal(x1,y1,'left')
            if (newX != 'no'):
                if (removeLast == 'yes'):
                    sense.set_pixel(x1,y1,o)
                    sense.set_pixel(x2,y2,o)
                    sense.set_pixel(x3,y3,o)
                    sense.set_pixel(x4,y4,o)
                    
                print(newX)
                print(newY)
                x1 = newX
                y1 = newY
                x2 = newX + 1
                y2 = newY
                x3 = newX
                y3 = newY + 1
                x4 = newX + 1
                y4 = newY + 1
                    
                        
                removeLast = 'yes'
                sense.set_pixel(x1,y1,currentColor)
                sense.set_pixel(x2,y2,currentColor)
                sense.set_pixel(x3,y3,currentColor)
                sense.set_pixel(x4,y4,currentColor)
        
        
def moveRight(event):
    if (event.action == 'pressed'):
        global x1
        global y1
        global x2
        global y2
        global x3
        global y3
        global x4
        global y4
        global removeLast

        x = x1+3
        y = y1
        if (spotOpen(x,y) == True):
            if (x1 != 6):
                if (removeLast == 'yes'):
                    sense.set_pixel(x1,y1,o)
                    sense.set_pixel(x2,y2,o)
                    sense.set_pixel(x3,y3,o)
                    sense.set_pixel(x4,y4,o)
                
                removeLast = 'yes'
                sense.set_pixel(x1 + 3,y1,currentColor)
                sense.set_pixel(x2 + 3,y2,currentColor)
                sense.set_pixel(x3 + 3,y3,currentColor)
                sense.set_pixel(x4 + 3,y4,currentColor)
                
                x1 = x1 + 3
                x2 = x2 + 3
                x3 = x3 + 3
                x4 = x4 + 3
                
        elif (spotOpen(x,y) == False):     
            newX, newY = checkDiagonal(x1,y1,'right')
            if (newX != 'no'):
                if (removeLast == 'yes'):
                    sense.set_pixel(x1,y1,o)
                    sense.set_pixel(x2,y2,o)
                    sense.set_pixel(x3,y3,o)
                    sense.set_pixel(x4,y4,o)
                    
                print(newX)
                print(newY)
                x1 = newX
                y1 = newY
                x2 = newX + 1
                y2 = newY
                x3 = newX
                y3 = newY + 1
                x4 = newX + 1
                y4 = newY + 1
                    
                        
                removeLast = 'yes'
                sense.set_pixel(x1,y1,currentColor)
                sense.set_pixel(x2,y2,currentColor)
                sense.set_pixel(x3,y3,currentColor)
                sense.set_pixel(x4,y4,currentColor)
        
    
def pushedMiddle(event):
    if (event.action == 'pressed'):
        global removeLast
        removeLast = 'no'
        checkForWinner()
        changeColor()
    
    if(event.action =='held'):
        sense.clear()
        createBoard()

        
    
createBoard()    
sense.stick.direction_up = moveUp
sense.stick.direction_down = moveDown
sense.stick.direction_left = moveLeft
sense.stick.direction_right = moveRight
sense.stick.direction_middle = pushedMiddle


