import environ

env = environ.Env()
SECRET_KEY = env('SECRET_KEY')

print(SECRET_KEY)