# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def es_alpha(s):
    list =[]
    for i in s:
        if i.isalpha():
            list.append(i)
    return list

def alpha_comp(s):
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    return sorted([x for x in alfabeto if x not in es_alpha(s)])

def es_dig(s):
    list =[]
    for i in s:
        if i.isdigit():
            list.append(i)
    return list

def dig_comp(s):
    digitos = ["1","2","3","4","5","6","7","8","9","0"]
    return sorted([x for x in digitos if x not in es_dig(s)])




def pega(s):
    rest=""
    for i in s:
        rest += i
    return rest

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(es_dig("alos12345"))
    print(dig_comp("alos12345"))
    print(pega(dig_comp("alos12345")))
    print(es_alpha("alos12345"))
    print(alpha_comp("alos12345"))
    print(pega(alpha_comp("alos12345")))
    print(pega(dig_comp("dennce23wcdwd44c"))+pega(alpha_comp("dennce23wcdwd44c")))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
