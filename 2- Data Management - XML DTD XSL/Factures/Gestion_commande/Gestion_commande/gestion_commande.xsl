<?xml version = "1.0" encoding = "UTF-8"?> 
 <xsl:stylesheet version = "1.0" 
      xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">
   <xsl:template match = "/"> 
      <html> 
         <body> 
            <h2>Gestion des commandes</h2> 
			<h3>Table Client</h3>
            <table border = "1"> 
               <tr bgcolor = "#9acd32"> 
			    <th>id_client</th> 
                  <th>nom</th> 
                  <th>Prenom</th> 
                 <th>Email</th> 
                  <th>Quantité</th> 
				   <th>id_prod</th> 
               </tr> 
			   	
					
               <xsl:for-each select = "Gestion_commande/client"> 
					
                  <tr> 
				  <td><xsl:value-of select = "id_client"/></td> 
                     <td><xsl:value-of select = "nom"/></td> 
                     <td><xsl:value-of select = "Prenom"/></td> 
                    <td><xsl:value-of select = "Email"/></td> 
                     <td><xsl:value-of select = "commande/ligne_commande/qte_cmd"/></td> 
                     <td><xsl:value-of select = "commande/ligne_commande/id_prod"/></td> 
                  </tr> 
               </xsl:for-each>
			   
					
                </table>
	             <h3>Table Produit</h3>
						 <table border = "1"> 
               <tr bgcolor = "orange"> 
			    <th>id_prod</th> 
                  <th>Nom_Produit</th>  </tr> 	

        <xsl:for-each select = "Gestion_commande/Produit"> 
					
                  <tr> 
				  <td><xsl:value-of select = "id_prod"/></td> 
                     <td><xsl:value-of select = "Nom_Produit"/></td> 
                    
                  </tr> 
               </xsl:for-each>	
 </table>			   
         </body> 
      </html> 
   </xsl:template>  
</xsl:stylesheet>