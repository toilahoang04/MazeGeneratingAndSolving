import pygame as pg
import sys

pg.init()
# size
mazeSize=500
buttonbarW=250
barH=500
pointbarW=150
border=10
# Các màu cơ bản
white = (255, 255, 255)         # Trắng
black = (0, 0, 0)                # Đen
gray = (128, 128, 128)           # Xám
red = (255, 0, 0)                # Đỏ
green = (0, 255, 0)              # Xanh lá
blue = (0, 0, 255)               # Xanh dương
displaySurf=pg.display.set_mode((border+mazeSize+buttonbarW+pointbarW,border+barH))
displaySurf.fill(gray)

#Ảnh
startPic=pg.image.load("./img/actor.png")
endPic=pg.image.load("./img/vietnam.png")
#scale ảnh
startPic=pg.transform.scale(startPic,(50,50))
endPic=pg.transform.scale(endPic,(50,50))

#function chức năng
def drawRecAndText(x,y,w,h,content,size,boxColor,textColor):
    pg.draw.rect(displaySurf,boxColor,(x,y,w,h))
    font=pg.font.Font(None,size)
    text=font.render(content,True,textColor)
    textRect=text.get_rect()
    textBlockRect=pg.Rect(x,y,w,h)
    textRect.center=textBlockRect.center
    displaySurf.blit(text,textRect)

def drawText(x,y,w,h,content,size,color):
    font=pg.font.Font(None,size)
    text=font.render(content,True,color)
    textRect=text.get_rect()
    textBlockRect=pg.Rect(x,y,w,h)
    textRect.center=textBlockRect.center
    displaySurf.blit(text,textRect)
#Biến check đang ở screen nào
AiScreen=True
#hàm vẽ screen
def drawAiScreen():
    pg.draw.rect(displaySurf,(0,0,255),(border/2,border/2,buttonbarW,barH))
    pg.draw.rect(displaySurf,(255,255,255),(border/2+buttonbarW,border/2,mazeSize,mazeSize))
    pg.draw.rect(displaySurf,(0,255,0),(border/2+mazeSize+buttonbarW,border/2,pointbarW,barH))
    #left bar
    drawRecAndText(border/2,border/2*1+50*0,buttonbarW,50,'Autogenerate maze',24,black,white)
    drawRecAndText(border,border/2*2+50*1,buttonbarW-border,50,'DFS',24,black,white)
    drawRecAndText(border,border/2*3+50*2,buttonbarW-border,50,'Hunt and kill',24,black,white)
    drawRecAndText(border/2,border/2*4+50*3,buttonbarW,50,'Autogenerate maze',24,black,white)
    drawRecAndText(border,border/2*5+50*4,buttonbarW-border,50,'BFS',24,black,white)
    drawRecAndText(border,border/2*6+50*5,buttonbarW-border,50,'DFS',24,black,white)
    drawRecAndText(border,border/2*7+50*6,buttonbarW-border,50,'Greedy',24,black,white)
    drawRecAndText(border,border/2*8+50*7,buttonbarW-border,50,'A*',24,black,white)
    #right bar
    drawText(border+buttonbarW+mazeSize,border/2+50*0,75,50,'Start point',24,red)
    drawText(border+buttonbarW+mazeSize,border/2+50*1,75,50,'End point',24,red)
    displaySurf.blit(startPic,(border+buttonbarW+mazeSize+75,border/2+50*0))
    displaySurf.blit(endPic,(border+buttonbarW+mazeSize+75,border/2+50*1))

drawAiScreen()
while(True):
    for event in pg.event.get():
        if event.type==pg.QUIT:
                pg.quit()
                sys.exit()
    pg.display.update()