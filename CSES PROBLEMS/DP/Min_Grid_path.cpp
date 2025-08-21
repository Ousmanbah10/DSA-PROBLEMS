#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<string> grid(n);
    for (int i = 0; i < n; i++) {
        cin >> grid[i];
    }
    
    // dp[i][j] = lexicographically smallest string from (i,j) to (n-1,n-1)
    vector<vector<string>> dp(n, vector<string>(n));
    
    // Fill from bottom-right to top-left
    dp[n-1][n-1] = grid[n-1][n-1];
    
    // Fill last row (can only go right)
    for (int j = n-2; j >= 0; j--) {
        dp[n-1][j] = grid[n-1][j] + dp[n-1][j+1];
    }
    
    // Fill last column (can only go down)
    for (int i = n-2; i >= 0; i--) {
        dp[i][n-1] = grid[i][n-1] + dp[i+1][n-1];
    }
    
    // Fill the rest
    for (int i = n-2; i >= 0; i--) {
        for (int j = n-2; j >= 0; j--) {
            string right = grid[i][j] + dp[i][j+1];
            string down = grid[i][j] + dp[i+1][j];
            
            if (right < down) {
                dp[i][j] = right;
            } else {
                dp[i][j] = down;
            }
        }
    }
    
    cout << dp[0][0] << endl;
    
    return 0;
}