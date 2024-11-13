from collections import deque
import copy

# Định nghĩa mê cung (0 là đường đi, 1 là tường)
# maze = [
#     [0, 1, 0, 0, 0],
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0],
#     [1, 1, 0, 1, 0],
#     [0, 0, 0, 0, 'E']
# ]

# Điểm bắt đầu
# start = (0, 0)  # tọa độ (hàng, cột)

# Các hướng đi (lên, xuống, trái, phải)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(maze, x, y, visited):
    """ Kiểm tra xem ô (x, y) có hợp lệ không """
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1 and (x, y) not in visited

def bfs(AllMaze,maze, start,end):
    """ Hàm BFS để tìm đường đi trong mê cung """
    queue = deque([(start, [start])])  # Sử dụng deque cho queue với mỗi phần tử là (tọa độ, đường đi hiện tại)
    visited = set([start])  # Tập hợp các ô đã thăm

    while queue:
        (x, y), path = queue.popleft()  # Lấy phần tử đầu hàng đợi
        

        # Kiểm tra nếu đã đến điểm kết thúc
        if x == end[0] and y == end[1]:
            return path,AllMaze
        maze[x][y] = 4
        AllMaze.append(copy.deepcopy(maze))
        # Thử đi theo các hướng
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(maze, nx, ny, visited):
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None  # Trả về None nếu không tìm thấy đường đi

# Tìm đường đi từ điểm bắt đầu
#path = bfs(maze, start,end)

# if path:
#     print("Đường đi ngắn nhất từ điểm bắt đầu đến điểm kết thúc là:")
#     for step in path:
#         print(step)
# else:
#     print("Không có đường đi đến điểm kết thúc.")
