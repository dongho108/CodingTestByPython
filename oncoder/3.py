#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, width, length):

        arr = [[0] * width for _ in range(length)]
        # print(arr)
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        x, y = 0, 0
        now_dir = 0

        while True:
            print(x, y)
            arr[x][y] = 1
            nx = x + dir[now_dir][0]
            ny = y + dir[now_dir][1]

            if 0 <= nx < length and 0 <= ny < width:
                # print(nx, ny)
                if arr[nx][ny] != 1:
                    x = nx
                    y = ny
                    continue

            now_dir = (now_dir+1) % 4
            # print(now_dir)
            nx = x + dir[now_dir][0]
            ny = y + dir[now_dir][1]

            if nx < 0 or nx >= length or ny < 0 or ny >= width or arr[nx][ny] == 1:
                break
            else:
                x = nx
                y = ny

        return y, x

# print(Solution().solution(6, 4))
# print(Solution().solution(6, 5))
# print(Solution().solution(1, 1))
print(Solution().solution(5000, 5000))