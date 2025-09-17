class Cliente:
    def __init__(self, nome, email, piva, via, citta): # Aggiunti via e citta
        self.nome = nome
        self.email = email
        self.piva = piva
        self.via = via
        self.citta = citta

    def scheda_riepilogativa(self):
        return f"Cliente: {self.nome} - Contatto: {self.email}"

    # Questo è un metodo che si comporta come un attributo
    @property
    def indirizzo_completo(self):
        return f"{self.via}, {self.citta}"

# ClienteVIP eredita da Cliente
class ClienteVIP(Cliente):
    def __init__(self, nome, email, piva, via, citta, sconto_percentuale):
        # Chiama il costruttore della classe "madre" (Cliente)
        # per fargli fare il suo lavoro (impostare nome, email, etc.)
        super().__init__(nome, email, piva, via, citta)

        # Ora aggiungiamo l'attributo che solo i VIP hanno
        self.sconto = sconto_percentuale

    # Ora SOVRASCRIVIAMO il metodo della madre per farlo comportare diversamente
    def scheda_riepilogativa(self):
        # Possiamo anche richiamare il metodo originale della madre se ci serve!
        scheda_base = super().scheda_riepilogativa()
        return f"{scheda_base} [VIP - Sconto: {self.sconto}%]"
    
# --- Programma Principale ---

# Un cliente normale
cliente_normale = Cliente(
    "Mario Rossi",
    "mario.rossi@email.com",
    "12345678901",
    "Via Roma 10",
    "Torino"
)

# Un cliente VIP!
cliente_vip = ClienteVIP(
    "Luigi Verdi",
    "luigi.verdi@email.com",
    "98765432109",
    "Corso Garibaldi 25",
    "Milano",
    15  # Questo è lo sconto del 15%
)

print("--- Schede Clienti ---")
print(cliente_normale.scheda_riepilogativa())
print(cliente_vip.scheda_riepilogativa()) # Eseguirà il metodo sovrascritto!

print("\n--- Indirizzi (grazie a @property) ---")
# Nota: chiamiamo indirizzo_completo SENZA parentesi ()!
print(f"Indirizzo Mario: {cliente_normale.indirizzo_completo}")
print(f"Indirizzo Luigi: {cliente_vip.indirizzo_completo}") # L'ha ereditato gratis!