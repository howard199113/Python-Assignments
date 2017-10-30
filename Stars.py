def draw_stars(stars):
    for x in stars:
        output = ""
        if isinstance(x,str) == True:
            times = len(x)
            while times > 0:
                output += x[:1]
                times -= 1
            print output
        else:
            for i in range(0,x):
                output += "*"
            print output
    return "Awesome!"
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
print draw_stars(x)