
using System;
using System.Web;
using System.Web.UI;

namespace web
{


	public partial class Login : System.Web.UI.Page
	{

		public virtual void OnAuthenticate(object sender, System.Web.UI.WebControls.AuthenticateEventArgs e){
			bool Authed = false;
			if (Login1.UserName == Login1.Password){
				e.Authenticated = true;	
			}
		}
	}
}

