import xml.etree.cElementTree as et

root = et.Element("Registro")

se = et.SubElement(root,"edificio2")
et.SubElement(se, "Matricula").text = "18050023"
et.SubElement(se, "Carrera").text = "Redes"
et.SubElement(se, "Nombre").text = "Dulce Alondra Lopez Rdz"


se = et.SubElement(root,"edificio2.1")
et.SubElement(se, "Matricula").text = "18040161"
et.SubElement(se, "Carrera").text = "Redes"
et.SubElement(se, "Nombre").text = "Luis Gerardo Nuncio Rdz "


se = et.SubElement(root,"edificio2.2")
et.SubElement(se, "Matricula").text = "18012121"
et.SubElement(se, "Carrera").text = "Redes"
et.SubElement(se, "Nombre").text = "Jonathan Rdz"



se = et.SubElement(root,"edificio2.3")
et.SubElement(se, "Matricula").text = "181812828"
et.SubElement(se, "Carrera").text = "Redes"
et.SubElement(se, "Nombre").text = "Alonso Reyes Segura"


se = et.SubElement(root,"edificio2.4")
et.SubElement(se, "Matricula").text = "180939382"
et.SubElement(se, "Carrera").text = "Redes"
et.SubElement(se, "Nombre").text = "Emmanuel Tovar Castañon"



tree= et.ElementTree(root)
tree.write("Registro.xml", xml_declaration=True)
