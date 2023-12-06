from icecream import ic

def gameIds(lines, numRed, numBlue, numGreen):
    total = 0
    for line in lines:
        line = line.strip()
        game, rest = line.split(":")

        name, id = game.split(" ")

        sets = rest.split(";")

        pause = False
        for set in sets:
            if pause:
                break
            gotten = set.split(", ")
            for get in gotten:
                get = get.strip()
                num, color = get.split(" ")
                if color == "red" and int(num) > numRed:
                    pause = True
                    break
                elif color == "blue" and int(num) > numBlue:
                    pause = True
                    break
                elif color == "green" and int(num) > numGreen:
                    pause = True
                    break
        if not pause:
            total += int(id)
    return total

def gameIds2(lines):
    total = 0
    for line in lines:
        line = line.strip()
        game, rest = line.split(":")

        name, id = game.split(" ")

        sets = rest.split(";")

        maxRed = 0
        maxBlue = 0
        maxGreen = 0

        for conjunto in sets:
            gotten = conjunto.split(",")
            for get in gotten:
                get = get.strip()
                num, color = get.split(" ")
                if color == "red" and int(num) > maxRed:
                    maxRed = int(num)
                elif color == "blue" and int(num) > maxBlue:
                    maxBlue = int(num)
                elif color == "green" and int(num) > maxGreen:
                    maxGreen = int(num)
        power = maxRed * maxBlue * maxGreen
        total += power            
    return total

def readFile():
    file = open("Day2Input.txt", "r")
    # file = open("test.txt", "r")
    lines = file.readlines()
    file.close()
    return lines

if __name__ == "__main__":
    lines = readFile()
    ic(gameIds2(lines))