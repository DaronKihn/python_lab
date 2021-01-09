print("Введите число продуктов в холодильнике:")
count_products = int(input())
products = set()
prod_in_rec = set()
print("Введите названия продуктов в холодильнике:")
for i in range(count_products):
    products.add(input())
print("Введите количество рецептов:")
count_rec = int(input())
for i in range(count_rec):
    print("Название рецепта:")
    name_rec = input()
    print("Количество необходимых продуктов:")
    count_prod_in_rec = int(input())
    print("Введите названия необходимых продуктов:")
    for j in range(count_prod_in_rec):
        prod_in_rec.add(input())
    if prod_in_rec <= products:
        print(name_rec, "- можно приготовить")
    prod_in_rec.clear()