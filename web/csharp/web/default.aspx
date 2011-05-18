<%@ Page Language="C#" Inherits="web.Default" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head runat="server">
	<title>Default</title>
</head>
<body>
	<form id="form1" runat="server">
		<h1 id="headers"><asp:Label Text="Please enter your name" runat="server" id='header' /></h1>
		<asp:TextBox id="test" runat="server"/>
		<asp:Button id="button1" runat="server" Text="Yah dat's me" OnClick="button1Clicked" />
	</form>
</body>
</html> 
