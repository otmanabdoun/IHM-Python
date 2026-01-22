<?xml version='1.0'?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/TR/WD-xsl">
<xsl:template match="/">
<html>
<body>
<p>
<h1 align="center"><U>Cahier de texte</U></h1>
<h2>Id_Professeur : <xsl:value-of select="Gestion_cahier_txt/Prof/@id_prof"/>.</h2>
<h2>Id_Module : <xsl:value-of select="Gestion_cahier_txt/Prof/Cahier_txt/@id_mod"/>.</h2>
<h2>Id_Groupe : <xsl:value-of select="Gestion_cahier_txt/Prof/Cahier_txt/Seance/@id_grp"/>.</h2>
<h2>Seances : </h2>

</p>
<table border="3" cellspacing="0" cellpadding="3" align="center">
<tr bgcolor="bleu">
<td align="center"><h3>Date</h3></td>
<td align="center"><h3>Salle</h3></td>
<td align="center"><h3>Objectifs</h3></td>
<td align="center"><h3>Synthese</h3></td>
<td align="center"><h3>Objectif de la seance suivante</h3></td>
</tr>
<xsl:for-each select="Gestion_cahier_txt/Prof/Cahier_txt/Seance">
<tr>
<td align="center"><h3><xsl:value-of select="@date_seance"/></h3></td>
<td align="center"><h3><xsl:value-of select="@num_salle"/></h3></td>
<td align="center"><h3><xsl:value-of select="@objectifs"/></h3></td>
<td align="center"><h3><xsl:value-of select="@synthese"/></h3></td>
<td align="center"><h3><xsl:value-of select="@objectifs_de_la_seance_prochaine"/></h3></td>
</tr>
</xsl:for-each>
</table>


</body>
</html>
</xsl:template>
</xsl:stylesheet>