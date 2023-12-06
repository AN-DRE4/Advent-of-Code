from icecream import ic



def readFile():
    file = open("Day2Input.txt", "r")
    # file = open("test.txt", "r")
    lines = file.readlines()
    file.close()
    return lines

if __name__ == "__main__":
    lines = readFile()
    ic(gameIds2(lines))