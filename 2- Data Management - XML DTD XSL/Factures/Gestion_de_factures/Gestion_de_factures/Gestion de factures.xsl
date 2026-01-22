<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
 <xsl:template match="/">
 <html>
 <head></head>
 <body>
 <table border="1" width="75%" align="left">
  <tr bgcolor="purple">
  <th>Id-Client</th>
  <th>Nom</th>
  <th>Prénom</th>
  <th>Num_cmd</th>
  <th>Qte_cmd</th>
  <th>Id_prod</th>
  </tr>
  <xsl:for-each select="Gestion_Commande/Client">
  <tr bgcolor="pink">
  <td><xsl:value-of select="@id"/></td>
  <td><xsl:value-of select="@nom" /></td>
  <td><xsl:value-of select="@prenom" /></td>
   <td><xsl:value-of select="Commande/@Num"/></td>
   <td><xsl:value-of select="Commande/Ligne_de_commande/@Qte_cmd" /></td>
   <td><xsl:value-of select="Commande/Ligne_de_commande/@Id_prod" /></td>
  </tr>
  </xsl:for-each>
  </table>
  <table border="1" width="20%" align="right">
  <tr bgcolor="gray">
  <th>id_Produit</th>
  <th>Nom_Produit</th>
  </tr>
  <xsl:for-each select="Gestion_Commande/Produit">
  <tr bgcolor="pink">
  <td><xsl:value-of select="@idP" /></td>
  <td><xsl:value-of select="@nomP" /></td>
  </tr>
 </xsl:for-each>
 </table>
 </body>
 </html>
 </xsl:template>
 </xsl:stylesheet>
