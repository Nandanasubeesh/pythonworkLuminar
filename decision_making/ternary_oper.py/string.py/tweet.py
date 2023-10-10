text="what a game, hats off to both teams well done @benstroke @patcummins30 you have bought test cricket back to life back to life love test cricket @TheBarmyarmy @cricketaus @ECB_cricket"
words=text.split(" ")

for w in words:
    if w.startswith("@"):
       
        print(w)