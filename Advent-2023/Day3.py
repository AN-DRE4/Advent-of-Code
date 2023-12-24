from icecream import ic

def allSymbols(lines):
    lista = []
    for line in lines:
        line2 = line.strip()
        ic(line2)
        for symbol in line2:
            if not symbol.isdigit() and symbol != ".":
                # append the location of the symbol
                lista.append((lines.index(line), line.index(symbol)))
    return lista

def solve(lines):
    lista = allSymbols(lines)
    return lista


def readFile():
    # file = open("Day3Input.txt", "r")
    file = open("Advent-2023/test.txt", "r")
    lines = file.readlines()
    file.close()
    return lines

if __name__ == "__main__":
    lines = readFile()
    ic(solve(lines))