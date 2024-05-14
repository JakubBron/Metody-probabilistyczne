#include <iostream>
#include <iomanip>
#include <random>
#include <map>
using namespace std;

pair<int, int> generate(uniform_real_distribution<double>& gen, default_random_engine& rng) {
    double x = gen(rng);
    double y;
    pair<int, int> result;
    
    // generte x using marginal distribution
    if (x < 0.5)
    {
        result.first = 1;
    }
    else if (x < 0.7)
    {
        result.first = 2;
    }
    else if (x < 0.9)
    {
        result.first = 3;
    }
    else
    {
        result.first = 4;
    }

    // generate y
    if (result.first == 1) 
    {
        y = gen(rng);
        
        if (y < 0.2)    // why 0.2?
        {
            result.second = 1;
        }
        else
        {
            result.second = 4;
        }
    }
    else if (result.first == 2) 
    {
        result.second = 1;
    }
    else if (result.first == 3) 
    {
        y = gen(rng);

        if (y < 0.5)
        {
            result.second = 2;
        }
        else
        {
            result.second = 4;
        }
    }
    else 
    {
        result.second = 3;
    }
    return result;
}

int main(int argc, char* argv[])
{
    random_device rd;
    default_random_engine rng(rd());
    uniform_real_distribution<double> gen(0.0, 1.0);
    int n = 100000;
    pair<short, short> p;
    int stats[4][4] = {0};

    if(argc > 1)
    {
        n = atoi(argv[1]);
    }

    for(int i=0; i<n; i++)
    {
        p = generate(gen, rng);
        stats[p.first-1][p.second-1]++;
    }   


    cout << "Distribution of n = " << n << " samples: \n";
    double percent;
    cout << "  |";
    for(int i=0; i<4; i++)
    {
        cout << left<<" "<<setw(19) << i+1;
        if(i < 3)
        {
            cout << " |";
        }
    }
    cout << "\n";
    for(int i=0; i<4; i++)
    {
        cout << (i+1) << " | ";
        for(int j=0; j<4; j++)
        {
            percent = double(stats[i][j])/n*100;
            printf("%-10d", stats[i][j]);
            printf("(%-6.2f%)", percent);
            if(j < 3)
            {
                cout << " | ";
            }
        }
        cout << endl;
    }   
    return 0;
}