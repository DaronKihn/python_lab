print("Введите количество книг в библиотеке:")
count_books_in_library = int(input())
print("Введите количество книг в списке:")
count_books_in_list = int(input())
books_in_library = set()
print("Введите названия книг из библиотеки:")
for i in range(count_books_in_library):
    books_in_library.add(input())
print("Введите названия книг из списка:")
for i in range(count_books_in_list):
    if input() in books_in_library:
        print("YES")
    else:
        print("NO")
