<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
 <xsl:template match="/">
        <html>
	    <head>
	        <title>Mon premier document XSL</title>
	    </head>
	    <body>
	    	<table border="1" align="left" callpadding="10" cellspacing="2" width="70%">
	        	<tr bgcolor="pink">
	        		<th>id_client</th>
	        		<th>nom_client</th>
	        		<th>prenom_client</th>
	        		<th>cin_client</th>
	        		<th>num_commande</th>
	        		<th>Qte_cmd</th>
	        		<th>Id_prod</th>

	        	</tr>
	        <xsl:for-each select="gestion_commande/client">
	        <tr>
	        		<td><xsl:value-of select="idC"/></td>
	        		<td><xsl:value-of select="nomC"/></td>	
	        		<td><xsl:value-of select="prenomC"/></td>	
	        		<td><xsl:value-of select="cin"/></td>
	        		<td><xsl:value-of select="commande/num"/></td>	
	        		<td><xsl:value-of select="commande/ligne_commande/@Qte_cmd"/></td>
	        		<td><xsl:value-of select="commande/ligne_commande/@Id_prod"/></td>					
	        </tr>		
            </xsl:for-each>
            </table>
            <table  border="1" align="right" callpadding="10" cellspacing="2" width="20%">
	        	<tr bgcolor="gray">
	        		<th>id_produit</th>
	        		<th>nom_produit</th>
	        	</tr>
	        	<xsl:for-each select="gestion_commande/produit">
	        	<tr>
	        		<td><xsl:value-of select="@id"/></td>
	        		<td><xsl:value-of select="nomP"/></td>
	        	</tr>	
	        	</xsl:for-each>	
	        </table>			
	    </body>
	</html>			
  </xsl:template>
</xsl:stylesheet>

