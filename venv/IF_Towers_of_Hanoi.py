def hanoi_tower(discs):
    '''
    There are three pegs.
    Initially, N disks are put on the first peg in order from larger to smaller.
    The goal is to move all the disks to the third peg.
    When moving disks, you can't put a larger disk on a smaller disk.
    :param discs: number of disks (int, positive)
    :return: The minimum number of steps to complete the task
    >>> hanoi_tower(10) - 1023
    >>> hanoi_tower(0) - 0
    >>> hanoi_tower(3) - 7
    '''

    if discs < 0:
        print('Input a positive integer number')
    else:
        print(2**discs - 1)

hanoi_tower(5)


