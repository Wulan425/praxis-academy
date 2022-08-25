# words = ["anggur", "apel", "jeruk"]
# for i in words:
#     print(i)

users = {'Rista': 'Cantik', 'Enlis': 'Ceria', 'Ria': 'Baik'}
for user, status in users.copy().items():
    if status == 'Ceria':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'Cantik':
        active_users[user] = status

print(users)
print(active_users)

a = {}
a["c"] = "d"
a["e"] = "f"
print(a)



