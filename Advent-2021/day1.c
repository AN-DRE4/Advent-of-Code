#include <stdio.h>
#include <stdlib.h>

void day1part1() {
    FILE *inp = fopen("advent_input/day1.txt", "r");
    if (inp == NULL) {
        printf("File not found!!\n");
        }
    else {
        int max_size = 50000;
        int a = 0;
        int *tmp = malloc(max_size);
        int numb1 = 0;
        while (fscanf(inp, "%d", tmp) != EOF) {
            if (numb1 != 0) {
                if (numb1 < *tmp) {
                    a++;
                }
            }
            numb1 = *tmp;
        }
        printf("%d\n", a);
    }
    fclose(inp);
}

void day1part2() {
    FILE *inp = fopen("advent_input/day1.txt", "r");
    if (inp == NULL) {
        printf("File not found!!");
        }
    else {
        int max_size = 50000;
        int a = 0;
        int *tmp = malloc(max_size);
        int numb1 = 0, numb2 = 0, numb3 = 0;
        while (fscanf(inp, "%d", tmp) != EOF) {
            if ((numb1 != 0) && (numb2 != 0) && (numb3 != 0)) {
                if (numb1 < *tmp) {
                    a++;
                }
            }
            if (numb1 == 0) numb1 = *tmp;
            else if (numb2 == 0) {numb2 = *tmp;}
            else if (numb3 == 0) {numb3 = *tmp;}
            else {numb1 = numb2; numb2 = numb3; numb3 = *tmp;}
        }
        printf("%d\n", a);
    }
    fclose(inp);
}

int main() {
    day1part1();
    day1part2();
    return 0;
}
