<?xml version="1.0"?>
<xsl:stylesheet version="1.0" sxmlns:xsl = "http://www.w3.org/TR/WD-xsl">
<xsl:template match="/Gcommande">
<html>
<body>
<P>
	<xsl:for-each select="client">
	<xsl:value-of select="ligne_commande"/> <br>
</P>
<P>
	<xsl:for-each select="produit">
	<xsl:value-of select="produit"/> 
</P>
</body>
</html>
</xsl:template>
</xsl:stylesheet>