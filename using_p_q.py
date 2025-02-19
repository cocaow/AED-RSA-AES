import gmpy2
from Crypto.PublicKey import RSA

def rsa_keyfromprimes(p, q , e):
    n = gmpy2.mul(p, q)
    phi = gmpy2.mul((p-1), (q-1)) 
    d = gmpy2.invert(e, phi)
    key = RSA.construct((int(n), int (e), int(d), int(p), int(q)))
    return key

def main():
    p = 4775857644794676250173788374034235557066651390842989010331
    q = 5634033005001224569208144003165564895248210119299568609429
    e = 65537

    try: 
        key = rsa_keyfromprimes(p, q, e)
        private_key_pem = key.export_key().decode('utf-8')
        print(private_key_pem)
    except Exception as e:
        print(f"Erro ao gerar a chave: {e}")

if __name__ == "__main__":
    main()