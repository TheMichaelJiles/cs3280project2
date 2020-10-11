#! /usr/bin/python

import sys
import validation
import masker

def main():
    ip = sys.argv[1]
    mask = sys.argv[2]
    mask = convertN_NotationToOctet(mask)
    print("Result: " + masker.applySubnetMask(ip, mask))

def convertN_NotationToOctet(mask):
    mask = mask.replace('/', '')
    mask_int = int(mask)
    bin_ip = ''
    ip_list = []
    for index in range(32):
        if index < mask_int:
            bin_ip += '1'
        else:
            bin_ip += '0'

        if (index + 1) % 8 == 0:
            ip_list.append(int(bin_ip, 2))
            bin_ip = ''

    result = ''
    for number in ip_list:
        result = result + str(number) + '.'
    return result[:-1]

if __name__ == '__main__':
    main()