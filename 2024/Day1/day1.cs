using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace adventOfCodeTest
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string filePath = "C:\\Users\\ethan\\source\\repos\\adventOfCodeTest\\input1.txt";
            List<int> list1 = new List<int>();
            List<int> list2 = new List<int>();
            try
            {
                string[] lines = File.ReadAllLines(filePath);

                foreach (string line in lines)
                {
                    string[] parts = line.Split(new[] { ' ', '\t' }, StringSplitOptions.RemoveEmptyEntries);

                    if (parts.Length == 2 && int.TryParse(parts[0], out int num1) && int.TryParse(parts[1], out int num2))
                    {
                        list1.Add(num1);
                        list2.Add(num2);
                    }
                    else
                    {
                        Console.WriteLine($"Invalid line: {line}");
                    }
                }

                list1.Sort();
                list2.Sort();

                int sum = 0;

                for (int i = 0; i < list1.Count; i++)
                {
                    int difference = Math.Abs(list1[i] - list2[i]);
                    sum += difference;
                }

                Console.WriteLine(sum);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error reading file: {ex.Message}");
            }
        }
    }
}
