
operators = ["+","(",")","!"]

def tokenize(expression): 
    tokens = [] 
    bool_expresion = expression
    temp_str = ""
    for i in bool_expresion:
        if i not in operators:
            temp_str += i
        elif i == operators[0] or i == operators[3]:
            temp_str += i
        elif i == operators[1] or i == operators[2]:
            tokens.append(temp_str)
            temp_str = ""
        else:
            continue
    tokens.append(temp_str)
    return tokens

def evaluate(token):
    result = ''
    curr_tokens = token
    upd_token = []
    for i in curr_tokens:
        if "+" in i:
            n = absorpOR(idempOR(identity(idempAND(i))))
            if n == '':
                continue
            else:
                upd_token.append(n)
        elif '0' in i or '1' in i:
            upd_token.append(identity(i))
        else:
            # IDEMPOTENT AND
            upd_token.append(f'{''.join(set(i))}')
    #print(result)
    for k in upd_token:
        if k == '+':
            pass
        else:
            result += f'{k}'
    #print(upd_token)
    result = result[0:(len(result))]
    return result


def identity(val):
    result = ''
    if "+" in val and '0' in val or '1' in val:
        data = str(val).split("+")
        fdata = []
        for i in data:
            temp_data = ''
            if '0' in i:
                continue

            elif '1' in i:              # Null Law
                if i == '1':
                    temp_data += i
                    fdata.append(temp_data)
                    break
                else:
                    for j in i:
                        if j == '1':
                            continue
                        else:
                            temp_data += j   
            else:
                temp_data += i
            if temp_data == '':
                continue
            else:
                fdata.append(temp_data)

        for k in fdata:
            result += f'{k}+'
        result = result[0:(len(result))-1]
        return result
                
    elif '1' in val:
        for i in val:
            if i == '1':
                continue
            else:
                result += i
        return result
    elif '0' in val:                #Null Law
        result += '0'
        return result

    else:
        return val


def idempAND(val):
    result = ''
    if "+" in val:
        data = str(val).split("+")
        #IDEMPOTENT OR & AND BOTH SIDES
        for i in data:
            result += f'{''.join(set(i))}+'
        result = result[0:(len(result))-1]
        if result == '':
            return val
        return str(result)
    else:
        return val

def idempOR(val):
    if "+" in val:
        result = ''
        data = str(val).split("+")
        
        for i in range(len(data)):
            j = i + 1
            while j < len(data):
                if data[i] == data[j]:
                    del data[j]
                else:
                    j += 1
        for k in data:
            result += f'{k}+'
        result = result[0:(len(result))-1]
        return result
    else:
        return val


def absorpOR(val):
    result = ''
    if '+' in val:
        data = str(val).split('+')
        tempt_data = []
        print(data)
        for i in range(len(data)-1):
            a = min(data, key=len)
            ab = max(data, key=len)
            if a == ab:
                ab = max(data)

            if len(a) == len(ab):
                if a in ab:
                    tempt_data.append(a)
                    del data[data.index(a)]
                else:
                    tempt_data.append(a)
                    tempt_data.append(ab)
                    del data[data.index(a)]
                    del data[data.index(ab)]
                
            else:
                num = 0
                for i in a:
                    if i in ab:
                        num += 1
                if num == len(a):
                    tempt_data.append(a)
                    del data[data.index(a)]
                    del data[data.index(ab)]

                elif num < len(a):
                    tempt_data.append(a)
                    tempt_data.append(ab)
                    del data[data.index(a)]
                    del data[data.index(ab)]

        for k in tempt_data:
            result += f'{k}+'
        result = result[0:(len(result))-1]
        return result
    else:
        return val
                
def absorpAND(val):
    data = val
    modiToken = []
    result = ""
    while data:
        for i in range(len(data)):
            if "+" in data[i]:
                curr_data = data[i].split('+')
    pass

    

def inverse(val):
    result = ""
    if "+" in val:
        data = str(val).split("+")
        if '!' in data:
            print('nice')

    else:
        if "!" in val:
            result += '0'