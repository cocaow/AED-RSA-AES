import subprocess
import itertools
import string
import time

KEY_PUBLIC_EN = '/home/marininha/Desktop/RSA - AES/key_public.en'
KEY_FOR_MESSAGE_EN = '/home/marininha/Desktop/RSA - AES/key_for_message.en'
KEY_FOR_RSA_HASH = '/home/marininha/Desktop/RSA - AES/key_for_rsa_public.hash'
MESSAGE_EN = '/home/marininha/Desktop/RSA - AES/message.en'

with open(KEY_FOR_RSA_HASH, 'r') as f:
    hash_senha = f.read().strip()

def brute_force_hash(prefix, hash_senha, hash_type="sha256"):
    """ Tenta encontrar a senha correta por força bruta, assumindo que tem 12 caracteres. """
    caracteres = string.ascii_letters + string.digits
    
    for sufixo in itertools.product(caracteres, repeat=10):
        tentativa = prefix + ''.join(sufixo)
        tentativa_hash = subprocess.run([
            "echo", "-n", tentativa, "|", "openssl", "dgst", "-{}".format(hash_type)
        ], capture_output=True, text=True).stdout.strip().split("= ")[-1]
        
        if tentativa_hash == hash_senha:
            return tentativa
    return None

start_time = time.time()

print("Tentando quebrar a senha...")
senha = brute_force_hash("mi", hash_senha)

if senha:
    print(f"Senha encontrada: {senha}")
    
    decrypted_rsa_key = "key_public_decrypted.pem"
    subprocess.run(["openssl", "enc", "-d", "-aes-256-cbc", "-in", KEY_PUBLIC_EN,
                    "-out", decrypted_rsa_key, "-pass", f"pass:{senha}"])
    
    print("Chave pública descriptografada!")
    
    decrypted_aes_key = "aes_key_decrypted.bin"
    subprocess.run(["openssl", "rsautl", "-decrypt", "-inkey", decrypted_rsa_key,
                    "-in", KEY_FOR_MESSAGE_EN, "-out", decrypted_aes_key])
    
    print("Chave AES descriptografada!")
    
    decrypted_message = "message_decrypted.txt"
    subprocess.run(["openssl", "enc", "-d", "-aes-256-cbc", "-in", MESSAGE_EN,
                    "-out", decrypted_message, "-pass", f"file:{decrypted_aes_key}"])
    
    print("Mensagem descriptografada! Verifique o arquivo message_decrypted.txt")
else:
    print("Falha ao encontrar a senha!")

end_time = time.time()
total_time = end_time - start_time
print(f"Tempo total de execução: {total_time:.2f} segundos")
