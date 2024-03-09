import xml.dom.minidom as md
import pyperclip

# クリップボードから文字列を取得してパース

xxx = pyperclip.paste()
print(xxx)

document = md.parseString(xxx)

# https://docs.python.org/ja/3/library/xml.dom.minidom.html
str_x = document.toprettyxml(indent='    ', newl='\r\n', encoding='utf-8')

pyperclip.copy(str_x.decode())
