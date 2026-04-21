#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <deque>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::string mode;
    std::cin >> n >> mode;


    std::unordered_map<std::string, int> man_to_id, woman_to_id;
    std::vector<std::string> id_to_man(n), id_to_woman(n);

    std::vector<std::vector<std::string>> raw_proposer_prefs(n, std::vector<std::string>(n));
    std::vector<std::vector<std::string>> raw_receiver_prefs(n, std::vector<std::string>(n));

    if (mode == "m") {

        for (int i = 0; i < n; i++) {
            std::cin >> id_to_man[i];
            man_to_id[id_to_man[i]] = i;
            for (int j = 0; j < n; j++)
                std::cin >> raw_proposer_prefs[i][j];
        }
        for (int i = 0; i < n; i++) {
            std::cin >> id_to_woman[i];
            woman_to_id[id_to_woman[i]] = i;
            for (int j = 0; j < n; j++)
                std::cin >> raw_receiver_prefs[i][j];
        }
    } else {

        for (int i = 0; i < n; i++) {
            std::cin >> id_to_woman[i];
            woman_to_id[id_to_woman[i]] = i;
            for (int j = 0; j < n; j++)
                std::cin >> raw_proposer_prefs[i][j];
        }
        for (int i = 0; i < n; i++) {
            std::cin >> id_to_man[i];
            man_to_id[id_to_man[i]] = i;
            for (int j = 0; j < n; j++)
                std::cin >> raw_receiver_prefs[i][j];
        }
    }

    std::vector<std::vector<int>> proposer_pref(n, std::vector<int>(n));
    std::vector<std::vector<int>> receiver_rank(n, std::vector<int>(n));

    if (mode == "m") {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                proposer_pref[i][j] = woman_to_id[raw_proposer_prefs[i][j]];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                int man_id = man_to_id[raw_receiver_prefs[i][j]];
                receiver_rank[i][man_id] = j;
            }
    } else {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                proposer_pref[i][j] = man_to_id[raw_proposer_prefs[i][j]];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                int woman_id = woman_to_id[raw_receiver_prefs[i][j]];
                receiver_rank[i][woman_id] = j;
            }
    }

    std::vector<int> partner_of_receiver(n, -1);
    std::vector<int> partner_of_proposer(n, -1);
    std::vector<int> next_proposal(n, 0);

    std::deque<int> free_proposers;
    for (int i = 0; i < n; i++) free_proposers.push_back(i);

    while (!free_proposers.empty()) {
        int p = free_proposers.front();
        int r = proposer_pref[p][next_proposal[p]];
        next_proposal[p]++;

        if (partner_of_receiver[r] == -1) {
            // Receptor libre: acepta
            partner_of_receiver[r] = p;
            partner_of_proposer[p] = r;
            free_proposers.pop_front();
        } else {
            int current_p = partner_of_receiver[r];
            if (receiver_rank[r][p] < receiver_rank[r][current_p]) {
                // Receptor prefiere al nuevo proponente
                partner_of_receiver[r]        = p;
                partner_of_proposer[p]         = r;
                partner_of_proposer[current_p] = -1;
                free_proposers.pop_front();
                free_proposers.push_back(current_p);
            } else {
                // Receptor rechaza al nuevo proponente
                free_proposers.pop_front();
                free_proposers.push_back(p);
            }
        }
    }


    if (mode == "m") {
        for (int p = 0; p < n; p++)
            std::cout << id_to_man[p] << " " << id_to_woman[partner_of_proposer[p]] << "\n";
    } else {
        for (int p = 0; p < n; p++)
            std::cout << id_to_woman[p] << " " << id_to_man[partner_of_proposer[p]] << "\n";
    }

    return 0;
}

