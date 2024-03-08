import xml.etree.ElementTree as ET
import xml.dom.minidom as md

xmlRoot = ET.Element('root')
# ElementTreeでXMLを作成



# 文字列パースを介してminidomへ移す
document = md.parseString('<user><name>hironemu</name><addresses><address><zip>xxx-xxxx</zip><city>Chofu</city></address><address><zip>yyy-xxxx</zip><city>Shinjuku</city></address></addresses></user>')

file = open('test.xml', 'w')
# エンコーディング、改行、全体のインデント、子要素の追加インデントを設定しつつファイルへ書き出し
document.writexml(file, encoding='utf-8', newl='\n', indent='', addindent='  ')
file.close()
