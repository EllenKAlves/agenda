import os

class Contact:
    """Classe para representar os contatos"""
    def __init__(self, name, phone, is_favorite=False):
        self.name = name
        self.phone = phone
        self.is_favorite = is_favorite

    def __str__(self):
        status = " (Favoritos)" if self.is_favorite else ""
        return f"{self.name} - {self.phone}{status}"


class ContactBook:
    """Classe para gerenciar contatos."""
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        """Add um contato novo."""
        self.contacts.append(Contact(name, phone))
        print(f"Contato '{name}' adicionado.")

    def list_contacts(self):
        """Lista de contatos."""
        if not self.contacts:
            print("Sem contatos.")
        else:
            print("\nContatos:")
            for idx, contact in enumerate(self.contacts, 1):
                print(f"{idx}. {contact}")

    def edit_contact(self, index, new_name=None, new_phone=None):
        """Editar um contato existente."""
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            if new_name:
                contact.name = new_name
            if new_phone:
                contact.phone = new_phone
            print(f"atualizar contato: {contact}")
        else:
            print("Contato não encontrado.")

    def delete_contact(self, index):
        """Deletar contato."""
        if 0 <= index < len(self.contacts):
            removed_contact = self.contacts.pop(index)
            print(f"Contato '{removed_contact.name}' deletado.")
        else:
            print("Contato não encontrado.")

    def mark_favorite(self, index):
        """Marcado como favorito."""
        if 0 <= index < len(self.contacts):
            self.contacts[index].is_favorite = True
            print(f"Contato '{self.contacts[index].name}' marcado como favorito.")
        else:
            print("Contato não encontrado.")


def clear_terminal():
    """Limpar terminal para menu melhor."""
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """loop principal."""
    contact_book = ContactBook()

    while True:
        clear_terminal()  # Clear the terminal before showing the menu
        print("--- Agenda ---")
        print("1. Adicionar contato")
        print("2. Lista de contatos")
        print("3. Editar contato")
        print("4. Deletar contato")
        print("5. Marcado como favorito")
        print("6. Sair")

        choice = input("escolha uma opção ")

        if choice == "1":
            name = input("insira o nome: ")
            phone = input("insira o número do contato: ")
            contact_book.add_contact(name, phone)

        elif choice == "2":
            contact_book.list_contacts()
            input("\nPressione Enter para voltar ao menu.")

        elif choice == "3":
            contact_book.list_contacts()
            try:
                index = int(input("Insira nome do contato: ")) - 1
                new_name = input("Insira o novo nome (Ou pressione Enter para pular): ") or None
                new_phone = input("Insira novo número (ou pressione Enter paar pular): ") or None
                contact_book.edit_contact(index, new_name, new_phone)
            except ValueError:
                print("Opção inválida.")
            input("\nPressione Enter para voltar ao menu.")

        elif choice == "4":
            contact_book.list_contacts()
            try:
                index = int(input("Insira nome do contato para deletar: ")) - 1
                contact_book.delete_contact(index)
            except ValueError:
                print("Opção inválida.")
            input("\nPressione Enter para voltar ao menu.")

        elif choice == "5":
            contact_book.list_contacts()
            try:
                index = int(input("Insira nome do contato para favoritar: ")) - 1
                contact_book.mark_favorite(index)
            except ValueError:
                print("Opção inválida.")
            input("\nPressione Enter para voltar ao menu.")

        elif choice == "6":
            print("Saindo da agenda, até mais!")
            break

        else:
            print("Opção inválida. Verifique as opções existentes.")
            input("\nPressione Enter para voltar ao menu.")


if __name__ == "__main__":
    main()
