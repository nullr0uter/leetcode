// This is one of my first C# Solutions to Leetcode problem 1
// I´m starting to learn C#
// It´s insane how long C# code can be while the python version is about the half

using System;

public class Program
{
  public static void Main(string[] args)
  {
    Program p = new Program();
    int[] result = p.twoSum(new int[] {2, 7, 11, 15}, 9);
    Console.WriteLine($"[{result[0]}, {result[1]}]");
  }

  public int[] twoSum(int[] nums, int target)
  {
    Array.Sort(nums);
    int[] result = new int[2];
    int left = 0;
    int right = nums.Length - 1;
    while (left < right)
    {
      int tmp = nums[left] + nums[right];
      if (tmp == target) {
        result[0] = left;
        result[1] = right;
        break;
      } else if (tmp < target) {
        left++;
      } else if (tmp > target) {
        --right;
      } else {
        int[] noResult = {};
        return noResult;
      }
    }
    return result;
  }
}
