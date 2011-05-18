
using System;
using System.Web;
using System.Web.UI;
using System.Web.UI.HtmlControls;
using System.IO;
namespace web
{


	public partial class oiu : System.Web.UI.Page
	{
		public virtual void Page_Load(object sender, EventArgs args){
			
			using (StreamReader sr = new StreamReader("table.csv")){
				string all = sr.ReadToEnd();
				foreach (string tow in all.Split('\n')){
					HtmlTableRow row = new HtmlTableRow();
					
					foreach (string cell in tow.Split(',')){
						HtmlTableCell c = new HtmlTableCell();
						c.InnerText = cell;
						row.Cells.Add(c);
						
					}
					SuperTable.Rows.Add(row);
				}
			}
		}
	}
}

