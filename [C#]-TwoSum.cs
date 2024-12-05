// This is one of my first C# Solutions to Leetcode problem 1
// I´m starting to learn C#
// It´s insane how long C# code can be while the python version is about the half

using System;
using System.Linq;
using System.Collections.Generic;

namespace TwoSumProgram
{
    public class Program
    {
        public static void Main()
        {
            Program program = new Program();
            List<int> nums = new List<int> {2,4,6,4,7};
            int target = 8;
            List<int> result = new List<int>();
            result = program.twoSum(nums, target);
            program.printResult(nums, target, result);
        }
        private List<int> twoSum(List<int> nums, int target)
        {
            List<int> result = new List<int>();
            nums.Sort();
            int left = 0; int right = nums.Count - 1;
            while (left < right)
            {
                int tmp = nums[left] + nums[right];
                if (tmp == target) {
                    result.Add(left);
                    result.Add(right);
                    break;
                } else if (tmp < target) { left++; }
                else if (tmp > target) { right--; }
                else {
                    return Enumerable.Empty<int>().ToList();
                }
            }
            return result;
        }
        private void printResult(List<int> nums, int target, List<int> result)
        {
            nums.Sort();
            Console.Write("Sorted: {");
            for (int i = 0; i < nums.Count; i++)
            {
                Console.Write(nums[i]);
                if (i != nums.Count - 1)
                {
                    Console.Write(",");
                }
            }
            Console.Write("}");
            Console.WriteLine("\nTarget: {0}", target);
            if (result.Count == 2) {
                Console.Write("Result: {");
                for (int i = 0; i < result.Count; i++)
                {
                    Console.Write(result[i]);
                    if (i != result.Count - 1)
                    {
                        Console.Write(",");
                    }
                }
                Console.Write("}");
            } else {
                Console.WriteLine("Result: Keine Lösung gefunden.");
            }
        }
    }
}
