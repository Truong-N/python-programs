try:
    fr = open("./eng9.txt", "r", encoding="utf-8")
    lines = fr.readlines()
    # for ind in range(len(lines)):
    #     if ind % 2 == 0:
    #         print(lines[ind])
    print(len(lines))
    i = 0
    wrd_no = 1
    while i <= 100: # len(lines): read 100 lines each days
        wrd = lines[i].strip()
        sent = lines[i+2]
        
        viets = lines[i+3].split(",")
        viet = viets[0].split(":")
        viet1 = viet[1].replace("/", "")
        wrd1 = f'<span class="english {wrd_no}">{wrd}</span><span class="viet {wrd_no} hide"> {viet1} </span>'
        sent = sent.replace( wrd, wrd1)

        wrd_no += 1
        i += 6
        print(sent)
        input("enter")
except:
    print("error open file")
