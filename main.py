import config
try:
    import api
except ModuleNotFoundError:
    print('api.py not found. Create this file as described in the readme.')
    exit(0)


print(config.version)
print(api.API_TOKEN)
