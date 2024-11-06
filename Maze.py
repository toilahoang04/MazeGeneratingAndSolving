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
displaySurf=pg.display.set_mode((border+mazeSize+buttonbarW+pointbarW,border+barH))
displaySurf.fill(gray)

#Ảnh
#startPic=pg.image.load("./img/actor.png")
#endPic=pg.image.load("./img/vietnam.png")
#scale ảnh
#startPic=pg.transform.scale(startPic,(50,50))
#endPic=pg.transform.scale(endPic,(50,50))

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
    #displaySurf.blit(startPic,(border+buttonbarW+mazeSize+75,border/2+50*0))
    #displaySurf.blit(endPic,(border+buttonbarW+mazeSize+75,border/2+50*1))

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
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

cell_size = 20

w,h = mazeSize // cell_size, mazeSize // cell_size



SaveEndx,SaveEndy =0,0
SaveStartx,SaveStarty =0,0
MAZE = 0



#print(maze)

# Hàm kiểm tra xem vị trí mới có nằm trong phạm vi của mê cung và là tường không
def is_within_bounds(x, y):
    return 0 <= x < h and 0 <= y < w and maze[x][y] == 1

startx = (border/2+buttonbarW) 
starty = (border/2) 


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
                color = black
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




# Hàm tìm các ô chưa thăm xung quanh một ô nhất định
# def get_neighbors(x, y):
#     neighbors = []
#     #random.shuffle(DIRECTIONS)
#     for dx, dy in DIRECTIONS:
#         nx, ny = x + dx * 2, y + dy * 2
#         if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] == 1:
#             neighbors.append((nx, ny, dx, dy))
#     return neighbors
def get_neighbors(x, y):
    neighbors = []
    #random.shuffle(DIRECTIONS)
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx * 2, y + dy * 2
        if 0 <= nx < h and 0 <= ny < w :
            neighbors.append((nx, ny, dx, dy))
    return neighbors
def random_walk(x, y):
    maze[x][y] = 0  # Đánh dấu ô hiện tại là đã ghé thăm
    random.shuffle(DIRECTIONS)  # Trộn hướng đi để tạo mê cung ngẫu nhiên
    TT = False
    while True:
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx * 2, y + dy * 2  # Di chuyển hai ô mỗi lần để tạo tường ngăn cách
            if is_within_bounds(nx, ny):
                maze[x + dx][y + dy] = 0  # Xóa tường giữa các ô
                maze[nx][ny] = 0          # Xóa ô đích để tạo đường đi
                x, y = nx, ny  
                draw_maze(startx,starty)               # Cập nhật màn hình mỗi khi có thay đổi
                pg.display.flip()     # Vẽ lại màn hình
                pg.time.delay(20)     # Thời gian trễ để xem rõ quá trình tạo mê cung
            else: 
                TT = True
                break
        if TT: break
    

    #while True:
        
        # Tìm các ô liền kề chưa ghé thăm
        #neighbors = [(nx, ny, dx, dy) for nx, ny, dx, dy in get_neighbors(x, y) if maze[nx][ny] == 1]
        

        # if neighbors:
        #     # Chọn ngẫu nhiên một ô liền kề chưa ghé thăm
        #     nx, ny, dx, dy = random.choice(neighbors)
        #     # Xóa tường giữa ô hiện tại và ô liền kề
        #     maze[x + dx][y + dy] = 0
        #     maze[nx][ny] = 0
        #     # Di chuyển đến ô mới
        #     x, y = nx, ny
        #     draw_maze(startx, starty)  # Vẽ mê cung
        #     pg.display.flip()
        #     pg.time.delay(30)
        # else:
        #     break
       
def hunt(maze):
    #print(1)
    for i in range(w):
        for j in range(h):
            # Tìm ô chưa ghé thăm có ít nhất một ô liền kề đã ghé thăm
            if maze[i][j] == 1:

                neighbors = [(nx, ny, dx, dy) for nx, ny, dx, dy in get_neighbors(i, j) if maze[nx][ny] == 0]
                print(neighbors)
                if neighbors:
                    #print(1)
                    # Chọn ngẫu nhiên một ô đã ghé thăm liền kề
                    #nx, ny, dx, dy = random.choice(neighbors)
                    #print(nx,ny)
                    # Xóa tường giữa ô chưa ghé thăm và ô đã ghé thăm
                    #maze[i + dx][j + dy] = 0
                    #maze[i][j] = 0
                    # Trả về ô mới để bắt đầu lại từ đó
                    #print("uuuuu")
                    return i, j
    return None, None  # Không tìm thấy ô mới


# Hàm tạo mê cung bằng thuật toán Hunt and Kill
def generate_maze_hunt_and_kill(x,y,maze):
   # Chọn ngẫu nhiên một ô bắt đầu
    random_walk(x, y)

    while True:
        # Thực hiện giai đoạn hunt để tìm ô mới bắt đầu
        x, y = hunt(maze)
        if x is None:
            break  # Kết thúc nếu hunt không tìm thấy ô nào
        # Tiếp tục với giai đoạn kill từ ô mới
        random_walk(x, y)

                    


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
        randomstartx = random.randint(0,24)
        randomstarty = random.randint(0,24)
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
        check_button_dfs = False
        
    if check_button_Hunt_and_Kill:
        randomstartx = random.randint(0,24)
        randomstarty = random.randint(0,24)
        SaveStartx = randomstartx
        SaveStarty = randomstarty
        maze = [[1 for _ in range(w)] for _ in range(h)]  # 1: Tường, 0: Đường
        generate_maze_hunt_and_kill(randomstartx,randomstarty,maze)
        tuple = drawStartEnd()
        MAZE = maze
        SaveEndx = tuple[0]
        SaveEndy = tuple[1]
        check_button_Hunt_and_Kill = False

        

    
    pg.display.update()
    