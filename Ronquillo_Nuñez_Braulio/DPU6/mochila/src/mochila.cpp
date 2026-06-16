// Author: Ronquillo Nunez Braulio
// Knapsack 0-1 (mochila)

#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>
using namespace std;

pair<int, vector<int>> knapsack(int capacity, const vector<pair<int, int>> &items)
{
    int itemCount = (int)items.size();
    vector<vector<int>> dp(itemCount + 1, vector<int>(capacity + 1, 0));

    for (int i = 1; i <= itemCount; i++)
    {
        int value = items[i - 1].first;
        int weight = items[i - 1].second;

        for (int currentCapacity = 0; currentCapacity <= capacity; currentCapacity++)
        {
            dp[i][currentCapacity] = dp[i - 1][currentCapacity];

            if (weight <= currentCapacity)
            {
                int candidate = dp[i - 1][currentCapacity - weight] + value;

                if (candidate > dp[i][currentCapacity])
                {
                    dp[i][currentCapacity] = candidate;
                }
            }
        }
    }

    vector<int> selectedItems;
    int currentCapacity = capacity;

    for (int i = itemCount; i >= 1; i--)
    {
        if (dp[i][currentCapacity] != dp[i - 1][currentCapacity])
        {
            int weight = items[i - 1].second;
            selectedItems.push_back(i);
            currentCapacity -= weight;
        }
    }

    sort(selectedItems.begin(), selectedItems.end());
    return {dp[itemCount][capacity], selectedItems};
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int itemCount;
    int capacity;

    while (cin >> itemCount >> capacity)
    {
        vector<pair<int, int>> items;
        items.reserve(itemCount);

        for (int i = 0; i < itemCount; i++)
        {
            int value;
            int weight;
            cin >> value >> weight;
            items.push_back({value, weight});
        }

        pair<int, vector<int>> answer = knapsack(capacity, items);

        cout << answer.first << '\n';

        for (int i = 0; i < (int)answer.second.size(); i++)
        {
            if (i > 0)
            {
                cout << ' ';
            }
            cout << answer.second[i];
        }
        cout << '\n';
    }

    return 0;
}
