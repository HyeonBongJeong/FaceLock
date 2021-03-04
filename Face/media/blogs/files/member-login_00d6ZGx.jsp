<%@page import="java.text.DecimalFormat"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%
	String ctxPath=request.getContextPath();
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript">
function goLogin() {
	var frm = document.loginFrm;
	frm.action = "<%=ctxPath%>/test/login.do"
	frm.method="post";
	frm.submit();
}
</script>
</head>
<body>
<form name="loginFrm">
id:<input type="text" name="id"><br>
pwd:<input type="text" name="pwd"><br>

<input type="checkbox" name="chk1" value="c1">c1
<input type="checkbox" name="chk1" value="c2">c2
<input type="checkbox" name="chk1" value="c3">c3
<input type="checkbox" name="chk1" value="c4">c4

<button type="button" onclick="goLogin();">로그인</button>
</form>

<hr>
<c:if test="${not empty chkedName}">
	<h2>선택한 것들은~</h2>
	<c:forEach items="${chkedName }" var="e" varStatus="s">
		${s.count } :  ${e } <br>
	</c:forEach>
</c:if>
<c:if test="${empty chkedName }">
	선택하지 않았습니다.
</c:if>
</body>
</html>











