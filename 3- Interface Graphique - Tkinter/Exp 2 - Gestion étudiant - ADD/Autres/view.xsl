<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	
	<xsl:template match="/">
	<html>
		<head>
				<link rel="stylesheet" href="style.css"/>
		</head>
		<body>
			<h1>La liste des étudiants Masters M2I & MQL</h1>
			<!--L'affichage des étudinats-->
			<div class="etudiants">
				<h2>Les étudiants:</h2>
				<table>
						<tr>
							<th>Numéro</th>
							<th>Nom</th>
							<th>Prénom</th>
							<th>Master</th>
						</tr>
						<xsl:for-each select="//etudiant"> 
							<tr>
								<td><xsl:value-of select="@nom"/></td>
								<td><xsl:value-of select="@nom"/></td>
								<td><xsl:value-of select="@prenom"/></td>
								<td><xsl:value-of select="@master"/></td>
							</tr>
						</xsl:for-each>
				</table>
			</div>
			<script src="jquery.js"></script>
			<script>
				$(function(){

				});
			</script>
		</body>
	</html>
	</xsl:template>

</xsl:stylesheet>


