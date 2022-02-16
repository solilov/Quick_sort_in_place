from my_sort_packege import Player, quicksort


if __name__ == '__main__':
    number = int(input())
    arr = []
    for i in range(number):
        a, b, c = input().split()
        arr.append(Player(a, int(b), int(c)))
    quicksort(arr, 0, number)
    print(*arr, sep='\n')
