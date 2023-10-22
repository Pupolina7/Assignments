//Polina Pushkareva
//p.pushkareva@innopolis.university
#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <cstdio>
#include <random>

using namespace std;


int main() {
    FILE *pipe = _popen("D:\\gnuplot\\bin\\gnuplot -persist", "w");
    if(pipe!= nullptr) {
        int v0, k0;
        cin >> v0 >> k0;
        double a1, a2, b1, b2, T, N;
        cin >> a1 >> b1 >> a2 >> b2 >> T >> N;
        double t = T / N;
        cout << "t:" << endl;
        vector<double> time;
        double j = 0;
        while (j <= T) {
            time.push_back(j);
            cout << fixed << setprecision(2) << j << " ";
            j += t;
        }
        vector<double> victims;
        fprintf(pipe, "plot[0:10][0:10]'-' using 1:2 with lines title 'v(t)', '-' using 1:2 with lines title 'k(t)'\n");
        cout << endl << "v:" << endl;
        for (double i: time) {
            double v = ((v0 - (a2 / b2)) * cos(sqrt(a1 * a2) * i)) -
                       ((k0 - (a1 / b1)) * sqrt(a2) * b1 * sin(sqrt(a1 * a2) * i) / (b2 * sqrt(a1)));
            v += (a2 / b2);
            victims.push_back(v);
            fprintf(pipe, "%f\t%f\n", i, v);
            cout << v << " ";
        }
        fprintf(pipe, "e\n");
        cout << endl << "k:" << endl;
        vector<double> killers;
        for (double i: time) {
            double k = ((v0 - (a2 / b2)) * sqrt(a1) * b2 * sin(sqrt(a1 * a2) * i)) / (b1 * sqrt(a2)) +
                       (k0 - a1 / b1) * cos(sqrt(a1 * a2) * i);
            k += (a1 / b1);
            killers.push_back(k);
            fprintf(pipe, "%f\t%f\n", i, k);
            cout << k << " ";
        }
        fprintf(pipe, "e\n");
    }
    return 0;
}
