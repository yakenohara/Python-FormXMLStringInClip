import xml.dom.minidom as md
import pyperclip

# クリップボードから文字列を取得してパース
document = md.parseString(pyperclip.paste())

# https://docs.python.org/ja/3/library/xml.dom.minidom.html
str_x = document.toprettyxml(indent='    ', newl='\r\n', encoding='utf-8')

print(str_x)

pyperclip.copy(str_x)
