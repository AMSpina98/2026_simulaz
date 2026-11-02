class Model:
    def __init__(self):
        pass
    #L’utente seleziona dal corrispondente menù a
tendina un paese (Country) tra quelli associati ai
clienti nella tabella Customer.
b. Premendo il pulsante “Crea grafo”, l’applicazione
costruisce un grafo orientato e pesato che
rappresenta le relazioni tra clienti appartenenti al
paese selezionato. I vertici sono i clienti
(Customer) che hanno effettuato almeno una
fattura (Invoice) e che risiedono nel paese scelto.
Per ogni cliente C, si calcoli il fatturato totale come
la somma dei campi Total delle sue fatture.
(Suggerimento. Potrebbe essere conveniente
aggiungere un attributo alla classe Customer per
memorizzare il fatturato totale.) Esiste un arco da C1 a C2 se:
1. entrambi hanno effettuato almeno una fattura, e
2. almeno un artista compare in fatture di entrambi (cioè esiste almeno un artista che ha brani acquistati
da C1 e anche da C2, utilizzando le tabelle customer, invoice, invoiceline, track,
album, artist).
Il verso dell’arco è da C1 verso C2 se il fatturato totale di C1 è maggiore di quello di C2; in caso di parità si
inseriscono due archi, uno in ciascun verso. Il peso dell’arco (C1, C2) è la somma dei fatturati dei due clienti.
c. Costruito il grafo, l’applicazione visualizza immediatamente il numero di vertici e il numero di archi.
d. Alla pressione del tasto “Stampa Info”, l’applicazione visualizza: i) il cliente più influente, dove l’influenza di
un cliente è definita come: influenza(C) = peso archi uscenti – peso archi entranti; ii) i 5 archi di peso
massimo, in ordine decrescente di peso.


# modifiche di ale
