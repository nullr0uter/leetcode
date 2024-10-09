#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> twoSum(std::vector<int> nums, int target) {
  std::vector<int> result{};
  std::sort(nums.begin(), nums.end());
  std::cout << "Sorted: {";
  for (size_t i = 0; i < nums.size(); i++) {
    std::cout << nums[i];
    if (i != nums.size() - 1) {
      std::cout << ",";
    }
  }
  std::cout << "}\nTarget: " << target << std::endl;
  int left = 0;
  int right = nums.size() - 1;
  while (left < right) {
    int tmp = nums[left] + nums[right];
    if (tmp == target) {
      result.push_back(left);
      result.push_back(right);
      break;
    } else if (tmp < target) { left++; }
    else if (tmp > target) { right--; }
    else { return {}; }
  }
  return result;
}

int main() {
  std::vector<int> nums = {2,3,6,4,1,7};
  int target = 9;
  std::vector<int> result = twoSum(nums, target);
  std::cout << "Result: {";
  for (size_t i = 0; i < result.size(); i++) {
    std::cout << result[i];
    if (i != result.size() - 1) {
      std::cout << ",";
    }
  }
  std::cout << "}" << std::endl;
  return 0;
}
