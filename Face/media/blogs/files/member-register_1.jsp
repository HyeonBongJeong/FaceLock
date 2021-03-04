<%@page import="kh.test.model.MemberDAO"%>
<%@page import="kh.test.model.MemberVO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	String ctxPath1 = request.getContextPath();
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>aaaa</title>
<style>
</style>

<script type="text/javascript">
	function goRegister(){
		var frm = document.registerFrm;
		frm.action = "<%=ctxPath1%>/test/memberRegister.do";
		frm.method = "post";
		frm.submit();
	}
</script>

</head>
<body>
	<div class="layer">
		<h2>회원가입</h2>
		<form name="registerFrm">
			<ul>
				<li>아이디<br /> <input type="text" name="id" value=""
					required="required" />
				</li>
				<li>아이디<br /> <input type="text" name="pwd" value=""
					required="required" />
				</li>
				<li>성명<br /> <input type="text" name="name" value=""
					required="required" />
				</li>
				<li>생년월일 (예: 19950402)<br /> <input type="text" name="birthday"
					value="" required="required" placeholder="19950402" />
				</li>
				<li><label for="man">남</label> <input type="radio"
					name="gender" id="man" value="1" checked="checked" /></li>
				<li><label for="woman">여</label> <input type="radio"
					name="gender" id="woman" value="2" /></li>
				<li>
					<button type="button" id="btnOK" onclick="goRegister()">확인</button>
				</li>
			</ul>
		</form>
	</div>
</body>
</html>