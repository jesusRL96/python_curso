import xml.dom.minidom

domtree = xml.dom.minidom.parse('cd_catalog.xml')
catalog = domtree.documentElement
cds = catalog.getElementsByTagName('CD')

for cd in cds:
    print("--- CD ---")
    if cd.hasAttribute('id'):
        print(f"ID: {cd.getAttribute('id')}")
    print(f"Title: {cd.getElementsByTagName('TITLE')[0].childNodes[0].data}")
    print(f"Artist: {cd.getElementsByTagName('ARTIST')[0].childNodes[0].data}")
    print(f"Country: {cd.getElementsByTagName('COUNTRY')[0].childNodes[0].data}")

cds[2].getElementsByTagName('TITLE')[0].childNodes[0].nodeValue = "New Title"
cds[0].setAttribute('id', '99999')

# domtree.writexml(open('cd_catalog_new.xml', 'w'))

newCD = domtree.createElement('CD')
newCD.setAttribute('id', '8484')
title = domtree.createElement('TITLE')
title.appendChild(domtree.createTextNode('new element'))
artist = domtree.createElement('ARTIST')
artist.appendChild(domtree.createTextNode('new artist'))
country = domtree.createElement('COUNTRY')
country.appendChild(domtree.createTextNode('MEX'))

newCD.appendChild(title)
newCD.appendChild(artist)
newCD.appendChild(country)

catalog.appendChild(newCD)
domtree.writexml(open('cd_catalog_new.xml', 'w'))