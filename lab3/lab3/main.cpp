#include <iostream>
#include <random>

using namespace std;

extern "C" double f(double);

double inverse_cumulative_distribution(double arg, double rangeMin, double rangeMax)
{
    return (rangeMax - rangeMin) * arg + rangeMin;
}

int elimination_method(double chance)
{
    if (chance <= 20.0)         // 20%
    {
        return 1;
    }
    else if (chance <= 50.0)    // 30%
    {
        return 2;
    }
    else if (chance <= 90.0)     // 40%
    {
        return 3;
    }
    else                          // 10%
    {
        return 4;
    }
}

void printStats(int stats[], int size, int step)
{
    for (int i = 0; i < size; i++)
    {
        cout << (i + 1) * step << ": " << stats[i];
        cout << "\n";
    }
}

void printStats(int stats1[], int stats2[], int size, int step1, double step2)
{
    for (int i = 0; i < size; i++)
    {
        cout << i * step1 << " -> " << (i + 1) * step1 << ": " << stats1[i];
        cout << " vs ";
        cout << double(i) * step2 << " -> " << (double(i) + 1) * step2 << ": " << stats2[i];
        cout << "\n";
    }
}


int main()
{
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> dis(0.0, 1.0);
    const int testCases = 10;

    int inverse_cumulative_distribution_stats[10] = { 0 };
    int distribution_stats[10] = { 0 };
    for (int i = 0; i < testCases; i++)
    {
        double t = dis(gen);
        double t1 = inverse_cumulative_distribution(t, 50, 150);
        double t1_asm = f(t);
        cout << i << ": " << t << " -> " << t1 << " from ASM: " << t1_asm << "\n";
        inverse_cumulative_distribution_stats[(int(t1) - 50) / 10]++;
        distribution_stats[int(t * 10)]++;
    }
    printStats(inverse_cumulative_distribution_stats, distribution_stats, 10, 10, 0.1);

    cout << "\n\n";
    int elimination_method_stats[4] = { 0 };
    for (int i = 0; i < testCases; i++)
    {
        double chance = dis(gen) * 100;   // chance in %
        int v = elimination_method(chance);
        cout << i << ": " << v << " with chance: " << chance << " % " << "\n";
        elimination_method_stats[v - 1]++;
    }
    printStats(elimination_method_stats, 4, 1);

    return 0;
}