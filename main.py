from lxml import html

html_code = """
<html>
  <body>
    <div class="product">
      <span class="price">$19.99</span>
    </div>
  </body>
</html>
"""

tree = html.fromstring(html_code)
price = tree.xpath("//span[@class='price']/text()")[0]
print(price)