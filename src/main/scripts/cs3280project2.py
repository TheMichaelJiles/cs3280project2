#! /usr/bin/python

import sys
import validation
import masker

def main():
    #ip = sys.argv[1]
    #mask = sys.argv[2]
    print(masker.applySubnetMask("255.255.255.255", "255.128.0.0"))

if __name__ == '__main__':
    main()