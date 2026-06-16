// Braulio Ronquillo
// Interval Scheduling

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

struct Job
{
    int id;
    int start;
    int finish;
};

struct CompareByFinish
{
    bool operator()(const Job &a, const Job &b) const
    {
        return a.finish < b.finish;
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;

    while (cin >> n)
    {
        vector<int> st(n);
        vector<int> ft(n);

        for (int i = 0; i < n; i++)
        {
            cin >> st[i];
        }

        for (int i = 0; i < n; i++)
        {
            cin >> ft[i];
        }

        vector<Job> jobs;

        for (int i = 0; i < n; i++)
        {
            Job job;
            job.id = i + 1;
            job.start = st[i];
            job.finish = ft[i];
            jobs.push_back(job);
        }

        stable_sort(jobs.begin(), jobs.end(), CompareByFinish());

        vector<int> selected;
        int lastFinish = -1;

        for (int i = 0; i < n; i++)
        {
            if (jobs[i].start >= lastFinish)
            {
                selected.push_back(jobs[i].id);
                lastFinish = jobs[i].finish;
            }
        }

        sort(selected.begin(), selected.end());

        cout << selected.size() << '\n';

        for (int i = 0; i < (int)selected.size(); i++)
        {
            if (i > 0)
            {
                cout << ' ';
            }
            cout << selected[i];
        }

        cout << '\n';
    }

    return 0;
}
