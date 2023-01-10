#include <bits/stdc++.h>
using namespace std;

class Meva
{
protected:
    string navi;
    int yashash_davri;
    bool yesa_boladimi;
    bool shirinmi;
};

class Olma :
    private Meva
{
private:
    string rangi;
    int narxi;
    bool pishganmi;
    double massasi;
public:
    Olma(string navi, string rangi, int narxi, double massasi, int yashash_davri, bool yesa_boladimi, bool shirinmi, bool pishganmi):
        rangi(rangi), narxi(narxi), pishganmi(pishganmi), massasi(massasi)
        {
            this->navi = navi;
            this->shirinmi = shirinmi;
            this->yashash_davri = yashash_davri;
            this->yesa_boladimi = yesa_boladimi;
        }
    void showInfo()
    {
        cout << std::boolalpha;
        cout << "navi: " << this->navi << endl;
        cout << "yashash davri: " << this->yashash_davri << endl;
        cout << "yesa_boladimi: " << this->yesa_boladimi << endl;
        cout << "shirinmi: " << this->shirinmi << endl;
        cout << "Rangi: " << this->rangi << endl;
        cout << "Narxi: " << this->narxi << endl;
        cout << "Pishganmi: " << this->pishganmi << endl;
        cout << "Massasi: " << this->massasi << endl;
    }
};


int main()
{
    Olma yashil_olma("Zlyonka", "Yashil", 1200, 300, 25, true, false, true);
    yashil_olma.showInfo();
}
