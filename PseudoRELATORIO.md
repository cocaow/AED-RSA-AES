# Relatório do Desafio de Criptoanálise: AES-256 e RSA

## 1. Introdução
Este relatório documenta o processo de descriptografia de uma mensagem cifrada utilizando AES-256, cuja chave estava protegida por RSA. A chave pública RSA, por sua vez, estava cifrada com AES-256, e apenas parte da senha utilizada para sua criptografia era conhecida. O objetivo do trabalho foi quebrar a senha, recuperar as chaves e acessar a mensagem original.

## 2. Metodologia
O procedimento seguido para a recuperação da mensagem envolveu as seguintes etapas:

### 2.1. Quebra da Senha AES-256 da Chave Pública RSA
- O arquivo `key_for_rsa_public.hash` continha o hash da senha utilizada para cifrar a chave RSA.
- Foi utilizado um ataque de força bruta, assumindo que a senha tinha 12 caracteres e começava com "mi".
- Para validar cada tentativa de senha, foi calculado seu hash e comparado com o hash fornecido.

### 2.2. Descriptografia da Chave Pública RSA
- Com a senha recuperada, a chave pública (`key_public.en`) foi descriptografada usando OpenSSL.

### 2.3. Descriptografia da Chave AES da Mensagem
- A chave AES usada para cifrar a mensagem estava no arquivo `key_for_message.en`, criptografada com a chave RSA.
- A chave privada foi utilizada para descriptografar a chave AES.

### 2.4. Descriptografia da Mensagem Final
- A mensagem cifrada (`message.en`) foi decifrada utilizando a chave AES recuperada.

## 3. Implementação
O processo foi automatizado com um script Python, que executou as seguintes etapas:
- Cálculo de hashes para força bruta da senha AES-256.
- Descriptografia da chave pública RSA.
- Descriptografia da chave AES da mensagem.
- Decifração final da mensagem.

O script utilizou as bibliotecas `subprocess`, `itertools` e `string` para automação e execução de comandos OpenSSL.

## 4. Especificação do Ambiente de Execução
- **Sistema Operacional**: [Informe o sistema operacional utilizado, ex: Ubuntu 22.04]
- **Hardware**: Intel Core i5-11400H, GPU NVIDIA GTX 1650
- **Ferramentas Utilizadas**:
  - OpenSSL: [Informe a versão]
  - Python: [Informe a versão]
  - Bibliotecas Python: `subprocess`, `itertools`, `string`

## 5. Desafios Encontrados
- **Força Bruta**: A execução do brute-force foi inicialmente desafiadora devido ao número elevado de tentativas necessárias. Ajustes no script foram feitos para otimizar o processo e evitar sobrecarga.
- **Otimização**: Algumas alternativas de implementação foram testadas, como a utilização de ferramentas para acelerar o brute-force ou o uso de máquinas virtuais com maior capacidade de processamento.

## 6. Tempo de Execução e Otimizações
- O tempo total de execução foi aproximadamente **XX minutos**.
- **Otimizações Realizadas**:
  - Paralelização das tentativas de senha.
  - Uso de hash mais eficiente para reduzir o tempo de comparação.
  
Caso o brute-force tenha demorado mais do que o esperado, testes alternativos, como a busca de senhas menores ou outros padrões, foram realizados.

## 7. Implicações de Segurança
Este desafio demonstrou a importância de senhas fortes para proteger informações sensíveis. Através da força bruta, foi possível recuperar a senha e acessar os dados protegidos. 

Reflexões sobre como a criptografia pode ser vulnerável a ataques de força bruta:
- **Senhas fracas ou previsíveis** são alvo fácil de ataques de força bruta.
- **Criptografia** baseada apenas em senhas deve ser combinada com outras camadas de segurança, como chaves de acesso ou autenticação multifatorial.

**Boas práticas recomendadas**:
- Uso de senhas longas e geradores aleatórios.
- Implementação de criptografia simétrica combinada com criptografia assimétrica para maior segurança.
- Consideração de algoritmos de hash resistentes a ataques de força bruta.

## 8. Resultados
- A senha encontrada foi: `************` (ocultada para conformidade com o desafio).
- A mensagem decifrada foi: `"[conteúdo da mensagem]"`.
- O tempo total de execução foi aproximadamente **XX minutos**.

## 9. Conclusão
O desafio demonstrou a importância de senhas fortes para proteger informações sensíveis. Através da força bruta, foi possível recuperar a senha e acessar os dados protegidos. Este experimento reforça a necessidade de boas práticas de segurança, como o uso de senhas longas e geradores aleatórios.

## 10. Anexos
- Código-fonte do script utilizado.
    decrypt.py
- Arquivos processados.
    key_for_message.en
    key_for_rsa_public.hash
    key_public.en
    message.en
    
