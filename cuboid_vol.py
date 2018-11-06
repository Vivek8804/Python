print("Enter the length, breadth and height of the cuboid ")
l,b,h = float(input()), float(input()), float(input())
def volume_cuboid(a,b,c):
    volume = a*b*c
    print("The volume of cuboid is {}".format(volume))

volume_cuboid(l,b,h)