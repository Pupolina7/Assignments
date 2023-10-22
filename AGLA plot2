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
    FILE *pipe = _popen(R"(D:\\gnuplot\\bin\\gnuplot -persist)", "w");
    FILE *pipe11 = _popen(R"(D:\\gnuplot\\bin\\gnuplot -persist)", "w");
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
        fprintf(pipe, "set xlabel 'time'\n");
        fprintf(pipe, "set ylabel 'Prey'\n");
        fprintf(pipe, "plot[0:10][0:10]'-' using 1:2 with lines title 'v(t)', '-' using 1:2 with lines title 'k(t)'\n");
        fprintf(pipe11, "plot[0:10][0:10]'-' using 1:2 with lines title 'v(k)' lc 2\n");
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
//        fprintf(pipe, "set xlabel 'Prey'\n");
//        fprintf(pipe, "set ylabel 'Predator'\n");
//        fprintf(pipe, "plot[0:10][0:10]'-' using 1:2 with lines title 'Predator-Prey model'\n");
//        fprintf(pipe, "set xlabel 'time'\n");
//        fprintf(pipe, "set ylabel 'Predator'\n");
        vector<double> killers;
        for (double i: time) {
            double k = ((v0 - (a2 / b2)) * sqrt(a1) * b2 * sin(sqrt(a1 * a2) * i)) / (b1 * sqrt(a2)) +
                       (k0 - a1 / b1) * cos(sqrt(a1 * a2) * i);
            k += (a1 / b1);
            killers.push_back(k);
//            fprintf(pipe11, "%f\t%f\n", victims[killers.size()-1], k);
            fprintf(pipe, "%f\t%f\n", i, k);
            cout << k << " ";
        }
        fprintf(pipe, "e\n");
        for(int i = 0; i < killers.size(); i++)
        {
            fprintf(pipe11, "%f\t%f\n", killers[i], victims[i]);
        }
        fprintf(pipe11, "e\n");
    }
    return 0;
}
