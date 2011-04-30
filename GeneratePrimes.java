import java.util.LinkedList;
import java.util.Queue;


public class GeneratePrimes {

	/**
	 * @param args
	 */
	
	public static Integer[] gen_primes(int lowerBound, int upperBound){
		
		//error checking, if we've got swapped upper and lowers, just switch them back around
		if (lowerBound > upperBound){
			int temp = lowerBound;
			lowerBound=upperBound;
			upperBound = temp;
		}
		
		//if there's no possible primes, just return an empty array
		if (upperBound < 2){
			return new Integer[0];
		}
		
		
		Queue<Integer> primeList = new LinkedList<Integer>();
		Queue<Integer> internalList = new LinkedList<Integer>();
		Integer currentInteger = 2;
		boolean isPrime = false; 
		while (currentInteger<lowerBound){
			isPrime = true;
			
			for (Integer p : internalList){
				if (currentInteger%p == 0){
					isPrime=false;
					break;
				}
			}
			if (isPrime){
				internalList.add(currentInteger);
			}
			currentInteger++;
			
		}
		
		
		while (currentInteger<=upperBound){
			isPrime = true;
			
			for (Integer p : internalList){
				if (currentInteger%p == 0){
					isPrime=false;
					break;
				}
			}
			
			if (isPrime){
				for (Integer p : primeList){
					if (currentInteger%p == 0){
						isPrime = false;
						break;
					}
				}
			}
			
			if (isPrime){
				primeList.add(currentInteger);
			}
			
			currentInteger++;
		}
		
		return primeList.toArray(new Integer[0]);
		
	}
	public static void main(String[] args) {
		
		if (args.length > 1){
			try {
				int l = Integer.parseInt(args[0]),u=Integer.parseInt(args[1]);
				for (int n : gen_primes(l,u)){
					System.out.println(n);
				}
			}
			catch (Exception e){
				//Invalid input is assumed to be the phrase "Let's see a demonstration"
				doTest();
			}
		}
		else {
			//Do a demonstration
			doTest();
		}
		
		
		
	}
	private static void doTest() {
		System.out.println("Primes from 2 to 10");
		for(int n:gen_primes(2,10)){
			System.out.print(n);
			System.out.print(',');
		}
		System.out.println();
		
		System.out.println("Primes from -2 to 0");
		for(int n:gen_primes(-2,0)){
			System.out.print(n);
			System.out.print(',');	
		}
		System.out.println();
		
		System.out.println("Primes from 10 to 100");
		for(int n:gen_primes(10,100)){
			System.out.print(n);
			System.out.print(',');	
		}
		System.out.println();
	}

}
