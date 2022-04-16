from decouple import config


print(config("HOST"))
print(config("USER"))
print(config("PASSWORD"))
print(config("DB"))
