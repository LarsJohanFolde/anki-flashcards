import requests
import html2text
url = "https://www.worldcubeassociation.org/regulations/full/"

#clears files to reprint all regs and guidelines
open("regulations.csv", "w").close()
open("guidelines.csv", "w").close()
open("test.txt", "w").close()

content = requests.get(url).text
#updates regulations in regs.txt
print(html2text.content)

with open("test.txt", "a", encoding="utf-8") as f:
    for line in nightmarelistwithalltheregs.split("\n"):
        if ") " in line and  not line.startswith(" "):
            if line.split("\"")[1].endswith("+"):
                f.write(line.split("\"")[1] + ") " + line.split(">")[5].split("<")[0] + " " + line.split(">")[7] + "\n")
            else:
                f.write((line.split("\"")[1] + line.split(">")[3]).split("<")[0]  + "\n")
                #f.write(line + "\n")
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