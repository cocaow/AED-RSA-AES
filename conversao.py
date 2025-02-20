import base64

# A string Base64
base64_hash = "t8TT9lwdQ4sYw0ibxFQN6dXxjnOGuusGHbEcRVNX8BM="

# Descodificar o Base64
decoded_bytes = base64.b64decode(base64_hash)

# Salvar o resultado como um arquivo binário
with open("decoded_hash.bin", "wb") as f:
    f.write(decoded_bytes)

print("Arquivo binário gerado com sucesso!")
