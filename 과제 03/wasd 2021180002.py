import turtle

T = turtle.Turtle()
T.shape("turtle")
W = T.getscreen()
T.pendown() 
def left() :
    T.seth(180)
    T.forward(50)
    
def right():
    T.seth(0)
    T.forward(50)
    
def forward() :
    T.seth(90)
    T.forward(50)
    
def backward() :
    T.seth(270)
    T.forward(50)

def reset() :
    W.reset()
    
W.onkeypress(left, "a")
W.onkeypress(right, "d")
W.onkeypress(forward, "w")
W.onkeypress(backward, "s")
W.onkeypress(reset, "Escape")
W.listen()
W.mainloop()
