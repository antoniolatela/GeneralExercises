from decimal import Decimal

'''getUnsInt returns the unsigned int value from a sequence of bits without limitation to bits number'''
def getUnsInt(s):
    res = 0
    '''This sub-method (visible only internally to getUnsInt(s) method)returns the value of the power of 2 on a specific
     index passed by for loop'''
    def getVal(i):
        v = 0
        for z in range (0, i+1):
            if z == 0:
                v = 1
            elif z ==1 :
                v = 2
            else:
                v = v*2
        return v
    '''for loop reads byte string from left to right and add the result returned calling recursively getVal() method'''
    for i in reversed(range(0, len(s))):
        if int(s[i]) == 1:
            res = res + getVal(abs(i-len(s)+1))
    return res

'''getDecimal2CompNot retruns the decimal value from a list of bits organised in a 2's complement notation'''
def getDecimal2CompNot(s):
    out = ''
    flag = False
    '''the if condition checks if the msb is 1 - then the number should be considered negative. in this case it reads
    all the other bits from right to left and after haveing read the first 1 it flips all the other bits of the list'''
    if s[0] == '1':
        for i in reversed(range(0, len(s))):
            if not flag:
                if s[i] == '0':
                    out = '0' + out
                if s[i] == '1':
                    out = '1' + out
                    flag = True
            else:
                if s[i] == '0':
                    out = '1' + out
                if s[i] == '1':
                    out = '0' + out
        '''at the end of conversion (if negative) the function return the int value (negative) passing the fipper
        bits to getUnsInt function'''
        return -1 * getUnsInt(out)
    else:
        ''' in case of positive value (the first bit is 0) the function pass the string directly to the conversion 
        funtion getUnsInt'''
        return getUnsInt(s)

'''getBinary2CompNot take as input two integers. The first represent the number to convert and the second the the number of bits (8, 16, 32, etc)'''
def getBinary2CompNot(s, bit):
    p = abs(s)
    s1 = ''
    flag = False
    '''this while produce the binary version of the input'''
    while (p >= 1):
        s1 = str(p % 2) + s1
        p = p//2
    '''this wile fill the output up to bit number'''
    while len(s1)<bit:
        s1 = '0' + s1
    '''the if checks if the input si negative. In case of negative input apply the rule of flip number after the first 1 
    found on the right most of the string, from right to left'''
    if s<0:
        cn = ''
        for i in reversed(range(0, len(s1))):
            if not flag:
                if s1[i] == '0':
                    cn = '0' + cn
                if s1[i] == '1':
                    cn = '1' + cn
                    flag = True
            else:
                if s1[i] == '0':
                    cn = '1' + cn
                if s1[i] == '1':
                    cn = '0' + cn
        s1 = cn
    return s1

'''getFloatFromIEEE754 apply the algorithm to transform an IEEE754 32 bit long to a float number'''
def getFloatFromIEEE754(s):
    if len(s)!=32:
        raise Exception('IEEE754 should be 32 bit long string')
    '''sign is the most significant bit of the string'''
    sign = s[0]
    mant = 0
    '''exponent is 8 bit vrom 1 to 9 of 32 byte string array'''
    exp = s[1:9]
    '''get in value of exp and remove 127'''
    exp = getUnsInt(exp) - 127
    '''get mantissa from byte 9 to the end of byte array'''
    m = s[9:len(s)]
    '''calculate decimal part summing 1/x to mant variable where x is the value of the bit based on its position in 
    array'''
    for i in range(0, len(m)):
        if m[i] == '1':
            mant = mant + 1/(2**(i+1))
    '''return the composed value of foat umber converted (-1^sing * (1+ mantissa) * 2^exponent -> to transform the
    number from scientific notation to original float notation)'''
    return ((-1)**int(sign)) * (1 + mant) * 2**(exp)

def getIEEE754FromFloat(s):
    s1 = ''
    s2 = ''
    try:
        '''checks if the value in input is a floating point value'''
        str(s).index('.')
        sign = 0
        '''checks if the sign of input is negative'''
        if s < 0:
            sign = 1
            s = str(s)[1:]
        else:
            s = str(s)
        '''p is the integer part of the numver'''
        p = int(s[0:str(s).index('.')])
        '''q is in 0.xy format'''
        q = float('0.'+s[str(s).index('.')+1:])
        '''transform p in binary'''
        while (p >= 1):
            s1 = str(p % 2) + s1
            p = p // 2
        '''transform q in binary - multilpy 0.xx * 2 until result = 1 and the decimal decimal per of q = 0.0 or if the 
        precision is neverending like in 0.45 the wile finish when the number of byte is 23 that includes also s1 (the
        integer part of the number)'''
        while (q != 0.0 and len(s2) < 23 - (len(s1)-1)):
            q = Decimal(q * 2)
            r = int(q // 1)
            q = (q) - int(q)
            s2 = s2 + str(r)
        '''add 0 at the end in case the number of byte is < 23 for the mantissa'''
        while len(s2) < 23 - (len(s1)-1):
            s2 = s2 + '0'
        '''uses getBinary2CompNot to get exponent converted after adding 127'''
        exp = getBinary2CompNot(127 + (len(s1) - 1), 8)
        '''return the byte string composed by sign, exponent and mantissa'''
        return(str(sign) + exp + s1[1:] + s2)
    except:
        '''in case of not float number add .0 on the right most side to call the function recursively'''
        return getIEEE754FromFloat(float(str(s)+'.0'))

print("Question 4.c: " + str(getDecimal2CompNot('11000001101100000000000000000000')))
print("Question 4.c: " + str(getUnsInt('11000001101100000000000000000000')))
print("Question 4.c: " + str(getFloatFromIEEE754('11000001101100000000000000000000')))

print("Question 5.a: " + getBinary2CompNot(-107, 32))
print("Question 5.b: " + getIEEE754FromFloat(-107))
print("Question 5.c: " + getIEEE754FromFloat(-14.375))
