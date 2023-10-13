# Pizza al taglio
Si scriva un programma che permetta di calcolare i valori nutrizionali delle teglie di pizza di una pizzeria.

I moduli e le classi vanno sviluppati nel package *restaurant*.
Non spostare o rinominare moduli e classi esistenti e non modificare le signature dei metodi.

In *main.py* viene fornito del semplice codice, da voi modificabile, che testa le funzionalità base.
Esso mostra esempi di uso dei metodi principali ed esempi dei controlli richiesti.

Tutte le eccezioni, se non altrimenti specificato, sono di tipo *TrayException* definita nel modulo *exceptions*.


## R1: Ingredienti (5/19)
La classe astratta *Nutritional* del modulo *nutritional* rappresenta le proprietà nutritive di un prodotto alimentare.
Essa definisce le property astratte:
- ```name(self) -> str```
- ```carbs(self) -> float```
- ```fat(self) -> float```
- ```proteins(self) -> float```

Esse forniscono, rispettivamente, il nome, e le quantità in grammi di carboidrati, grassi e proteine.

La classe *Pizzeria* del modulo *pizzeria* permette di aggiungere diversi ingredienti.

Il metodo ```create_ingredient(self, name: str, carbs: float, fat: float, proteins: float) -> Nutritional```,
permette di definire un nuovo ingrediente per il condimento delle pizze,
specificandone il nome, e i suoi valori nutrizionali.
Il metodo restituisce un ```Nutritional``` che rappresenta l'ingrediente.
Per gli ingredienti i valori nutrizionali sono espressi su 100 g.

Il metodo ```get_ingredient(self, name: str) -> Nutritional```
permette di ottenere l'oggetto rappresentante l'ingrediente, dato il suo nome.

La rappresentazione in stringa (```__str__(self) -> str```) di un ingrediente
deve contenerne il nome, grammi di carboidrati, grammi di grassi e grammi proteine,
in quest'ordine e separati da spazi.
I grammi dei valori nutrizionali vanno espressi su due cifre decimali.
Esempio:
- *Pomodoro 17.00 0.20 4.20*

L'ordinamento degli oggetti rappresentanti gli ingredienti deve avvenire automaticamente per nome,
quando viene utilizzato ```sort``` o ```sorted``` su una collezione ordinabile che li contiene (ad. es. una lista).


## R2: Teglie (4/19)
**ATTENZIONE**: Conviene leggere anche R3 per impostare il codice in modo corretto fin da subito.

La classe *Pizzeria* fornisce dei metodi per gestire le teglie di pizza.
Una teglia di pizza può essere rappresentata da una scacchiera di fette, ognuna contenente ingredienti su più strati.
Lo stesso ingrediente **PUO' ESSERE RIPETUTO** su più strati.

Il metodo ```create_pizza_tray(self, name: str, size: int) -> None```
permette di creare una teglia di pizza **QUADRATA**,
dato il nome e la dimensione (numero di fette su un lato).

Il metodo ```add_tray_ingredient(self, tray_name: str, ingredient_name: str, pos: Tuple[int, int], size, quantity: float) -> None```
permette di aggiungere un ingrediente alla teglia.
Il primo parametro è il nome della teglia e il secondo il nome dell'ingrediente.

L'ingrediente deve essere distribuito su un'area **QUADRATA** della teglia.
Il parametro ```pos``` è una *Tupla* contenente riga e colonna dell'angolo in alto a sinistra
dell'area su cui viene aggiunto l'ingrediente.
Gli indici di riga e colonna partono da zero.
Il parametro ```size``` indica la lunghezza del lato dell'area, in termini di numero di fette.
L'ultimo parametro indica in grammi **TOTALI** dell'ingrediente aggiunto.

L'ingrediente aggiunto va a occupare **IL PRIMO STRATO LIBERO** di ciascuna fetta sui cui è aggiunto.

Il metodo lancia un'eccezione se l'area su cui si vuole aggiungere l'ingrediente esce dai confini della teglia.

Il metodo ```get_pizza_tray(self, name: str) -> Nutritional``` restituisce un ```Nutritional``` rappresentante la teglia.
I valori nutritivi di una teglia sono la somma dei quelli dei suoi ingredienti.
A differenza degli ingredienti questi devono essere **TOTALI** e **NON** riferiti a 100 g.


## R3: Strati e Fette (4/19)
La classe *Pizzeria* fornisce dei metodi per ottenere informazioni su fette e strati d'ingredienti delle teglie di pizza.

Il metodo ```get_slice(self, tray_name: str, pos: Tuple[int, int]) -> List[Nutritional]```
fornisce la lista degli ingredienti di una fetta, partendo dallo strato inferiore.
Il metodo accetta come parametri il nome della teglia e una *Tupla* contenente riga e colonna della fetta.

Il metodo ```get_layer(self, tray_name: str, num_layer: int) -> List[List[str]]```
accetta come parametri il nome di una teglia e il numero di uno strato.
Gli strati sono numerati partendo da zero da quello inferiore.
Il metodo restituisce una tabella contenente gli ingredienti di tutte le fette della teglia per lo strato indicato.
Se una fetta non ha un ingrediente per lo strato richiesto, la tabella deve contenere *None* nella cella corrispondente.

## R4: Porzioni (4/19)
Il metodo ```get_contiguous_portion(self, tray_name: str, pos: Tuple[int, int], to_avoid: str) -> List[List[bool]]```
della classe *Pizzeria* accetta come parametri il nome di una teglia, la posizione di una fetta sulla teglia
(*Tupla* contenente riga e colonna) e il nome di un ingrediente non gradito.

Il metodo individua l'insieme di fette contigue della teglia (porzione), contenente la fetta indicata,
che non hanno l'ingrediente che si vuole evitare in nessuno dei loro strati.

Le fette sono contigue se si toccano su un lato.
Due fette che si toccano in diagonale **NON** sono contigue.

Il metodo restituisce una tabella di valori booleani contenente *True* nelle celle corrispondenti alle fette
appartenenti alla porzione individuata e *False* in **TUTTE** le altre.


## R5: Ingredienti preferiti (2/19)
Il metodo ```sort_slice(self, tray_name: str, pos: Tuple[int, int], score_func: Callable[[Nutritional], float]) -> List[Nutritional]```
riceve come parametri il nome di una teglia, la posizione di una fetta (*Tupla* contenente riga e colonna)
e una funzione che, ricevendo come parametro un ```Nutritional``` rappresentante un ingrediente, ne restituisce una valutazione.

Il metodo deve restituire la lista degli ingredienti della fetta,
ordinati in modo crescente in base alla funzione di valutazione.
