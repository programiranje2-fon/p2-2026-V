from sys import stderr
from datetime import datetime

class Putnik:

    def __init__(self, ime, zemlja, pasos, COVID_safe=False):
        self.ime = ime
        self.zemlja = zemlja
        self.pasos = pasos
        self.COVID_bezbedan = COVID_safe

    @property
    def pasos(self):
        if not hasattr(self, '_Putnik__pasos'):
            self.__pasos = None
        return self.__pasos

    @pasos.setter
    def pasos(self, value):
        if isinstance(value, str) and len(value) == 6 and value.isdigit():
            self.__pasos = value
            return
        if isinstance(value, int) and len(str(value)) == 6:
            self.__pasos = str(value)
            return

        stderr.write(f"Neadekvatna vrednost ({value}) za pasos putnika -> vrednost nije postavljena\n")


    def __str__(self):
        putnik_str = f"Putnik {self.ime}\n"
        putnik_str += f"\tbroj pasosa: {self.pasos if self.pasos else 'nepoznat'}\n"
        putnik_str += f"\tdrzavljanstvo: {self.zemlja}\n"
        putnik_str += f"\tCOVID status: {'bezbedan' if self.COVID_bezbedan else 'inficiran'}"
        return putnik_str


    def azuriraj_COVID_bezbedan(self, tip_uverenja, datum_uverenja):
        if tip_uverenja.lower() not in ['vakcinacija', 'negativan_test']:
            stderr.write(f"Pogresna vrednost za tip uverenja ({tip_uverenja}) -> azuriranje ne moze biti izvrseno\n")
            return
        if not isinstance(datum_uverenja, (str, datetime)):
            stderr.write(f"Pogresna vrednost za datum uverenja ({datum_uverenja}) -> azuriranje ne moze biti izvrseno\n")
            return

        if isinstance(datum_uverenja, str):
            datum_uverenja = datetime.strptime(datum_uverenja, '%d/%m/%Y')

        td_days = (datetime.now() - datum_uverenja).days
        # Option 1
        # if (tip_uverenja.lower() == 'vakcinacija' and td_days < 365) or (tip_uverenja == 'negativan_test' and td_days < 3):
        #     self.COVID_bezbedan = True
        # else:
        #     self.COVID_bezbedan = False
        # Option 2
        self.COVID_bezbedan = (tip_uverenja.lower() == 'vakcinacija' and td_days < 365) or (tip_uverenja == 'negativan_test' and td_days < 3)

        print(f"COVID status putnika je uspesno azuriran - nova vrednost je {self.COVID_bezbedan}")

    @classmethod
    def from_string(cls, str_data):
        parts = [part.strip() for part in str_data.split(';')]
        if len(parts) == 4:
            # Option 1
            # ime, zemlja, pasos, covid = parts
            # return cls(ime, zemlja, pasos, covid)
            # Option 2
            return cls(*parts)
        stderr.write(f"Neadekvanta string vrednost za kreiranje Putnik objekta\n")
        return None

    def __eq__(self, other):
        return isinstance(other, Putnik) and other.zemlja == self.zemlja and other.pasos == self.pasos


if __name__ == '__main__':
    bob = Putnik("Bob Smith", "UK", "123456", True)
    john = Putnik("John Smith", "USA", 987656, True)
    anna = Putnik("Anna Smith", "Spain", "987659")
    luis = Putnik.from_string("Luis Bouve; France; 123456; True")

    print("PUTNICI:\n")
    print(bob)
    print(john)
    print(anna)
    print(luis)

    print("\nPUTNICI NAKON UPDATE-a COVID STATUS-a:\n")
    anna.azuriraj_COVID_bezbedan('vakcinacija', '01/02/2024')
    print(anna)

    luis.azuriraj_COVID_bezbedan('negativan_test', '04/11/2024')
    print(luis)
    print()

    print("Provera da li su 'bob' i 'john' reference na istog putnika")
    print("Isti putnik" if bob == john else "Razliciti putnici")
    print()
    print("Provera da li su 'john' i 'johnny' reference na istog putnika")
    johnny = Putnik("Johnny Smith", "USA", 987656, False)
    print("Isti putnik" if john == johnny else "Razliciti putnici")
