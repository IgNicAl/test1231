from src.onlyfiles.utils.file_navigator import FileNavigator

def main():
    print("Testando o navegador de arquivos...")
    navigator = FileNavigator()
    
    # Testar a navegação
    selected_path = navigator.navigate()
    
    if selected_path:
        print(f"\nCaminho selecionado: {selected_path}")
        print("\nNOTA: Este é apenas um teste de navegação. Para organizar os arquivos,")
        print("      use o programa principal com as opções de organização.")
    else:
        print("\nNavegação cancelada pelo usuário.")

if __name__ == "__main__":
    main() 