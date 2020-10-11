import re

def isValidIPV4Address(ip):
    validate = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
    return validate.match(ip)

def isValidOctectNetmask(mask):
    validate = re.compile("^(((255\.){3}(255|254|252|248|240|224|192|128|0+))|((255\.){2}(255|254|252|248|240|224|192|128|0+)\.0)|((255\.)(255|254|252|248|240|224|192|128|0+)(\.0+){2})|((255|254|252|248|240|224|192|128|0+)(\.0+){3}))$")
    return validate.match(mask)

def isValidBitNumberNotationNetmask(mask):
    validate = re.compile("(\/1[0-9])|(\/2[0-9])|(\/3[0-1])|(\/[1-9])")
    return validate.match(mask)
