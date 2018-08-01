from lxml import etree
# 准备要转化的字符串
html = ''' <div> <ul>
        <li class="item-1"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
        </ul> </div> '''

# 将字符串转化为element对象,具有xpath方法,返回值为列表,能接受bytes类型和str类型数据(是指etree.HTML方法)
# etree.HTML() 支持字节类型和没有xml声明的文本类型
# 所以如果文档中xml声明,如:<?xml version="1.0" encoding="UTF-8"?>, 就只能传入字节数据, 而不能传入字符串
element = etree.HTML(html)

# lxml会自动修正html和xml,将element转化为字符串,返回bytes类型结果
# 对修正后的内容进行对比
html_str = etree.tostring(element)
print(html_str)
print(html_str.decode())