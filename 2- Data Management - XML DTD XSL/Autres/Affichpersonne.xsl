<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet
    xmlns:xsl="http://www.w3.org/TR/WD-xsl"
    xmlns="http://www.w3.org/TR/REC-html40"
    result-ns="">
    
    <xsl:template match="/">
        
        <HTML>
            
            <HEAD>
                
                <TITLE>Liste des professeurs</TITLE>
                
            </HEAD>
            
            <BODY BGCOLOR="#FFFFFF">
                
                <xsl:apply-templates/>
                
            </BODY>
            
        </HTML>
        
    </xsl:template >
    
    <xsl:template match="personne" >
        
        <ul>
            
            <li>
                
                <xsl:value-of select="nom"/>
                
                -
                <xsl:value-of select="prenom"/>
                
            </li>
            
        </ul>
        
    </xsl:template >
    
</xsl:stylesheet>