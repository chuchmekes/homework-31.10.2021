names = []
num = 0
while not num==3:
    num+=1
    names.append(input("Введите имя:").capitalize())
print(names)
answer=str(input("Вы хотите продолжить ввод имен? ")).capitalize()
if answer=="Yes":
    while not names[-1]=="No":
        names.append(input("Введите имя:").capitalize());

print(names)
name=input("Введите имя одного из гостей: ").capitalize()
print(names.index(name))
ask=str(input("Вы правда хотите, чтобы этот человек присутствовал на вечеринке? "))
if ask=="no":
    names.remove(name)
    print(names)

