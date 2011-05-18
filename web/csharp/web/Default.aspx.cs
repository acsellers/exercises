
using System;
using System.Web;
using System.Web.UI;

namespace web
{


	public partial class Default : System.Web.UI.Page
	{
		public virtual void Page_Load(object sender, EventArgs args){
			header.Text = "What yo name";	
			
		}

		public virtual void button1Clicked (object sender, EventArgs args)
		{
			header.Text = "Hello "+test.Text;
		}
	}
}

