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

                Dictionary<int, int> countDict2 = new Dictionary<int, int>();
                foreach (int number in list2)
                {
                    if (countDict2.ContainsKey(number))
                    {
                        countDict2[number]++;
                    }
                    else
                    {
                        countDict2[number] = 1;
                    }
                }

                int totalSimilarityScore = 0;

                for (int i = 0; i < list1.Count; i++)
                {
                    int similarityScore = 0;
                    if (countDict2.ContainsKey(list1[i]))
                    {
                        similarityScore = list1[i] * countDict2[list1[i]];
                    }
                    totalSimilarityScore += similarityScore;
                }

                Console.WriteLine(totalSimilarityScore);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error reading file: {ex.Message}");
            }
        }
    }
}
