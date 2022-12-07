print('''

         .                      .
         .                      ;
         :                  - --+- -
         !           .          !
         |        .             .
         |_         +
      ,  | `.
--- --+-<#>-+- ---  --  -
      `._|_,'
         T
         |
         !
         :         . : 
         .       *
''')

print("Tervetuloa aurinkokunnan tutkimisen pariin!")
print("Kuinka pitkälle olet valmis menemään tullaksesi juhlituksi sankariksi?")

choiceya = input("Lähdet Tellukselta. Kierrätkö Telluksen yli vai ali? ").lower()
if choiceya == "ali":
    choiceavo = input("Zwoaam! Alaspäin! Vasen vai oikea? ").lower()
    if choiceavo == "vasen":
        choicevkj = input("Ja tiukka vasen! Kaasua vai jarrua? ").lower()
        if choicevkj == "jarrua":
            choicejmm = input("Skriiks, kuuluu jarruista. Seuraava suunta: Mars. Vai Merkurius sittenkin? ").lower()
            if choicejmm == "mars":
                choicemlv = input("Marsia kohti siis! Ohoh, asteroidivyöhyke. Läpi vai väistö? ").lower()
                if choicemlv == "väistö":
                    choiceauk = input("Kuinka rohkeaa! Jatkatko aurinkokunnasta ulos (u) vai palaatko kotiin (k)? ").lower()
                    if choiceauk == "k":
                        print("Selvisit kotiin! Voitto se on tämäkin. Nyt olet sentään käynyt avaruudessa.")
                    elif choiceauk == "u":
                        choicekl = input("Ulos aurinkokunnasta siis! Kauas vai lähelle? ").lower()
                        if choicekl == "kauas":
                            choicehk = input("No niin, rohkea tyyppi! Mennäänkös hitaasti vai kovaa? ").lower()
                            if choicehk == "kovaa":
                                print("Tutkit koko aurinkokunnan ja aika pitkälle uloskinpäin. Sankari!")
                            else:
                                print("Joskus kannattaisi painaa kaasua. Avaruusoliot nappasivat sinut.")
                        else:
                            print("Joskus kannattaisi ottaa riski. Nyt olet nössö sankari, ja palaat kotiin kosmisella maitojunalla.")
                else:
                    print("Läpimeneminen ei aina kannata. Nyt olet sitten tyhmänrohkea sankari. RIP.")
            else:
                print("Merkuriukseen mennessäsi törmäät aurinkoon. Olet nyt kansan mielestä kuuma sankari. Oikeastikin tuli lämpimät olot.")
        else:
            print("Kaasutitkin vähän liikaa. Valonnopeuden ylittyessä aluksesi tuhoutui. Olet nyt joillekin kahjo sankari.")
    else:
        print("Oho, törmäsit kummalliseen olioon ja aluksesi nielaistiin. No... olet nyt joillekin rohkea sankari.")
else:
    choicevo = input("Zuuuum! Ylös! Vasen vai oikea? ").lower()
    if choicevo == "oikea":
        choicekh = input("Oikea kurvi... kaasua vai jarrua? ").lower()
        if choicekh == "jarrua":
            choicejs = input("Fiksu päätös varmasti. Suuntaatko Jupiteria kohti (j) vai Saturnusta kohti (s) seuraavaksi? ").lower()
            if choicejs == "j":
                choicelv = input("Selvä homma, Jupiteriin siis. Oho, matkalla on valtaisa kaasupilvi! Läpi vai väistö? ").lower()
                if choicelv == "väistö":
                    choicekl = input("Fiksu veto tuo väistäminen! Ties mitä kaasupilvestä olisi löytynyt. Lähdetkö ulos aurinkokunnasta (u) vai takaisin kotiin (k)? ").lower()
                    if choicekl == "k":
                        print("Selvisit kotiin! Voitto se on tämäkin. Nyt olet sentään käynyt avaruudessa!")
                    else:
                        choicelk = input("Ulos siis. Hurjaa. Kauas vai lähelle? ").lower()
                        if choicelk == "kauas":
                            choicehk = input("Kaaaauas! Hitaasti (h) vai kovaa (k)? ").lower()
                            if choicehk == "k":
                                print("Se oli järkevää! Ehdit ihastella maisemiakin ennen kuin palasit kotiin sankarina.")
                            else:
                                print("Se oli fiksua! Ehdit todella kauas ennen paluutasi kotiin.")
                        else:
                            print("Olisi kannattanut ottaa riski. Ehkä et olisi törmännyt villisti riuhtovaan koivunrunkoon. Mistä se edes tuli avaruuteen!?")
                else:
                    print("Kaasupilvessä oli aikamoinen eldritch abomination. Tulit syödyksi. Avaruudessa kukaan ei kuule huutoasi.")
            else:
                print("Saturnukseen oli muitakin matkalla. Ruuhkassa lentää helposti kolarin. Crash boom bang!")
        else:
            print("Liika kaasu ei olisi kannattanut. Kone ylikuumeni, kabuum.")
    else:
        print("Vasemmalla odotti asteroideja. Höh. No, aluksesi räjähdys näkyi Telluksellekin.")