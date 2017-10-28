using System;

namespace csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            // print out a variable
            string helloString = "Hello World! as a varible";
            Console.WriteLine(helloString);

            // use string formatting
            string wrld = "World!";
            Console.WriteLine($"Hello {wrld}, we're doing string formatting");

            //more formatting
            string h = "Hello";
            Console.WriteLine(string.Format("{0} World", h));
        }
    }
}
