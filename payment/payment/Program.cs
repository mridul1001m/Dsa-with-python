using System;

namespace payment
{
    
    interface Ipayment
    {
        void Makepayment(double amount);
    }

    class Creditcard : Ipayment
    {
        public void Makepayment(double amount)
        {
            Console.WriteLine($"INR {amount} done through credit card");
        }
    }

    class Paypal : Ipayment
    {
        public void Makepayment(double amount)
        {
            Console.WriteLine($"INR {amount} done through paypal");
        }
    }

    class UPI : Ipayment
    {
        public void Makepayment(double amount)
        {
            Console.WriteLine($"INR {amount} done through upi");
        }
    }

    class mainprogram
    {
        static void Main(string[] args)
        {
            Ipayment payment;

            payment = new Creditcard();
            payment.Makepayment(2000.00);

            payment = new Paypal();
            payment.Makepayment(1500.50);

            payment = new UPI();
            payment.Makepayment(1000.75);
        }
    }
}
