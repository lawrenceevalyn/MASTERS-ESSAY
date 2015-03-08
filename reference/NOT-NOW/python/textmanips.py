outfile = open("loy.txt", mode="w")
outfile.write("Mina Loy wrote: Pocked with personification, the fossil virgin of the skies waxes and wanes.")
outfile.close()

infile = open("loy.txt")
text = infile.read()

def processed(text):
    lowerReplace = text.lower() .replace("p","b")
    return lowerReplace
processed(text)
