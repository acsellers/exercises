using System;
using System.IO;
using System.Collections;

namespace csactivity
{
	class Activity {
		
		string name;
		int worth;
		
		public Activity(string def){
			name = def.Split(' ',1)[0];	
			worth = new Parse(def.Split(' ',1)[1]);
		}
		public int get_value(){
			return worth;
		}
		public string get_name(){
			return name;	
		}
	}
	class MainClass
	{
		var dict = new Dictionary<int,string> ();
		ArrayList positive = new ArrayList<Activity> ();
		ArrayList negative = new ArrayList<Activity> ();
		public bool check(int level){
			if (level <= this.positive.Count) {
				foreach (string s in recurse_select(level, true)) {
					
				}
			}
			if (level <= this.negative.Count) {
				foreach (string s in recurse_select(level, true)) {
					
				}
			}
		}
		
		public ArrayList<string> recurse_select(int item_number, bool isPositive) {
			
		}
		public ArrayList<string> do_recurse_select(int start_number, int level, bool isPositive) {
			ArrayList output = new ArrayList<string> ();
			var array = this.negative;
			if (isPositive){
				array = this.positive;
			}
			
			if (level == 1){
				for (int i=start_number; i<array.Count;i++){
					output.Add(array[i].get_value
				}
			}
				     
			else {
			}
		}
		public static void Main (string[] args)
		{
			if (args.GetLength() > 0){
				using (TextReader fs = File.OpenRead(args[0])){
					int items = Parse(fs.ReadLine());
					for (int i=0;i<items;i++){
						Activity a = new Activity(fs.ReadLine());
						if (a.get_value() > 0){
							positive.Add(a);
						}
						else {
							negative.Add(a);
						}	
					}
				}
				
				int level = 0;
				if (this.negative.Count <= this.positive.Count){
					level = this.postive.Count;
				}
				else {
					level = this.negative.Count;
				}
				
				for (int i=0; i<level; i++){
					if (this.check(i)){
						break;
					}
					
				}
			}
		}
	}
}

