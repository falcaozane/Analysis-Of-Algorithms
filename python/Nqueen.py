board = [0]*20
count = 0

def main():
    n = int(input("\nEnter the Number of Queens : "))
    queen(1, n)

def print_board(n):
    global count
    print(f"\n Solution {count} : \n\n", end="")
    for i in range(1, n+1):
        print(f"\t{i}", end="")
    for i in range(1, n+1):
        print(f"\n\n{i}", end="")
        for j in range(1, n+1):
            if board[i] == j:
                print("\tQ", end="")
            else:
                print("\t-", end="")

def is_safe(row, column):
    for i in range(1, row):
        if board[i] == column or abs(board[i]-column) == abs(i-row):
            return False
    return True

def queen(row, n):
    for column in range(1, n+1):
        if is_safe(row, column):
            board[row] = column
            if row == n:
                global count
                count += 1
                print_board(n)
            else:
                queen(row+1, n)

if __name__ == "__main__":
    main()
