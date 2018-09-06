using System;

namespace ConsoleApp1
{
    class Program
    {
        const string SOUNDFILE = @"c:/Users/wilso/Desktop/test.wav";
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            SoundPlayer.play(SOUNDFILE);
            Console.ReadKey();
        }
    }

    internal class SoundPlayer
    {
        public static bool play(string fileLocation)
        {
            try
            {
                System.Diagnostics.Process.Start(@"powershell", $@"-c (New-Object Media.SoundPlayer '{fileLocation}').PlaySync();");
                return true;
            }
            catch (Exception err)
            {
                Console.WriteLine("Failed to play Windows file at [" + fileLocation + "], error:\n" + err);
                return false;
            }
        }
    }
}