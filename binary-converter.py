def biner_to_desimal(biner):
    desimal = int(biner, 2)
    return desimal


print("""
    --------------------------------
    [+] Convert Binary to Decimal [+]
    --------------------------------
""")

print("[*] Type binary numbers and convert to decimal ..")
print("[*] ex: 10110010, without space")

prompt = '> '

biner_input = input(prompt)
desimal_output = biner_to_desimal(biner_input)

format = desimal_output

print(f"Result: {format}")
