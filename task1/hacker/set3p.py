n = int(input())

countries = set()

for i in range(n):
    country = input()
    countries.add(country)

print(len(countries))