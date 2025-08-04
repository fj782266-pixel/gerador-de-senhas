import random
import string
import pyperclip

def gerar_senha(tamanho=12, letras=True, numeros=True, simbolos=True):
    caracteres = ""
    
    if letras:
        caracteres += string.ascii_letters
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return None  # Retorna None se não tiver caracteres selecionados

    return ''.join(random.choice(caracteres) for _ in range(tamanho))

print("=== GERADOR DE SENHAS SEGURAS ===")

# Validação de entrada com limite
while True:
    tamanho_input = input("Digite o tamanho da senha (8 a 32): ")
    if tamanho_input.isdigit():
        tamanho = int(tamanho_input)
        if 8 <= tamanho <= 32:
            break
        else:
            print("⚠️ Digite um valor entre 8 e 32!")
    else:
        print("⚠️ Por favor, digite apenas números!")

usar_letras = input("Incluir letras? (s/n): ").lower() == 's'
usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

senha = gerar_senha(tamanho, usar_letras, usar_numeros, usar_simbolos)

if senha:
    print(f"\n🔐 Sua senha gerada: {senha}")
    try:
        pyperclip.copy(senha)
        print("📋 A senha foi copiada automaticamente para a área de transferência!")
    except:
        print("❌ Não foi possível copiar a senha. Instale o pacote 'pyperclip'.")
else:
    print("\n⚠️ Erro: Nenhum tipo de caractere foi selecionado! Execute o programa novamente.")
