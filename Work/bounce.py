# bounce.py
#
# Exercise 1.5

height = 100
bounce_back = 3/5
bounces = 10

for bounce in range(bounces):
    height = round(height * bounce_back, 4)
    print(height)
