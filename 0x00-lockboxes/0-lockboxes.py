#!/usr/bin/python3
"""Lockboxes interview preparation"""


def canUnlockAll(boxes):
    """Verify if all boxes can be opened"""

    if boxes == []:
        return True

    i_list = [i for i in range(len(boxes))]

    visited = [0]

    for v in visited:
        for k in boxes[v]:
            if k not in visited and k in i_list:
                if k >= len(boxes):
                    return False
                visited.append(k)

    if len(visited) == len(boxes):
        return True
    else:
        return False
