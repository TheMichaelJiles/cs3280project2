def applyIPV4SubnetMask(ip, mask):
    ip_list = ip.split('.')
    mask_list = mask.split('.')
    result = ''
    for index in range(4):
        ip_section = int(ip_list[index])
        mask_section = int(mask_list[index])
        result = result + str((ip_section & mask_section)) + '.'

    return result[:-1]

def applyIPV6SubnetMask(ip, mask):
    ip_list = ip.split(':')
    for section in ip_list
        for char in range(len(section) - 4):
            section = section + "0"
        ip += section
    result = ''
    for index in range(mask):
        result += ip_list


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
