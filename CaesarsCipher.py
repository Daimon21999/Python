from colorama import Fore, Back, init


class CaesarsCipher:
    def __init__(self):
        init()
        self.alphabet = self._create_alphabet()

    def _create_alphabet(self):
        d = dict()
        s = 'abcdefghijklmnopqrstuvwxyz'
        for i, letter in enumerate(s):
            d[letter] = i
        return d

    def encrypt(self, key, message):
        s = ''
        for letter in message:
            try:
                index = (self.alphabet[letter] + key) % 26
            except:
                s += letter
                continue

            for l, i in self.alphabet.items():
                if i == index:
                    s += l
                    break
        return s

    def decrypt(self, key, message):
        s = ''
        for letter in message:
            try:
                index = (self.alphabet[letter] - key) % 26
            except:
                s += letter
                continue
            for l, i in self.alphabet.items():
                if i == index:
                    s += l
                    break
        return s

    def menu(self):
        while True:
            print(Fore.RESET + Back.RESET, end='')
            message = input(Back.RED + Fore.BLACK + 'Input message: ').lower()
            try:
                key = int(input('Input key: '))
                if key > 26:
                    raise Exception('Incorrect option')
            except:
                print('Incorrect option')
                continue

            choose = input(Back.GREEN + Fore.BLACK + 'e-encrypt, d-decrypt: ')

            if choose.lower() in ['e', 'encrypt']:
                print(Back.LIGHTGREEN_EX + Fore.BLACK + self.encrypt(key=key, message=message))
                tmp = input('Continue (Y/N): ')
                if tmp.lower() == 'y':
                    continue
                else:
                    break
            elif choose.lower() in ['d', 'decrypt']:
                print(Back.LIGHTCYAN_EX + Fore.BLACK + self.decrypt(key=key, message=message))
                tmp = input('Continue (Y/N): ')
                if tmp.lower() == 'y':
                    continue
                else:
                    break
            else:
                print('Incorrect option')


if __name__ == '__main__':
    cezar = CaesarsCipher()
    cezar.menu()
