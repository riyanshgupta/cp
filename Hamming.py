def calculate_parity_bits(data):
    parity_bits = []
    for i in range(len(data)):
        if 2**i >= len(data) + i + 1:
            break
        parity_bits.append(2**i)

    for i in parity_bits:
        data.insert(i - 1, None)

    for i in range(len(parity_bits)):
        index = parity_bits[i]
        bit_list = [data[j] for j in range(len(data)) if (j + 1) & index]
        data[index - 1] = '1' if bit_list.count('1') % 2 == 1 else '0'

    return data


def generate_hamming_code(data):
    hamming_code = list(data)
    hamming_code = calculate_parity_bits(hamming_code)
    return ''.join(hamming_code)


def detect_error(hamming_code):
    error_position = 0
    parity_bits = []

    for i in range(len(hamming_code)):
        if 2**i >= len(hamming_code):
            break
        parity_bits.append(2**i)

    for pb in parity_bits:
        bit_list = [hamming_code[j] for j in range(len(hamming_code)) if (j + 1) & pb]
        if bit_list.count('1') % 2 != 0:
            error_position += pb

    if error_position != 0:
        print("Error detected at position:", error_position)
        if hamming_code[error_position - 1] == '0':
            hamming_code = hamming_code[:error_position - 1] + '1' + hamming_code[error_position:]
        else:
            hamming_code = hamming_code[:error_position - 1] + '0' + hamming_code[error_position:]
        print("Corrected code:", hamming_code)
    else:
        print("No error detected.")

    return hamming_code


if __name__ == "__main__":
    data = input("Enter data to be encoded using Hamming Code: ")
    hamming_code = generate_hamming_code(data)
    print("Hamming Code:", hamming_code)

    # Introduce error
    error_position = int(input("Enter the position to introduce an error (0 for no error): "))
    if error_position > 0 and error_position <= len(hamming_code):
        hamming_code = hamming_code[:error_position - 1] + ('0' if hamming_code[error_position - 1] == '1' else '1') + hamming_code[error_position:]
        print("With error:", hamming_code)
    else:
        print("No error introduced.")

    corrected_code = detect_error(hamming_code)