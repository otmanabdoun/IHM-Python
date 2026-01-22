<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	
	<xsl:template match="/">
	<html>
		<head>
				<link rel="stylesheet" href="style.css"/>
		</head>
		<body>
			<h1>La gestion des commandes</h1>
			<!--L'affichage des PRODUITS-->
			<div class="produits">
				<h2>Les Produits:</h2>
				<table>
						<tr>
							<th>Designation</th>
							<th>Prix</th>
						</tr>
						<xsl:for-each select="//produit"> 
							<tr>
								<td><xsl:value-of select="@designation"/></td>
								<td><xsl:value-of select="@prix"/> DH</td>
							</tr>
						</xsl:for-each>
				</table>
			</div>
			<!--L'affichage des CLIENTS-->
			<div class="clients">
				<h2>Les clients:</h2>
				<table>
						<tr>
								<th>Nom</th>
								<th>Prenom</th>
						</tr>
						<xsl:for-each select="//client"> 
							<tr>
								<td><xsl:value-of select="@nom"/></td>
								<td><xsl:value-of select="@prenom"/></td>
							</tr>
						</xsl:for-each>
				</table>
			</div>
			<!--L'affichage des produits commandes par un clients-->
			<div class="produits_commandes">
				<h2>Les produits commandés par le client "AFKIR Marouan" séparés en fonction de commande:</h2>
				<table id="tb_Pro_cmd">
						<tr>
								<th>Designation</th>
								<th>Prix unitaire</th>
								<th>Quantité commandée</th>
						</tr>
						<xsl:for-each select="//client[@id_client='cl1']/commande">

							<tr>
								<td id="NbCmd">Commande <xsl:value-of select="position()"/>:</td>
							</tr>
							<xsl:for-each select="ligne_cmd">
								<tr>
									<td><xsl:value-of select="//produit[@id_prod = current()/@ref_pro]/@designation"/></td>
									<td><xsl:value-of select="//produit[@id_prod = current()/@ref_pro]/@prix"/> Dh</td>
									<td><xsl:value-of select="@qte_cmd"/> unité(s)</td>
								</tr>
							</xsl:for-each>
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


