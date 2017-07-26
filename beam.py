# coding=utf-8
#import queue as q
import heapq

INF = 100000000
maze = [
    ['#', 'S', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '#'],
    ['.', '#', '#', '#', '#', '.', '#', '#', '.', '#'],
    ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
    ['.', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '#', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ]

sx, sy = 0, 1 # スタート地点の座標
gx, gy = 9, 6 # ゴール地点の座標

field_x_length = len(maze)
field_y_length = len(maze[0])

class State():
    def __init__(self, distance, score, x, y):
        self.distance = distance
        self.score = score
        self.x = x
        self.y = y
    def __lt__(self, other):
        return self.score < other.score

def debug_print(maze):
    for xx in maze:
        for yy in xx:
            print(yy, end="")
        print("\n", end="")

def beam(beam_size):
    queue = []
    distance = 0
    for i in range(0, 4):
        nx, ny = sx + [1, 0, -1, 0][i], sy + [0, 1, 0, -1][i]
        if (0 <= nx and nx < field_x_length and 0 <= ny and ny < field_y_length and maze[nx][ny] != '#'):
            score = (gx - nx) ** 2 + (gy - ny) ** 2
            heapq.heappush(queue, State(distance+1, score, nx, ny))

    loop_count = 0
    while len(queue):
        if loop_count % beam_size == 0:
            queue = queue[:beam_size]

        state = heapq.heappop(queue)
        distance = state.distance
        x = state.x
        y = state.y

        if x == gx and y == gy:
            ans = distance
            break

        for i in range(0, 4):
            nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]

            if (0 <= nx and nx < field_x_length and 0 <= ny and ny < field_y_length and maze[nx][ny] != '#'):
                score = (gx - nx) ** 2 + (gy - ny) ** 2
                heapq.heappush(queue, State(distance+1, score, nx, ny))
                print((distance+1, score, nx, ny))

        loop_count += 1

    return ans

def clear_maze():
    debug_print(maze)
    return beam(5)

if __name__ == "__main__":
    print(clear_maze())
