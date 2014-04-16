#!/usr/local/bin/python
# -*- encoding: utf-8 -*-

import sys
import urllib
import urllib2
import json
import io


def sparqlQuery(query, baseURL, graph="", format="application/json"):
	params={
		"default-graph": graph,
		"query": query,
		"format": format,
	}
	querypart=urllib.urlencode(params)
	response = urllib.urlopen(baseURL,querypart).read()
	return json.loads(response)


def main():

	#Variables
	dataSourceName="http://opendata.caceres.es/sparql/"
	nombreSalida="Salida"
	if len(sys.argv)>=3: nombreSalida=sys.argv[2]


	#Abrimos el fichero de la consulta.
	print "Procesando la consulta a partir del fichero: ", sys.argv[1]
	fConsulta=open(sys.argv[1],'r')
	auxConsulta=fConsulta.read()
	print "\nLa consulta que estamos tratando es:\n", auxConsulta


	#Obtenemos el csv y lo guardamos


	#Obtenemos el json y lo guardamos
	datosjson=sparqlQuery(auxConsulta,dataSourceName)

	with io.open('/Users/jesusredondogarcia/Desktop/Scripts/Descargas/'+nombreSalida+'_Cáceres_JSON.json', 'w', encoding='utf-8') as f:
		f.write(unicode(json.dumps(datosjson, ensure_ascii=False, indent=2)))
	


if len(sys.argv)<=1:
	print "Error, se necesita un fichero de entrada que contenga la consulta a procesar." 
	print "El modo de empleo de este scritp es: $python ", sys.argv[0]," Fichero_Consulta"
	print "Ejemplo: $python", sys.argv[0],"/Users/jesusredondogarcia/Desktop/Abril/subidos\ a\ opendata/Museos/consulta_Museos"
	print "\nPuede añadir un segundo parámetro de entrada para que los ficheros de salida se almacenen con el nombre correcto."
	print "Ejemplo: $python", sys.argv[0],"/Users/jesusredondogarcia/Desktop/Abril/subidos\ a\ opendata/Museos/consulta_Museos Museos"
	print "Produciría los ficheros de salida: \"Museos_Cáceres_csv.csv\" y \"Museos_Cáceres_JSON.json\""
else:
	main()

