class Binary:
    def __init__(self) -> None:
        self.table = []

    def number_to_binary(self, number: int) -> str:
        self.number = number

        while True:
            if (self.number == 2) or (self.number <= 1):
                self.table.append(self.number % 2)
                self.table.append(int(self.number / 2))
                break

            self.table.append(self.number % 2)
            self.number = int(self.number / 2)
            continue

        self.table.reverse()

        if (self.table[0] == 0) and (self.number <= 1):
            self.table.pop(0)

        self.result = [
            str(element).replace('\n', '') for element in self.table
            ]

        return str(object="").join(self.result)
    
    def binary_to_number(self, binary: int) -> str:
        self.number = binary
        self.binary = [
            int(char) for char in str(binary)
            ]
        self.binary.reverse()
        self.length = [
            int(number) for number in range(len(self.binary))
            ]
        self.result = sum([
            int(self.binary[n] * (2 ** n)) for n in self.length
            ])

        return str(self.result)
    
    # code with cisco :D