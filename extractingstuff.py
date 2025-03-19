currentarticle = ""

with open("regs.txt", "r") as f:
    with open("guidelines.csv", "r+") as g:
        all = f.readlines()
        storedguidelines = g.readlines()
        for reg in all:
            if reg.startswith("Article"):
                currentarticle = reg.split(":")[0]
            if (reg.split(")")[0]).endswith("+") and reg not in storedguidelines:
                justreg = reg.split(")")
                regnum = justreg.pop(0).rstrip()
                g.write(regnum+ "\t"+ "".join(justreg).rstrip() + "\t " + currentarticle + "\n")


print("completed")