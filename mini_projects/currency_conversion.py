def rupees_to_dollars():
    rs=int(input('please type the rupees: '))
    dollars= int((rs / 82))
    return dollars

def dollars_to_rupees():
    doll=int(input('please enter the dollars: '))
    rupees=int((doll * 82))
    return rupees

type = input('enter the type of conversion. Type "d" to get value in dollars, Type "r" to get value in rupees: ')

if type == 'd':
    print (rupees_to_dollars())

elif type== 'r':
    print (dollars_to_rupees())

else:
    print('please type a valid option')
