

def applySubnetMask(ip, mask):
    ip_list = ip.split('.')
    mask_list = mask.split('.')
    result = ''
    for index in range(4):
        ip_section = int(ip_list[index])
        mask_section = int(mask_list[index])
        print(ip_section)
        print(mask_section)
        print("Masked: " + str((ip_section & mask_section)))
        result = result + str((ip_section & mask_section)) + '.'

    return result[:-1]

