#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    based in leetcode.com
    :type data: List[int]
    :rtype: True if data is a valid UTF-8 encoding, else return False
    """

    num_bytes = 0

    # 1000 0000
    fst_mask = 1 << 7

    # 0100 0000
    snd_mask = 1 << 6
    for num in data:
        # 1000 0000
        mask = 1 << 7
        if num_bytes == 0:
            # 1000 0000 & 0100 0001
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (num & fst_mask and not (num & snd_mask)):
                return False
        num_bytes -= 1
    return num_bytes == 0
