# Fungsi penjumlahan
def add(a, b):
    return a + b

# Fungsi pengurangan
def minus(a, b):
    return a - b

# Fungsi perkalian
def mult(a, b):
    return a * b

# Fungsi pembagian
def div(a, b):
    if b == 0:
        return "Tidak bisa bro"
    return a / b

# Fungsi pohon ekspresi
def tree(expression_tree):
    if isinstance(expression_tree, tuple):
        left_operand = tree(expression_tree[0])
        operator = expression_tree[1]
        right_operand = tree(expression_tree[2])

        if operator == '+':
            return add(left_operand, right_operand)
        elif operator == '-':
            return minus(left_operand, right_operand)
        elif operator == '*':
            return mult(left_operand, right_operand)
        elif operator == '/':
            return div(left_operand, right_operand)
    else:
        return expression_tree

# Contoh pohon ekspresi: (2 + 3) * (5 - 1)
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)

print("Hasil evaluasi pohon ekspresi:", result)
