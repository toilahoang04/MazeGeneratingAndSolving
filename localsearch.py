import numpy as np
import copy
# Mê cung: 0 là đường đi, 1 là tường
# maze = [
#     [0, 1, 0, 0, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0],
# ]

# Hàm kiểm tra bước đi hợp lệ

def is_valid_move(maze, x, y):
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and (maze[x][y] == 0 or maze[x][y] == 4 or maze[x][y] == 3)

# Tính khoảng cách Manhattan
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# Thuật toán Local Search
def local_search(AllMaze,maze, start, end):
    stack = [start]  # Ngăn xếp lưu các vị trí đã đi qua
    path = [start]  # Lưu đường đi đã chọn
    visited = set()
    visited.add(start)
    
    while stack:
        # print(stack[-1])
        current_position = stack[-1]  # Lấy vị trí hiện tại từ đỉnh ngăn xếp
        # if current_position is None:
        #     print("Lỗi: current_position không hợp lệ!")
        #     return None
        x, y = current_position
        neighbors = [
            (x + 1, y), (x - 1, y), 
            (x, y + 1), (x, y - 1)
        ]
        
        # Lọc các neighbor hợp lệ
        valid_neighbors = [
            (nx, ny) for nx, ny in neighbors 
            if is_valid_move(maze, nx, ny) and (nx, ny) not in visited
        ]
        
        # In tất cả các neighbor hợp lệ
        #print(f"Current position: {current_position}")
        #print(f"Valid neighbors: {valid_neighbors}")
        
        if not valid_neighbors:
            stack.pop()  
            path.pop()
            print("iiiiiiiiiiiiiiiiiii") 
            continue
            #return False
            #print("Không tìm thấy đường đi!")
            #return path,AllMaze  # Trả về đường đi hiện tại
        
        # Tìm neighbor gần nhất tới đích
        next_position = min(
            valid_neighbors, 
            key=lambda pos: manhattan_distance(pos[0], pos[1], end[0], end[1])
        )
        stack.append(next_position)
        visited.add(next_position)
        path.append(next_position)
        if next_position[0] == end[0] and next_position[1] == end[1] :
            print("ooo")
            return path,AllMaze
        
        #print(f"Next position chosen: {next_position}\n")
        for neighbor in valid_neighbors:
            maze[neighbor[0]][neighbor[1]] = 4  # Đánh dấu điểm đã đi
            AllMaze.append(copy.deepcopy(maze))

        #maze[next_position[0]][next_position[1]] = 4
        #AllMaze.append(copy.deepcopy(maze)) 
        
       
        #print(next_position)
        print(next_position,end)

        
    
    return False

# Điểm bắt đầu và kết thúc
# start = (0, 0)
# end = (4, 6)

# Gọi thuật toán
# path = local_search(AllMaze,maze, start, end)

# # In kết quả
# print("Đường đi tìm được:", path)

# # Hiển thị mê cung và đường đi
# print("\nMê cung với đường đi:")
# for i in range(len(maze)):
#     for j in range(len(maze[0])):
#         if (i, j) in path:
#             print("P", end=" ")  # P cho path
#         elif maze[i][j] == 1:
#             print("1", end=" ")  # 1 cho tường
#         else:
#             print("0", end=" ")  # 0 cho đường đi
#     print()
