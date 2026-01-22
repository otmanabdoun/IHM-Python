<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/TR/WD-xsl">
<xsl:template match="/">

<html>
 <head> 
  <title> facture.xml </title> 
 </head>

<body>

<center><H1><b><u> Facture  </u></b></H1></center>

<center>
<H3> Num de la facture : </H3><xsl:value-of select="Facture/@Num_fact"/>
<H3> Date de commande: </H3><xsl:value-of select="Facture/@Dat_cmd"/>
<H3> Nom du Client: </H3><xsl:value-of select="Facture/@Nom_clt"/>
<H3> Addressdu Client: </H3><xsl:value-of select="Facture/@Add_cli"/>

</center>



<center>
<table  border="3" width="700">

<tr>
<td align="center" colspan="3" bordercolor="aquamarine"  bgcolor="aliceblue">lignes de commande</td></tr>
<tr>
<td align="center"  bgcolor="lavender" bordercolor="lightslategray"> Description de Produit </td>
<td align="center"  bgcolor="lavender" bordercolor="lightslategray"> Quantite commande </td>
<td align="center"  bgcolor="lavender" bordercolor="lightslategray"> Prix-unitaire de produit </td> </tr>

<xsl:for-each select="Facture/ligne_de_cmd">
<tr>
<td> <xsl:value-of select="Descr_prd"/> </td>
<td> <xsl:value-of select="Qte_cmd"/> </td>
<td> <xsl:value-of select="Prix_unt_prod"/> </td> </tr>
</xsl:for-each>

</table>
</center>
</body>
</html>
</xsl:template>
</xsl:stylesheet>

