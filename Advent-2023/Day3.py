from icecream import ic

def allGears(lines):
    lista = []
    for i, line in enumerate(lines):
        # ic(line2)
        for j, symbol in enumerate(line):
            if symbol == "*":
                # append the location of the symbol
                lista.append((i, j))
    return lista

def solve(lines):
    nums = []
    for i, line in enumerate(lines):
        num = ""
        done = False
        checking = False
        for j, char in enumerate(line):
            if char.isdigit():
                checking = True
                num += char
                # check if the char is adjacent to a symbol, make done True
                if hasSymbolAdjacent(lines, j, i):
                    done = True
            else:
                if checking:
                    if done:
                        ic(num)
                        nums.append(int(num))
                    num = ""
                    done = False
                    checking = False
    return sum(nums)

def hasSymbolAdjacent(lines, col, row):
    # check if there is a symbol adjacent to the number, aka not a '.' or a number
    rows, cols = len(lines), len(lines[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if lines[new_row][new_col] not in [".", "\n"] and not lines[new_row][new_col].isdigit():
                ic(lines[new_row][new_col], new_row, new_col)
                return True
    return False

def hasGearAdjacent(lines, col, row):
    # check if there is a symbol adjacent to the number, aka not a '.' or a number
    rows, cols = len(lines), len(lines[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if lines[new_row][new_col] in ["*"]:
                ic(lines[new_row][new_col], new_row, new_col)
                return True, (new_row, new_col)
    return False, None

'''
Change way of thought

1. Iterate throught all characters until you find a number, where you store it in a string
2. Check if the number is adjacent to a symbol or a number *TO THE RIGHT*
3.1. If it is adjacent to a symbol, change a variable to True
3.2. If it is adjacent to a number, add the number to the string
4. If there is no more numbers to the right, check if the variable is True
4.1. If it is True, add it to the list of numbers
4.2. If it is False, continue
'''

def solve2(lines):
    nums = []
    gears = {}
    for i, line in enumerate(lines):
        num = ""
        gear = None
        done = False
        checking = False
        for j, char in enumerate(line):
            if char.isdigit():
                checking = True
                num += char
                # check if the char is adjacent to a symbol, make done True
                tmp, gear2 = hasGearAdjacent(lines, j, i)
                if tmp:
                    done = True
                    gear = gear2
            else:
                if checking:
                    if done:
                        ic(num)
                        if gear not in gears:
                            gears[gear] = []
                        gears[gear].append(int(num))
                        # nums.append(int(num))
                    num = ""
                    gear = None
                    done = False
                    checking = False
    ic(gears)
    for gear in gears:
        if len(gears[gear]) > 1:
            nums.append(gears[gear][0] * gears[gear][1])
    return sum(nums)
    
    

def readFile():
    file = open("Advent-2023/Day3Input.txt", "r")
    file2 = open("Advent-2023/test.txt", "r")
    lines = file.readlines()
    lines2 = file2.readlines()
    file.close()
    file2.close()
    return lines, lines2

if __name__ == "__main__":
    lines, lines2 = readFile()
    # ic(solve(lines))
    ic(solve2(lines))