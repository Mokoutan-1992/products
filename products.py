# 读取档案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品名,价格' in line：
            continue #跳过接下来的loop内容 回到forloop起点
        name, price = line.strip().split(',')
        products.append([name , price])
print(products)


#让用户输入
while True:
    name = input('请输入商品名称')
    if name == 'q':
        break
    price = input('请输入商品价格')
    price = int(price)
    products.append([name , price])
print(products)

#印出购买记录
for p in products:
    print(p[0], '的价格是', p[1])

#写入档案
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品名,价格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')