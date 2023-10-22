#include <string.h>
#include <stdio.h>

//"C:/Users/polil/CLionProjects/ITPAssignment/input.txt"
//"C:/Users/polil/CLionProjects/ITPAssignment/output.txt"
int main() {
    //reading the input file
    FILE *fi = fopen("input.txt", "r");
    //creating the output file
    FILE *fo = fopen("output.txt", "w");
    int n;
    //scanning number of lines n
    fscanf(fi, "%d", &n);
    //checking if the number of lines satisfy the condition given in the task
    if (n > 100 || n < 1) {
        fprintf(fo, "Error in the input.txt");
        fclose(fi);
        fclose(fo);
        return 0;
    }

    //creating an array for n lines of names
    char names[n][104];
    for (int i = 0; i < n; i++) {
        //scanning names
        fscanf(fi, "%s", names[i]);
        //checking if there is an empty string
        if (strlen(names[i]) == 0) {
            fprintf(fo, "Error in the input.txt");
            fclose(fi);
            fclose(fo);
            return 0;
        }
        //checking if every string starts with capital letter
        if (!(names[i][0] >= 65 && names[i][0] <= 90)) {
            fprintf(fo, "Error in the input.txt");
            fclose(fi);
            fclose(fo);
            return 0;
        }

        //checking if names contain not lowercase letters
        for (int j = 1; j < strlen(names[i]); j++) {
            if (!(names[i][j] >= 97 && names[i][j] <= 122)) {
                fprintf(fo, "Error in the input.txt");
                fclose(fi);
                fclose(fo);
                return 0;
            }
        }
    }
    //creating new string for sorting the array of names
    char vr[104];
    //sorting array of names in non-descending order
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            //if the next string is bigger than current, swap these strings
            if (strcmp(names[j], names[j + 1]) > 0) {
                strcpy(vr, names[j]);
                strcpy(names[j], names[j + 1]);
                strcpy(names[j + 1], vr);
            }
        }
    }
    //writing result in output file
    fclose(fi);
    fclose(fo);
}
