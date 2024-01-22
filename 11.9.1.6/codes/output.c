#include <stdio.h>

int main() {
    FILE *file = fopen("output.dat", "w");  // Open a text file for writing

    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;  // Return an error code
    }

    int x[11];
    float y[11];

    for (int i = 0; i < 11; i++) {
        x[i] = i;
        y[i] = (float)((x[i] + 1) * (x[i] + 1) * (x[i] + 1) + 5 * (x[i] + 1)) / 4;
    }

    // Use fprintf to write arrays to the file
    for (int i = 0; i < 11; i++) {
        fprintf(file, "%d %.2f\n", x[i], y[i]);
    }

    fclose(file);  // Close the file

    return 0;
}

