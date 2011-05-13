using System;
using System.Collections;
using System.Collections.Generic;

namespace csprimes
{
	public class PrimeEnumerator : IEnumerable<int>
	{
		Queue<int> primes = new Queue<int>();
		int current = 2;
		int start = 2;
		int limit=-1;
		public PrimeEnumerator (){
			
		}
		
		public PrimeEnumerator (int prime_limit){
				limit=prime_limit;
		}
		
		public PrimeEnumerator (int prime_limit, int start){
			if (start < 2){
				start = 2;
			}
			this.start = start;
			limit = prime_limit;
			
		}
		
		public IEnumerator<int> GetEnumerator() {
			while (true){
				bool IsPrime = true;
				
				if (limit != -1){
					if (current > limit) {
						return false;//throw new InvalidOperationException ("Took it to the limit, 1 too many times");
					}
				}
				
				foreach (int prime in primes){
					if (current % prime == 0){
						IsPrime = false;
						break;
					}
				}
				
				if (IsPrime) {
					primes.Enqueue(current);
					if (current >= start){
						yield return current;
					}
				}
				current++;
			}
		}
		
		IEnumerator IEnumerable.GetEnumerator() {
			return GetEnumerator ();
		}
		
		
		
	}

	class MainClass
	{
		public static void Main (string[] args)
		{
			PrimeEnumerator p = new PrimeEnumerator(10);
			var enumer = p.GetEnumerator();
			System.Console.WriteLine("Generating primes from 1 to 10");
			while (enumer.MoveNext()){
				Console.WriteLine(enumer.Current);	
			}
			
			
			p = new PrimeEnumerator(2,-10);
			enumer = p.GetEnumerator();
			System.Console.WriteLine("Generating primes from -10 to 2");
			while (enumer.MoveNext()){
				Console.WriteLine(enumer.Current);	
			}
			
			
			p = new PrimeEnumerator(-10,-100);
			enumer = p.GetEnumerator();
			System.Console.WriteLine("Generating primes from -100 to -10");
			while (enumer.MoveNext()){
				Console.WriteLine(enumer.Current);	
			}
			
			
			p = new PrimeEnumerator(1100,1000);
			enumer = p.GetEnumerator();
			System.Console.WriteLine("Generating primes from 1000 to 1100");
			while (enumer.MoveNext()){
				Console.WriteLine(enumer.Current);	
			}
			
			
			p = new PrimeEnumerator(-100,100);
			enumer = p.GetEnumerator();
			System.Console.WriteLine("Generating primes from 100 to -100");
			while (enumer.MoveNext()){
				Console.WriteLine(enumer.Current);	
			}
			
		}
	}
}

