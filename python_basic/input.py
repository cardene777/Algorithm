# 標準入力について

input()

# リストに変換（空白で区切る）
input().split()

# くっついているものをリストに変換
list(input())

# 数字に変換する
map(int, input().split())

# 数字に変換してリストにする
list(map(int, input().split()))

# n行とってくる
n = 3
[input() for _ in range(n)]
[input().split() for _ in range(n)]
[map(int, input().split()) for _ in range(n)]
[list(map(int, input().split())) for _ in range(n)]

num1, num2, num3, num4, num5 = [int(input()) for i in range(5)]

