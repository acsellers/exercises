using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;

namespace csactivity
{
	class Activity {
		
		string name;
		int worth;
		
		public Activity(string def){
			name = def.Split(' ')[0];
			worth = System.Convert.ToInt32(def.Split(' ')[1]);
		}
		public int get_value(){
			return worth;
		}
		public string get_name(){
			return name;	
		}
	}
	
	class SearchSystem {
		List<Activity> positive = new List<Activity> ();
		List<Activity> negative = new List<Activity> ();
		Dictionary<int, string> solutions = new Dictionary<int, string> ();
		
		public SearchSystem(string inFile){
			using(StreamReader sr = new StreamReader(inFile)){
				for (int i = 0; i < System.Convert.ToInt32(sr.ReadLine()); i++) {
					Activity a = new Activity(sr.ReadLine());
					if (a.get_value() > 0){
						positive.Add(a);
					}
					else {
						negative.Add(a);
					}
				}
			}
		}
		
		
		public void search(){
			int level = 1;
			while ((level <= positive.Count) && (level <= negative.Count)) {
				
				if (level <= positive.Count){
					
					
					
				}
				
				if (level <= negative.Count){}
				
				
				level++;
			}
		}
		
		public List<string> get_combinations(int combo_size, List<Activity> source) {
			List<string> output = new List<string> ();
			for (int i = 0; i <= source.Count - combo_size; i++){
				
				
			}
		}
		
		public int score_combination(string combo, List<Activity> source){
			int sum = 0;
			foreach(string act_id in combo.Split(',')){
				sum += source[System.Convert.ToInt32(act_id)].get_value();	
			}
		}
	}
	class MainClass
	{
		
		public static void Main (string[] args)
		{
			if (args.Length > 0){
				var s = new SearchSystem(args[0]);
				
				s.search();
			}
		}
	}
}