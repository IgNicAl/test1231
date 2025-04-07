from src.onlyfiles.utils.file_navigator import FileNavigator
from src.onlyfiles.core.file_organizer import FileOrganizer
import os

def main():
    print("Testando o navegador de arquivos e organizador...")
    
    # Testar a navegação
    navigator = FileNavigator()
    selected_path = navigator.navigate()
    
    if selected_path:
        print(f"\nCaminho selecionado: {selected_path}")
        
        # Perguntar se deseja organizar os arquivos
        choice = input("\nDeseja organizar os arquivos neste diretório? (s/n): ").strip().lower()
        
        if choice == 's':
            print(f"\nOrganizando arquivos em: {selected_path}")
            try:
                # Organizar por tipo (padrão)
                result = FileOrganizer.organize_directory(selected_path)
                
                # Mostrar resultados
                print("\nArquivos organizados com sucesso!")
                for category, files in result.items():
                    if files:  # Só mostrar categorias com arquivos
                        print(f"\nCategoria: {category}")
                        for file in files:
                            print(f"  - {file}")
            except Exception as e:
                print(f"\nErro ao organizar arquivos: {str(e)}")
    else:
        print("\nNavegação cancelada pelo usuário.")

if __name__ == "__main__":
    main() 