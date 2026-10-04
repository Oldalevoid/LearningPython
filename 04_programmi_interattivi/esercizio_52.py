# DESCRIZIONE
# Introduce un primo sistema di attacco tra l'esercito del giocatore e un esercito nemico.
# L'utente sceglie sia l'unità attaccante sia il bersaglio e il Danno dell'attaccante
# viene sottratto alla Vita del nemico selezionato.
#
# COSA HO IMPARATO IN QUESTO ESERCIZIO
# - Usare una statistica di un'unità per modificare lo stato di un'altra unità
# - Selezionare separatamente attaccante e bersaglio
# - Gestire due liste di unità differenti
# - Impedire che la Vita scenda sotto zero
# - Gestire i casi in cui uno degli eserciti è vuoto
# - Usare più indici nello stesso flusso di gioco

unitadisponibili = [
    {
        "Tipo": "Giuseppe The Butcher 'Chiappacelli",
        "Vita": 1000,
        "Costo": 400,
        "Danno": 100,
        "Potere": "Divinità",
        "Livello": 1
    },
    {
        "Tipo": "Gisella The Golden Gremlin",
        "Vita": 800,
        "Costo": 150,
        "Danno": 100,
        "Potere": "Divinità",
        "Livello": 1
    }
]

esercitoAmandola = []

esercitoNemico = [
    {
        "Tipo": "Goblin",
        "Vita": 100,
        "Danno": 30
    },
    {
        "Tipo": "Arcere Goblin",
        "Vita": 80,
        "Danno": 20
    }
]

oro = 1000


def mostramenu(oro):
    while True:
        print("1 - Mostra esercito")
        print("2 - Recluta unità")
        print("3 - Riepilogo esercito")
        print("4 - Mostra oro")
        print("5 - Elimina unità")
        print("6 - Livella unità")
        print("7 - Attacca nemico")
        print("0 - Esci")

        scelta = chiediscelta("Scegli un'opzione: ", 0, 7)

        if scelta == 0:
            break

        elif scelta == 1:
            mostraesercito(esercitoAmandola)

        elif scelta == 2:
            oro = recluta(unitadisponibili, esercitoAmandola, oro)

        elif scelta == 3:
            riepilogaesercito(esercitoAmandola)

        elif scelta == 4:
            print(f"Oro rimasto: {oro}")

        elif scelta == 5:
            eliminaunita(esercitoAmandola)

        elif scelta == 6:
            livellaunita(esercitoAmandola)

        elif scelta == 7:
            attaccanemico(esercitoAmandola, esercitoNemico)

    return oro


def attaccanemico(esercito, esercitonemico):
    if len(esercito) == 0:
        print("Non hai unità con cui attaccare")
        return

    if len(esercitonemico) == 0:
        print("Non ci sono più nemici")
        return

    print("Scegli l'unità che deve attaccare:")

    for numero, unita in enumerate(esercito, start=1):
        print(
            numero,
            "-",
            unita["Tipo"],
            "- Danno:",
            unita["Danno"]
        )

    scelta = chiediscelta(
        "Quale unità deve attaccare? ",
        1,
        len(esercito)
    )

    indice = scelta - 1

    print("Scegli il bersaglio:")

    for numero, unita in enumerate(esercitonemico, start=1):
        print(
            numero,
            "-",
            unita["Tipo"],
            "- Vita:",
            unita["Vita"]
        )

    scelta_bersaglio = chiediscelta(
        "Quale unità deve essere attaccata? ",
        1,
        len(esercitonemico)
    )

    indice_bersaglio = scelta_bersaglio - 1
    danno = esercito[indice]["Danno"]

    esercitonemico[indice_bersaglio]["Vita"] -= danno

    print(
        f"{esercito[indice]['Tipo']} infligge "
        f"{danno} danni a {esercitonemico[indice_bersaglio]['Tipo']}"
    )

    if esercitonemico[indice_bersaglio]["Vita"] <= 0:
        esercitonemico[indice_bersaglio]["Vita"] = 0
        print(f"{esercitonemico[indice_bersaglio]['Tipo']} eliminato!")
    else:
        print(
            f"{esercitonemico[indice_bersaglio]['Tipo']} tentenna. "
            f"Vita rimasta: {esercitonemico[indice_bersaglio]['Vita']}"
        )


def chiediscelta(messaggio, minimo, massimo):
    while True:
        try:
            scelta = int(input(messaggio))

            if scelta < minimo or scelta > massimo:
                print("Inserisci un valore valido")
                continue

            return scelta

        except ValueError:
            print("Inserisci un intero")


def livellaunita(esercito):
    if len(esercito) == 0:
        print("L'esercito è vuoto")
        return

    for numero, unita in enumerate(esercito, start=1):
        print(numero, "-", unita["Tipo"])

    scelta = chiediscelta(
        "Quale unità vuoi livellare? ",
        1,
        len(esercito)
    )

    indice = scelta - 1

    esercito[indice]["Danno"] += 5
    esercito[indice]["Livello"] += 1
    esercito[indice]["Vita"] += 5

    print(
        f"{esercito[indice]['Tipo']} è ora al livello "
        f"{esercito[indice]['Livello']}"
    )


def eliminaunita(esercito):
    if len(esercito) == 0:
        print("L'esercito è vuoto")
        return

    for numero, unita in enumerate(esercito, start=1):
        print(numero, "-", unita["Tipo"])

    scelta = chiediscelta(
        "Quale unità vuoi eliminare? ",
        1,
        len(esercito)
    )

    indice = scelta - 1
    esercito.pop(indice)


def mostraesercito(esercito):
    if len(esercito) == 0:
        print("L'esercito è vuoto")
    else:
        for numero, unita in enumerate(esercito, start=1):
            print(
                numero,
                "-",
                unita["Tipo"],
                "- Livello:",
                unita["Livello"],
                "- Vita:",
                unita["Vita"],
                "- Danno:",
                unita["Danno"],
                "- Potere:",
                unita["Potere"]
            )


def mostracatalogo(caserma):
    for numero, unita in enumerate(caserma, start=1):
        print(numero, "-", unita["Tipo"], "- Costo:", unita["Costo"])


def recluta(caserma, esercito, oro):
    mostracatalogo(caserma)

    while True:
        print("0 - Termina il reclutamento")

        scelta = chiediscelta(
            "Quale unità vuoi reclutare? ",
            0,
            len(caserma)
        )

        if scelta == 0:
            break

        indice = scelta - 1

        if oro >= caserma[indice]["Costo"]:
            oro -= caserma[indice]["Costo"]
            print(f"Hai reclutato {caserma[indice]['Tipo']}")
            esercito.append(caserma[indice].copy())
        else:
            print("Fondi non sufficienti")

    return oro


def calcolavaloreesercito(esercito):
    valore = 0

    for unita in esercito:
        valore += unita["Costo"]

    return valore


def calcolavitatotaleesercito(esercito):
    lifepoints = 0

    for unita in esercito:
        lifepoints += unita["Vita"]

    return lifepoints


def riepilogaesercito(esercito):
    unitatotali = len(esercito)
    valoretotale = calcolavaloreesercito(esercito)
    vitatotale = calcolavitatotaleesercito(esercito)

    print(f"Unità totali: {unitatotali}")
    print(f"Valore totale: {valoretotale}")
    print(f"Vita totale: {vitatotale}")


oro = mostramenu(oro)
