#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        for(int i{0}; i < nums.size(); i++){
            for(int j{i+1}; j < nums.size(); j++){
                if (nums[i] + nums[j] == target)
                    return std::vector<int> {i, j};
            }
        }
    }
};

int main(){
    Solution testcase;
    std::vector<int> testvect{3,2,4};
    std::vector<int> test {testcase.twoSum(testvect, 6)};
    for(int i{0}; i<test.size(); i++)
        std::cout << test.at(i) << ' ';
};
