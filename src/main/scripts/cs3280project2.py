#! /usr/bin/python

import sys
import validation
import masker
import http.server

def main():
    ip = sys.argv[1]
    mask = sys.argv[2]

    if validation.isValidBitNumberNotationNetmask(mask):
        mask = masker.convertN_NotationToOctet(mask)

    if (validation.isValidIPV4Address(ip)):
        if validation.isValidOctectNetmask(mask):
            print("Result: " + masker.applySubnetMask(ip, mask))
        else:
            print("ERROR: MASK INVALID")
            #throw mask invalid error
    else:
        print("ERROR: IP INVALID")
        #throw ip invalid error

if __name__ == '__main__':
    main()
