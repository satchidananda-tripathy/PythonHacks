
'''

An IP address is a set of numbers that identify your computer on a network.
IPV4, the traditional numbering scheme, which has four quadrant
uses four integers ranging from zero to 255 and set apart by periods.
 For example, "204.120. 0.15" is a valid IPV4 address
'''

def validate_ip(ip):
    octate=[]
    for i in ip.split('.'):
        octate.append(i)
    print(octate)

    if len(octate)!=4:
        return 'Invalid IP'

    for oct in octate:
        if int(oct)<0 or int(oct)>255:
            return 'Invalid IP'
    else:
        return 'Valid IP'
ip ="204.320. 0.15"
print(validate_ip(ip))
ip ="320. 0.15"
print(validate_ip(ip))
ip ="204.12. 0.15"
print(validate_ip(ip))
ip ="204.-1. 0.15"
print(validate_ip(ip))

