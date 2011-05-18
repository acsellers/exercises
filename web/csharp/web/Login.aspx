<%@ Page Language="C#" Inherits="web.Login" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head runat="server">
	<title>Login</title>
</head>
<body>
	<form id="form1" runat="server">
		<asp:Login id="Login1" runat="server" OnAuthenticate="OnAuthenticate" />
	</form>
</body>
</html>
