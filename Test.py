def count_mines(arr, row, col, N):
    count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < N and 0 <= c < N and arr[r][c] == 1:
            count += 1
    return count

def print_minefield(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                print('*', end=' ')
            else:
                count = count_mines(arr, i, j, N)
                print(count, end=' ')
        print()

def main():
    N = int(input("N: "))
    arr = []
    print("지뢰 위치를 입력하세요 (지뢰는 1로 입력,지뢰가 아닌 곳은 0,각 숫자 입력 후 띄어쓰기!!):")
    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    print("\n내가 입력한 위치:")
    print_minefield(arr, N)

if __name__ == "__main__":
    main()
