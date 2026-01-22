<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/">
                          
                          <html>
                              <style>
                              
                                table
                                {
                                
                                  text-align: center;
                                  border:modium solide #000000;
                                  width:50%;
                                  margin-left:290px;
                                  margin-top:40px;
                                  
                                }
                                th
                                {
                                  background-color:blue;
                                }
                                
                                table th,td
                                {
                                border : thin solid #6495ed;
                                  padding: 4px;
                                  
                                }

                              </style>
                            <body>
                              
                              <table border="1" width="30%">
                                <tr>
                                  <th>le nom du client</th>
                                  <th>l'id de son produit</th>
                                  <th>la quantité</th>
                                </tr>
                                <xsl:for-each select="Gestion_Commande/client">
                                  <tr>
                                    <td>
                                      <xsl:value-of select="@nom" />
                                    </td>
                                    <td>
                                      <xsl:value-of select="Commande/ligne_Commande/@id_prod" />
                                    </td>
                                    <td>
                                      <xsl:value-of select="Commande/ligne_Commande/@qte_cmd" />
                                    </td>
                                    
                                  </tr>
                                </xsl:for-each>
                              </table>
                            </body>

		</html>
  </xsl:template>
</xsl:stylesheet>
