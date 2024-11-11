import pygame as pg
import sys
import random

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
aqua = (0, 255,255) 
dark_green = (0, 100, 0)
pale_yellow = (255, 255, 204)
displaySurf=pg.display.set_mode((border+mazeSize+buttonbarW+pointbarW,border+barH))
displaySurf.fill(gray)

#Ảnh
startPic=pg.image.load("./img/actor.png")
endPic=pg.image.load("./img/vietnam.png")
#scale ảnh
startPic=pg.transform.scale(startPic,(40,40))
endPic=pg.transform.scale(endPic,(40,40))

#load music
pg.mixer.music.load('./DLTTAD.mp3')  # Thay thế 'background_music.mp3' bằng tên tệp của bạn
pg.mixer.music.set_volume(0.1)  # Thiết lập âm lượng (0.0 đến 1.0)
pg.mixer.music.play(-1)  # Phát nhạc nền lặp lại vô hạn (-1)
#volume = 0.5



#function chức năng
def drawButton(x,y,w,h,content,size,textColor,inactiveColor,activeColor):
    mouse = pg.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pg.draw.rect(displaySurf, activeColor, (x, y, w, h))
    else:
        pg.draw.rect(displaySurf, inactiveColor, (x, y, w, h))
    font=pg.font.Font(None,size)
    text=font.render(content,True,textColor)
    textRect=text.get_rect()
    textBlockRect=pg.Rect(x,y,w,h)
    textRect.center=textBlockRect.center
    displaySurf.blit(text,textRect)
def drawRecAndText(x,y,w,h,content,size,boxColor,textColor):
    pg.draw.rect(displaySurf, boxColor, (x, y, w, h))
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
    #pg.draw.rect(displaySurf,(255,255,255),(border/2+buttonbarW,border/2,mazeSize,mazeSize))
    pg.draw.rect(displaySurf,(0,255,0),(border/2+mazeSize+buttonbarW,border/2,pointbarW,barH))
    #left bar
    drawRecAndText(border/2,border/2*1+50*0,buttonbarW,50,'Autogenerate Maze',24,black,white)


    drawButton(border,border/2*2+50*1,buttonbarW-border,50,'DFS',24,black,white,red)
    drawButton(border,border/2*3+50*2,buttonbarW-border,50,'Hunt and Kill',24,black,white,red)

    drawRecAndText(border/2,border/2*4+50*3,buttonbarW,50,'Algorithm Solving Maze',24,black,white)


    drawButton(border,border/2*5+50*4,buttonbarW-border,50,'BFS',24,black,white,red)
    drawButton(border,border/2*6+50*5,buttonbarW-border,50,'DFS',24,black,white,red)
    drawButton(border,border/2*7+50*6,buttonbarW-border,50,'Greedy',24,black,white,red)
    drawButton(border,border/2*8+50*7,buttonbarW-border,50,'A*',24,black,white,red)
    #right bar
    drawText(border+buttonbarW+mazeSize,border/2+50*0,75,50,'Start point',24,red)
    drawText(border+buttonbarW+mazeSize,border/2+50*1,75,50,'End point',24,red)
    displaySurf.blit(startPic,(border+buttonbarW+mazeSize+75+10,border/2+50*0))
    displaySurf.blit(endPic,(border+buttonbarW+mazeSize+75+10,border/2+50*1))

def check_stable_button(x, y, width, height):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        if click[0] == 1:
            return True
    return False


# check button dfs
check_button_dfs = False
check_button_Hunt_and_Kill = False

# Directions for moving in the maze (Right, Left, Down, Up)
# Khởi tạo các hướng di chuyển
DIRECTIONS = [
    (-1, 0),  # Lên
    (1, 0),   # Xuống
    (0, -1),  # Trái
    (0, 1)    # Phải
]

cell_size = 20
w,h = mazeSize // cell_size, mazeSize // cell_size



SaveEndx,SaveEndy =0,0
SaveStartx,SaveStarty =0,0
MAZE = 0



#print(maze)
#=====================================Function chung========================================
# Hàm kiểm tra xem vị trí mới có nằm trong phạm vi của mê cung và là tường không
def is_within_bounds(x, y):
    return 0 < x < h-1 and 0 < y < w-1 and maze[x][y] == 1

startx = (border/2+buttonbarW) 
starty = (border/2) 
#==========================================DFS==============================================
# Randomized Depth-First Search algorithm to generate maze
def generate_maze(x, y,maze):
    x = int(x)
    y = int(y)
    maze[x][y] = 0  # Đặt ô khởi đầu là đường (0)
    random.shuffle(DIRECTIONS)  # Trộn hướng đi để tạo mê cung ngẫu nhiên

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx * 2, y + dy * 2  # Di chuyển hai ô mỗi lần để tạo tường ngăn cách
        if is_within_bounds(nx, ny):
            maze[x + dx][y + dy] = 0  # Xóa tường giữa các ô
            maze[nx][ny] = 0          # Xóa ô đích để tạo đường đi
            draw_maze(startx,starty)               # Cập nhật màn hình mỗi khi có thay đổi
            pg.display.flip()     # Vẽ lại màn hình
            pg.time.delay(20)     # Thời gian trễ để xem rõ quá trình tạo mê cung
            generate_maze(nx, ny,maze)     # Đệ quy tiếp tục từ ô đích
# Drawing the maze
def draw_maze(startx, starty):
    for x in range(w):
        for y in range(h):
            if maze[x][y] == 1 :
                color = dark_green
            # elif maze[x][y] == 2:
            #     color = pale_yellow
            else: color = white
            pg.draw.rect(displaySurf, color, (startx + x * cell_size, starty+ y * cell_size, cell_size, cell_size))
def drawStartEnd():
    list =[]
    for x in range(w):
        for y in range(h):
            if maze[x][y] == 0 :
                list.append((x,y))
    randomend = random.randint(0, len(list))
    #print(randomend)
    tuple = list[randomend]
    #print(tuple)
    
    pg.draw.rect(displaySurf, red, (startx + randomstartx * cell_size, starty+ randomstarty* cell_size, cell_size, cell_size))
    pg.draw.rect(displaySurf, aqua, (startx + tuple[0] * cell_size, starty+ tuple[1]* cell_size, cell_size, cell_size))
    return tuple
    #print(startx , randomstartx, starty, randomstarty)

#==========================================Hunt and kill==============================================
def createMaze(maze,n):
    for i in range(n):
        for j in range(n):
            if i%2==0 or j%2==0:
                maze[i][j]=1
            else:
                maze[i][j]=0
def is_valid(maze, x, y):
    # Kiểm tra xem ô (x, y) có nằm trong giới hạn của mê cung và chưa được ghé thăm
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0
def huntAndKill(maze, start_x, start_y):
    maze[start_x][start_y] = 2  # Đánh dấu ô đầu tiên là đã ghé thăm bằng 2
    current_x, current_y = start_x, start_y

    while True:
        # Kill phase: Tìm ô lân cận chưa ghé thăm
        unvisited_neighbors = []
        for dx, dy in DIRECTIONS:
            nx, ny = current_x + 2*dx, current_y + 2*dy
            if is_valid(maze, nx, ny):
                unvisited_neighbors.append((nx, ny))

        if unvisited_neighbors:
            # Chọn ngẫu nhiên một ô lân cận chưa ghé thăm
            next_x, next_y = random.choice(unvisited_neighbors)
            wall_x, wall_y = (current_x + next_x) // 2, (current_y + next_y) // 2
            maze[wall_x][wall_y] = 2  # Phá vách ngăn bằng cách đánh dấu là 2
            maze[next_x][next_y] = 2  # Đánh dấu ô mới là đã ghé thăm
            current_x, current_y = next_x, next_y
            #vẽ
            draw_maze(startx,starty)
            pg.display.flip()
            pg.time.delay(20)
        else:
            # Hunt phase: Tìm ô chưa ghé thăm có lân cận đã ghé thăm
            found = False
            for i in range(len(maze)):
                for j in range(len(maze[i])):
                    if maze[i][j] == 0:  # Tìm ô chưa ghé thăm
                        # Kiểm tra nếu ô này có ô lân cận đã ghé thăm
                        for dx, dy in DIRECTIONS:
                            ni, nj = i + 2*dx, j + 2*dy
                            if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and maze[ni][nj] == 2:
                                # Phá vách ngăn và đánh dấu ô mới là đã ghé thăm
                                wall_x, wall_y = (i + ni) // 2, (j + nj) // 2
                                maze[wall_x][wall_y] = 2  # Phá vách ngăn
                                maze[i][j] = 2  # Đánh dấu ô này là đã ghé thăm
                                current_x, current_y = i, j  # Cập nhật vị trí hiện tại
                                found = True
                                pg.time.delay(500)
                                break
                        if found:
                            break
                    if found:
                        break
            # Nếu không tìm thấy ô nào chưa ghé thăm, thoát khỏi vòng lặp
            if not found:
                break

    # In mê cung kết quả
    for row in maze:
        print(" ".join(map(str, row)))
while(True):
    for event in pg.event.get():
        if event.type==pg.QUIT:
                pg.quit()
                sys.exit()
        if check_stable_button(border,border/2*2+50*1,buttonbarW-border,50):
            check_button_dfs = True
        if check_stable_button(border,border/2*3+50*2,buttonbarW-border,50):
            check_button_Hunt_and_Kill = True
    
    drawAiScreen()
    if check_button_dfs:
        #print(startx , randomstartx, starty, randomstarty)
        #(randomstartx,randomstarty)
        randomstartx = random.randint(1,24)
        randomstarty = random.randint(1,24)
        while randomstartx%2==0:
            randomstartx = random.randint(1,24)
        while randomstarty%2==0:
            randomstarty = random.randint(1,24)
        SaveStartx = randomstartx
        SaveStarty = randomstarty
        maze = [[1 for _ in range(w)] for _ in range(h)]  # 1: Tường, 0: Đường
        generate_maze(randomstartx,randomstarty,maze)
        tuple = drawStartEnd()
        MAZE = maze
        SaveEndx = tuple[0]
        SaveEndy = tuple[1]
        # print(SaveEndx, SaveEndy)
        # print(MAZE)
        draw_maze(startx,starty)
        check_button_dfs = False
        
    if check_button_Hunt_and_Kill:
        n=int(500/cell_size)
        randomstartx = random.randint(0,n-1)
        randomstarty = random.randint(0,n-1)
        while randomstartx%2==0:
            randomstartx = random.randint(1,n-1)
        while randomstarty%2==0:
            randomstarty = random.randint(1,n-1)
        SaveStartx = randomstartx
        SaveStarty = randomstarty
        maze = [[0 for _ in range(n)] for _ in range(n)]
        createMaze(maze,n)
        huntAndKill(maze,SaveStartx,SaveStarty)
        draw_maze(startx,starty)
        check_button_Hunt_and_Kill = False
        
    pg.display.update()
