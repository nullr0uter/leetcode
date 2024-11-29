// This is one of my first C# Solutions to Leetcode problem 1
// I´m starting to learn C#
// It´s insane how long C# code can be while the python version is about the half

using System;

namespace TwoSumCS
{
    class Program
    {
        static void Main(string[] args)
        {
            Program program = new Program();
            int[] nums = new int[5] { 2, 3, 5, 9, 4 };
            int target = 6;
            int[] result = new int[2];
            result = program.twoSum(nums, target);
            program.printResult(nums, target, result);
        }
        private int[] twoSum(int[] nums, int target)
        {
            int[] result = new int[2];
            Array.Sort(nums);
            int left = 0;
            int right = nums.Length - 1;
            while (left < right)
            {
                int tmp = nums[left] + nums[right];
                if (tmp == target)
                {
                    result[0] = left + 1;
                    result[1] = right + 1;
                    break;
                }
                else if (tmp < target)
                {
                    left++;
                }
                else if (tmp > target)
                {
                    right--;
                }
                else
                {
                    int[] none = new int[0];
                    return none;
                }
            }
            return result;
        }
        private void printResult(int[] nums, int target, int[] result)
        {
            Array.Sort(nums);
            Console.Write("Sorted: {");
            for (int i = 0; i < nums.Length; i++)
            {
                Console.Write(nums[i]);
                if (i != nums.Length - 1)
                {
                    Console.Write(",");
                }
            }
            Console.WriteLine("}");
            Console.WriteLine("Target: {0}", target);
            Console.Write("Result: {");
            for (int i = 0; i < result.Length; i++)
            {
                Console.Write(result[i]);
                if (i != result.Length - 1)
                {
                    Console.Write(",");
                }
            }
            Console.WriteLine("}");
        }
    }
}
