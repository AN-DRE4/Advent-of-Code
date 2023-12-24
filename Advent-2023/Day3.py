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

    nums = []
    # now search the if there are numbers adjacent to the symbols
    for symbol in lista:
        if symbol[0] != 0:
            # check the symbol above, only if it is not the first line
            if lines[symbol[0]-1][symbol[1]].isdigit():
                ic(lines[symbol[0]-1][symbol[1]])
        # check the symbol below, only if it is not the last line
        if symbol[0] != len(lines)-1:
            if lines[symbol[0]+1][symbol[1]].isdigit():
                ic(lines[symbol[0]+1][symbol[1]])
        # check the symbol to the left, only if it is not the first column
        if symbol[1] != 0:
            if lines[symbol[0]][symbol[1]-1].isdigit():
                ic(lines[symbol[0]][symbol[1]-1])
        # check the symbol to the right, only if it is not the last column
        if symbol[1] != len(lines[symbol[0]])-1:
            if lines[symbol[0]][symbol[1]+1].isdigit():
                ic(lines[symbol[0]][symbol[1]+1])

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