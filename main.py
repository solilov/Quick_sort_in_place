from my_sort_in_place import Player, quicksort


if __name__ == '__main__':
    number = int(input())
    list_of_players = []
    for i in range(number):
        a, b, c = input().split()
        list_of_players.append(Player(a, int(b), int(c)))
    quicksort(list_of_players, 0, number)
    print(*list_of_players, sep='\n')
