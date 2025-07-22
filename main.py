from lxml import html, etree

# html dosyası okunur
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# html ağacı oluştur
tree = html.fromstring(content)

# elementtree objesi (xpath için gerekli)
element_tree = etree.ElementTree(tree)

# xpath çıkarımı yapılacak öğeleri seç
elements = {
    "Başlık": tree.xpath('//h1')[0],
    "Açıklama": tree.xpath('//p[@class="desc"]')[0],
    "İlk Link": tree.xpath('//ul/li[1]/a')[0],
    "Buton": tree.xpath('//button')[0]
}

print("=== XPath Çıkarımları ===")
for name, elem in elements.items():
    xpath = element_tree.getpath(elem)
    print(f"{name}: {xpath}")
