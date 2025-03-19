currentarticle = ""

open("regulations.csv", "w").close()
open("guidelines.csv", "w").close()

#Guidelines
with open("regs.txt", "r") as f:
    with open("guidelines.csv", "a") as g:
        all = f.readlines()
        for reg in all:
            if reg.startswith("Article"):
                currentarticle = reg.split(":")[0].replace(" ", "_")
            if (reg.split(")")[0]).endswith("+"):
                justreg = reg.split(")")
                regnum = justreg.pop(0).rstrip()
                g.write(regnum+ "\t"+ "".join(justreg).rstrip() + "\t " + currentarticle + "\n")

#Regs
with open("regs.txt", "r") as f:
    with open("regulations.csv", "a") as g:
        all = f.readlines()
        for reg in all:
            if reg.startswith("Article"):
                currentarticle = reg.split(":")[0].replace(" ", "_")
                continue
            if not (reg.split(")")[0]).endswith("+"):
                justreg = reg.split(")")
                regnum = justreg.pop(0).rstrip()
                g.write(regnum+ "\t"+ "".join(justreg).rstrip() + "\t " + currentarticle + "\n")

print("completed")