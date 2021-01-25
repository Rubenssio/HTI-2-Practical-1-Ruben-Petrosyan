def hanoi(n, source, destination, aux):

    if n > 1:
        hanoi(n - 1, source, aux, destination)
        print(f'Move disk {n} from {source} to {destination}\t\tpr 2')
        hanoi(n-1, aux, destination, source)

    else:
        print(f'Move disk 1 from {source} to {destination}\t\tpr 1')
        return


n = int(input('n = '))
hanoi(n, 'A', 'C', 'B')
