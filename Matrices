//Polina Pushkareva
//p.pushkareva@innopolis.university
#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
using namespace std;
//class Matrix
class Matrix {
private:
    int n,m;
    double ** table;
public:
    //matrix creation
    void create()
    {
        table = new double * [n];

        for (int i = 0; i < n; i++)
            table[i] = new double [m];
    }
    //setting matrix elements from the input
    void setElements()
    {
        //special case for vector
        if(m==0) {
            for(int i=0; i<n; i++)
                cin>>table[i][0];
        }
        else {
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    cin >> table[i][j];
        }
    }
    //function for outputting the matrix
    void display()
    {
        //special case for vector
        if(m==0) {
            for(int i=0; i<n; i++) {
                //changing -0 to 0 if its needed
                if(round(table[i][0]*100)/100==-0.00) {
                    table[i][0]=0.00;
                }
                //outputting with two signs after .
                cout<<fixed<<setprecision(2)<<table[i][0]<<endl;
            }
        }
        else {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if(round(table[i][j]*100)/100==-0.00) {
                        table[i][j]=0.00;
                    }
                    cout << fixed << setprecision(2) << table[i][j];
                    if (j != (m - 1)) {
                        cout << " ";
                    }
                }
                cout << endl;
            }
        }
    }
    int getN()
    {
        return n;
    };
    int getM()
    {
        return m;
    };
    Matrix() {
        int n = 0;
        int m = 0;
        int arr = 0;
    }

    Matrix(int n, int m)
    {
        this->n = n;
        this->m = m;
        create();
    }
    //overloaded assigning operator
    friend int operator ==(Matrix& A, Matrix& B) {
        int n1 = A.getN();
        int m1 = A.getM();
        int n2 = B.getN();
        int m2 = B.getM();
        if (n1 != n2 || m1 != m2) {
            cout << "Error: the dimensional problem occurred" << endl;
        } else {
            for (int i = 0; i < n1; i++)
                for (int j = 0; j < m1; j++)
                    A.table[i][j]=B.table[i][j];
        }
        return 0;
    }
    //overloaded operator for matrix summation
    friend int operator +(Matrix& A, Matrix& B) {
        int n1 = A.getN();
        int m1 = A.getM();
        int n2 = B.getN();
        int m2 = B.getM();
        if (n1 != n2 || m1 != m2) {
            cout << "Error: the dimensional problem occurred" << endl;
        } else {
            for (int i = 0; i < n1; i++) {
                for (int j = 0; j < m1; j++) {
                    cout << A.table[i][j] + B.table[i][j];
                    if(j!=(m1-1)) {
                        cout<<" ";
                    }
                }
                cout << endl;
            }
        }
        return 0;
    }
    //overloaded operator for matrix subtraction
    friend int operator - (Matrix& A, Matrix& B)
    {
        int n1 = A.getN();
        int m1 = A.getM();
        int n2 = B.getN();
        int m2 = B.getM();
        if(n1!= n2 || m1!= m2) {
            cout<<"Error: the dimensional problem occurred"<<endl;
        } else {
            for (int i = 0; i < n1; i++) {
                for (int j = 0; j < m1; j++) {
                    cout << A.table[i][j] - B.table[i][j];
                    if(j!=(m1-1)) {
                        cout<<" ";
                    }
                }
                cout << endl;
            }
        }
        return 0;
    }
    //overloaded operator for matrix multiplication
    friend Matrix operator *(Matrix& B, Matrix& A)
    {
        int n2 = B.getN();
        int m2 = B.getM();
        int n1 = A.getN();
        int m1 = A.getM();
        Matrix matrix(n2, m1);
        if(m2!= n1) {
            cout<<"Error: the dimensional problem occurred"<<endl;
        } else if(m1==0) {
            for (int i = 0; i < n2; i++) {
                matrix.table[i][0]=0;
                for(int k = 0;k < m2;k++) {
                    matrix.table[i][0] = matrix.table[i][0] + B.table[i][k] * A.table[k][0];
                }
            }
        }else {
            for (int i = 0; i < n2; i++) {
                for (int j = 0; j < m1; j++) {
                    matrix.table[i][j]=0;
                    for(int k = 0;k < m2;k++) {
                        matrix.table[i][j] = matrix.table[i][j] + B.table[i][k] * A.table[k][j];
                    }
                }
            }
        }
        return matrix;
    }
    //function for matrix determinant
    void transpose () {
        for (int i = 0; i < m;i++) {
            for(int j = 0; j < n; j++){
                cout<<table[j][i];
                if(j!=(n-1)) {
                    cout<<" ";
                }
            }
            cout<<endl;
        }
    }
    //function for performing elimination
    void determinant(Matrix a) {
        int step=1, permutation =0;
        int n =a.getN();
        Matrix A=a;
        Matrix e(n, n);
        //firstly, we reduce the matrix to upper triangular
        for(int i=0; i<n; i++) {
            double max=abs(A.table[i][i]);
            int str;
            for(int j=i; j<n; j++) {
                if(abs(A.table[j][i])>max) {
                    max=abs(A.table[j][i]);
                    str=j;
                }
            }
            if(max!=abs(A.table[i][i])) {
                permutation++;
                cout<<"step: permutation"<<endl;
                step++;
                for(int j=0; j<n; j++) {
                    for(int k=0; k<n; k++) {
                        if(k==j && k!=i && k!=str) {
                            e.table[j][k]=1;
                        } else{
                            e.table[j][k]=0;
                        }
                    }
                }
                e.table[str][i]=1;
                e.table[i][str]=1;
                A=e*A;
                for(int i=0; i<n; i++) {
                    for(int j=0; j<n; j++) {
                        if(abs(A.table[i][j])< pow(10, -10)) {
                            A.table[i][j]=0;
                        }
                    }
                }
                A.display();
            }
            for (int j = 1; j < n; j++) {
                if (i < j) {
                    double c = -1 * A.table[j][i] / A.table[i][i];
                    //computing elimination matrix
                    for (int k = 0; k < n; k++) {
                        for (int l = 0; l < n; l++) {
                            if (k == l) {
                                e.table[k][l] = 1;
                            } else {
                                e.table[k][l] = 0;
                            }
                        }
                    }
                    e.table[j][i] = c;
                    //performing multiplication of a matrix and a vector by elimination matrix
                    A = e * A;
                    for(int i=0; i<n; i++) {
                        for(int j=0; j<n; j++) {
                            if(abs(A.table[i][j])< pow(10, -10)) {
                                A.table[i][j]=0;
                            }
                        }
                    }
                    cout<<"step: elimination"<<endl;
                    step++;
                    A.display();
                }
            }
        }
        double answer=1;
        for(int i=0; i<n; i++) {
            answer*=A.table[i][i];
        }
        if(permutation%2!=0) {
            answer*=-1;
        }
        cout<<"result:"<<endl<<fixed<<setprecision(2)<<answer;
    }
};
ostream& operator <<(ostream& out, Matrix& m)
{
    m.display();
    return (out);
}

istream& operator >>(istream& in, Matrix& m)
{
    m.setElements();
    return (in);
}

int main() {
    //scanning n
    int n;
    cout<<"Input the dimensions of a matrix:"<<endl<<"n: ";
    cin>>n;
    cout<<"Input n*n elements of a matrix:"<<endl;
    //declaring and scanning matrix A
    Matrix matrixA(n,n);
    cin>>matrixA;
    matrixA.determinant(matrixA);
    return 0;
}
