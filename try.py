hs_file=open('highscore.txt','r+')
line = int(hs_file.readline())
result=int(input("enter number"))
print(line)

if result>line:
    hs_file.seek(0,0)
    hs_file.write((str(result)))
    hs_file.truncate()
