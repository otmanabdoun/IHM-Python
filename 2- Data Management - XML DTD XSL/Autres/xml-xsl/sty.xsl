<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="1.0">
    <xsl:template match="/">
        <html>
            <head>
                <title>gestion des commandes</title>
                <style type="text/css">
                    tr.ctr td{
                    border-left:1px solid;
                    border-bottom:1px solid;
                    text-align:center
                    
                    }
                    .tb{
                    margin:auto;
                    text-align:center;
                    margin-top:200px;
                    margin-top:30px;
                    }
                  .di{
                  margin:auto;
                  position:absolue;
                  left:100;
                  background:red;
                  text-align:center;
                  }
                  .b{
                  color:#D6710B;
                  }
                </style>
            </head>
            <body style="background-color:#DBFCF8;">
            
                <table border="1px" width="80%" cellspacing="0" cellpadding="0" class="tb">
                    <tr>                        <td height="10%" style="background-color:yellow">
                        <h1>Gestion des commandes</h1>
                    </td></tr>
                    <tr class="ctr">

                        <td >
                            <table   width="100%" cellspacing="0" cellpadding="0">
                <xsl:for-each select="Gestion_Commande/Client">
                    
                    <tr  class="clt">
                        <td style="color:green; background-color:aqua">client : <xsl:value-of select="@nom_clt" ></xsl:value-of> </td>
                       
                        <td>
                            <table width="100%"  cellspacing="0" cellpadding="0">
                    <xsl:for-each select="Commande">
                        <tr>
                            <td style="color:#950000;"> <xsl:value-of select="@id_cmd" ></xsl:value-of></td>
                    <td>
                        <table width="100%"  cellspacing="0" cellpadding="0">
                            <xsl:for-each select="Ligne_com">
                            <tr>
                                
                                <td><div class="b">produit </div> <xsl:value-of select="@id_prod" ></xsl:value-of></td>
                                <td><div class="b">qte </div> <xsl:value-of select="@Qte_com" ></xsl:value-of></td>
                                
                            </tr>
                              </xsl:for-each>
                        </table>
                        
                    </td>
                            
                        </tr >
                    
                </xsl:for-each>
                            </table>
                        </td>
                            
                    </tr>
                    
                </xsl:for-each> </table>
                        </td>
                    </tr>
                </table>
            </body>
        </html>			
    </xsl:template>
</xsl:stylesheet>