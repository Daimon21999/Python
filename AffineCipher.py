class Affine:
    def __init__(self):
        self.alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.mode = self.mode = input('Input mode: [E]ncript | [D]ecript ==> ').upper()
        if self.mode not in ['E', 'D']:
            print('ERROR -> Incorrect option\nTry Again'); raise SystemExit
        self.keys = input('Input keys a b (a - prime number, b - 0 .. 25)\n ').split()
        self.a = int(self.keys[0]); self.b = int(self.keys[1]); self.m = 26
        self.mess = input('Input Message ==> ').upper()
        self.result = ''.join(self.encrypt_decrypt())

    def encrypt_decrypt(self):
        mess_indexes_list = [self.alpha.index(i) for i in self.mess]
        processed_mess_int = list(); processed_mess_string = list()

        if self.mode.upper() == 'E':
            # a * s + b ( mod 26 )
            for s in mess_indexes_list:
                processed_mess_int.append((self.a * s + self.b) % self.m)
            for s in processed_mess_int:
                processed_mess_string.append(self.alpha[s])
        elif self.mode.upper() == 'D':
            # -a * (s + m - b) mod m
            for s in mess_indexes_list:
                processed_mess_int.append((pow(self.a, 2) * (s + self.m - self.b) % self.m))
            for s in processed_mess_int:
                processed_mess_string.append(self.alpha[s])
        return processed_mess_string

    def __repr__(self):
        return self.result


if __name__ == '__main__':

    tmp = Affine()
    print(tmp)

