def hamming_74(data):
    data_bits = [int(bit) for bit in format(data, '04b')]
    print(data_bits)
    parity_bits = [
        (data_bits[0] + data_bits[1] + data_bits[3]) % 2,
        (data_bits[0] + data_bits[2] + data_bits[3]) % 2,
        (data_bits[1] + data_bits[2] + data_bits[3]) % 2
    ]

    codeword = data_bits + parity_bits

    return codeword

def hamming_95(data):
    data_bits = [int(bit) for bit in format(data, '05b')]
    print(data_bits)
    parity_bits = [
        (data_bits[0] + data_bits[1] + data_bits[2] + data_bits[4]) % 2,
        (data_bits[0] + data_bits[1] + data_bits[3] + data_bits[4]) % 2,
        (data_bits[0] + data_bits[2] + data_bits[3] + data_bits[4]) % 2,
        (data_bits[1] + data_bits[2] + data_bits[3] + data_bits[4]) % 2
    ]

    codeword = data_bits + parity_bits

    return codeword

# Тестовые данные
data = 10

# Вычисление кодов Хемминга
codeword_74 = hamming_74(data)
codeword_95 = hamming_95(data)

# Вывод результатов
print("Код (7,4):", codeword_74)
print("Код (9,5):", codeword_95)

# Сравнение избыточности
print("Избыточность кода (7,4):", len(codeword_74) - 4)
print("Избыточность кода (9,5):", len(codeword_95) - 5)

# Сравнение корректирующей мощности
print("Корректирующая мощность обоих кодов:", 1)
