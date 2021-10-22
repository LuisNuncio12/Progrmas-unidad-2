from xml.etree.ElementTree import parse, Element

file_name='Registro2.xml'
doc_xml = parse(file_name)
root = doc_xml.getroot()

root.remove(root.find ('edificio2.5'))

new_file = 'Registro3.xml'
doc_xml.write(new_file, xml_declaration=True)

