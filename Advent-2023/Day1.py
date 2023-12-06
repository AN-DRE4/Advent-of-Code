from icecream import ic

def findNums(lines):
    total = 0
    for line in lines:
        num1 = 0
        num2 = 0
        for char in line:
            if char.isdigit():
                num1 = char
                break
        for char in line[::-1]:
            if char.isdigit():
                num2 = char
                break
        joined = num1 + num2
        total += int(joined)
    return total

def findNums2(lines):
    total = 0
    dicionario = {'one': 1, 
                  'two': 2, 
                  'three': 3, 
                  'four': 4, 
                  'five': 5,
                  'six': 6,
                  'seven': 7,
                  'eight': 8,
                  'nine': 9,}
    for line in lines:
        num1 = 0
        str1 = ""
        num2 = 0
        str2 = ""
        pls = False
        for char in line:
            str1 += char            
            if char.isdigit():
                num1 = char
                break
            for chave in dicionario.keys():
                if chave in str1:
                    num1 = str(dicionario[chave])
                    pls = True
                    break
            if pls:
                pls = False
                break
        for char in line[:-1][::-1]:
            str2 += char
            reverse = str2[::-1]
            if char.isdigit():
                num2 = char
                break
            for chave in dicionario.keys():
                if chave in reverse:
                    num2 = str(dicionario[chave])
                    pls = True
                    break
            if pls:
                pls = False
                break
        ic(line[:-1], num1, num2, str1, str2)
        joined = num1 + num2
        total += int(joined)
    return total

def readFile():
    file = open("Day1Input.txt", "r")
    # file = open("test.txt", "r")
    lines = file.readlines()
    file.close()
    return lines

if __name__ == "__main__":
    lines = readFile()
    ic(findNums2(lines))