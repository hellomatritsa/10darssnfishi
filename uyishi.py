
####1-masala

# def majority_element(nums: list) -> int:
#     if not nums:
#         return -1
#     return max(nums, key=nums.count)

# nums=list(map(int, input("Sonlarni kiriting: ").split()))

# print(majority_element(nums))

##2-masala

# def search_by_genre(cinema: list, genre: str) -> list:
#     return list(filter(lambda x: x['genre']==genre, cinema))

# cinema = [
#     {"title": "Avatar", "genre": "Fantastika", "price": 40000},
#     {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
#     {"title": "Oq yo'l", "genre": "Drama", "price": 25000},
#     {"title": "Dune", "genre": "Fantastika", "price": 35000}
# ]

# print(search_by_genre(cinema, input("Janr kiriting: ")))

##3-masala
# def merge_unique_ids(active_users: list, new_users: list) -> list:
#     return list(set(active_users + new_users))

# active_users = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001']
# new_users = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']

# print(merge_unique_ids(active_users, new_users))

##4-masal

# def sorted_by_price(products: list) -> list:
#     return sorted(products, key=lambda x: int(x[1]), reverse=True)

# products = [
#     ('Olma', '12000', '50'),
#     ('Banan', '8000', '100'),
#     ('Gilos', '15000', '70'),
#     ('Apelsin', '9000', '80'),
#     ('Anor', '30000', '20'),
#     ('Uzum', '20000', '40'),
#     ('Tarvuz', '25000', '15'),
#     ('Shaftoli', '18000', '60'),
#     ('Qovun', '40000', '25'),
#     ('Qulupnay', '35000', '10')
# ]

# print(sorted_by_price(products))

##5-masala

# def are_numbers_ascending(text: str) -> bool:
#   new = [int(soz) for soz in text.split() if soz.isdigit()]
#   if new:
#     son = new[0]
#     for num in new[1:]:
#       if son>=num:
#         return False
#       son = num
#     return True
#   else:
#     return False

# matn = input("Matn kiriting: ")
# print(are_numbers_ascending(matn))



