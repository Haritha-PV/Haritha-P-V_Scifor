import os

os.environ['Setvar']="45ty67"

env=os.getenv('Setvar')
print(env, "\n")

env2=os.environ.get('Setvar')
print(env2)