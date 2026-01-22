<?xml version="1.0" encoding="ISO-8859-1" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/GestionCommande">
        
        <html>
            <head>
                <title></title>
                <style type="text/css">
                    #tb1{
                    width: 270px;
                    float: right;
                    background-color: #F2F2F2;
                    margin-right:320px;
                    }
                    #tb2{
                    width: 200px;
                    float: left;
                    margin-left: 320px;
                    background-color: #F2F2F2;
                    
                    }
                    
                    #tb3{
                    width: 200px;
                    margin-left:0px;
                    
                    background-color: #F2F2F2;
                    }
                    table ,tr,th,td
                    { border: 2px solid black;}
                    
                </style>
            </head>
            <body> 
                <center>
                    <h1 style="background-color:red;  border: 2px solid black;  background-color: #F2F2F2; width: 700px; margin-bottom:0px;"> Gestion commande</h1>
                    <table  id="tb1">
                        <tr>
                            <th colspan="3">Ligne Commande</th>
                        </tr>
                        <tr>
                            <td>Libelle</td>
                            <td>Qte</td>
                            <td>Id Prod</td>
                        </tr>
                        <xsl:for-each select="LigneCommande">
                        <tr>
                            <td><xsl:value-of select="Commande"/></td>
                            <td><xsl:value-of select="@Qte"/></td>
                            <td><xsl:value-of select="@Id_prod"/></td>
                        </tr>
                        </xsl:for-each>
                    </table>
                    
                    <table id="tb2">
                        <tr>
                            <th>Client</th>
                        </tr>
                        
                        <tr>
                            <td style="text-align: center;">Nom complet</td>
                        </tr>
                        <xsl:for-each select="Client">
                            <tr>
                                <td style="text-align: center;"><xsl:value-of select="nom"></xsl:value-of> <xsl:value-of select="prenom"></xsl:value-of> </td>
                            </tr>
                        </xsl:for-each>
                    </table> 
                    <table id="tb3">
                        
                        <tr>
                            <th colspan="2">Produit</th>
                        </tr>
                        <tr>
                            <td  >Libelle</td>
                            <td>Id Prod</td>
                        </tr>
                        <xsl:for-each select="Produit">
                            <tr>
                                <td><xsl:value-of select="libelle"></xsl:value-of></td>
                                <td><xsl:value-of select="@Id_prod"></xsl:value-of></td>
                            </tr>
                        </xsl:for-each>
                    </table>
                    
                </center>
            </body>
        </html> 
    </xsl:template>
</xsl:stylesheet>