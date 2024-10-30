# Định nghĩa mê cung (0 là đường đi, 1 là tường)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 'E']
]

# Điểm bắt đầu
start = (0, 0)  # Sử dụng tọa độ (hàng, cột)

# Các hướng đi (lên, xuống, trái, phải)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(maze, x, y, visited):
    """ Kiểm tra xem ô (x, y) có hợp lệ không """
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1 and (x, y) not in visited

def dfs(maze, x, y, visited, path):
    """ Hàm DFS để tìm đường đi trong mê cung """
    # Kiểm tra nếu đã đến điểm kết thúc
    if maze[x][y] == 'E':
        path.append((x, y))
        return True

    # Đánh dấu ô (x, y) đã thăm
    visited.add((x, y))
    path.append((x, y))

    # Thử đi theo các hướng
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(maze, nx, ny, visited):
            if dfs(maze, nx, ny, visited, path):
                return True

    # Nếu không tìm thấy đường đi, quay lại (backtrack)
    path.pop()
    return False

def find_path(maze, start):
    visited = set()
    path = []
    if dfs(maze, start[0], start[1], visited, path):
        return path
    else:
        return None

# Tìm đường đi từ điểm bắt đầu
path = find_path(maze, start)

if path:
    print("Đường đi từ điểm bắt đầu đến điểm kết thúc là:")
    for step in path:
        print(step)
else:
    print("Không có đường đi đến điểm kết thúc.")
