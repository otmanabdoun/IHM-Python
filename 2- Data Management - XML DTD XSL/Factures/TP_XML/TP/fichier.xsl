<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/gestiondecmd">
<html>
<head>
<title>Mise en forme avec XSLT</title>
</head>

<body>

<table width="1000" border="7" cellspacing="5" cellpadding="3">
  <tr>
    <th >ID</th>
	<th>Nom_pro</th>
	<th>prix</th>
  </tr>
  <xsl:for-each select="produit" >
  <tr>
     <td><xsl:value-of select="@id"/> </td>
	 <td><xsl:value-of select="nom"/> </td>
	 <td><xsl:value-of select="prix"/> </td>
  </tr>
  </xsl:for-each>
</table>


<table width="1000" border="7" cellspacing="5" cellpadding="3" >
  <tr>
    <th>ID</th>
	<th >TYPE</th>
    <th >ligne</th>
  </tr>
  <xsl:for-each select="client/cmd">
  <tr>
	 <td><xsl:value-of select="ligne-cmd/@id"/> </td>
	 <td><xsl:value-of select="type"/> </td>
	 <td><xsl:value-of select="ligne-cmd/@qte"/> </td>
  </tr>
  </xsl:for-each>
</table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>