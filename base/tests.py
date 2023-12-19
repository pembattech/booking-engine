from django.test import TestCase

# Create your tests here.

a = "kathmandu bhaktapur".split()

b = ['jhapa', 'ktm', 'kathmandu']

for i in a:
    if i in b:
        print(i)