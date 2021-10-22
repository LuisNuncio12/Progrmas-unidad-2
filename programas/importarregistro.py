import xml.etree.cElementTree as et
from xml.etree.ElementTree import SubElement, parse

xml_file = parse('Registro.xml')

root = et.Element("registroo")

xmlRoot = xml_file.getroot()
 
se = et.SubElement(root,"edificio2.5")
et.SubElement(se, "Matricula").text = "1891882"
et.SubElement(se, "Carrera").text = "Redes"
et.SubElement(se, "Nombre").text = "Laura Herandez Torres "

xmlRoot.append(se)

xml_file.write("Registro2.xml",xml_declaration=True)


