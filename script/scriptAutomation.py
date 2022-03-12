import webbrowser
from attr import asdict

from requests_toolbelt import SourceAddressAdapter

#Substituir pelo nome do seu browser ou utilizar = 'windows-defauilt' para abrir com seu navegador padrão.
c = webbrowser.get('firefox') 



#Tela de menu de opções
print("::::::::::Navegador Automático v.0::::::::::\n\n")
print("Olá Felipe!, selecione qual das telas você deseja abrir:\n\n"
    "1 - Principais Páginas     | Gmail | Linkedin | Tryhackme | Hackthebox | Udemy | Youtube\n\n"
    "2 - Youtube Favoritos      | Canais favoritos do Youtube\n\n"
    "3 - Kali Linux             | Kali Doc | Kali Tools\n\n"
    "4 - Nova página            | Nova guia em branco\n\n"
    "5 - Todas as páginas       | Abertura de todas as páginas acima")

print("::::::::::::::::::::::::::::::::::::::::::::::::")

resposta=input("Digite o número desejado para executar o script ou 'sair' para SAIR do programa: ").upper()

while resposta != "SAIR":

    if resposta=="1":

        c.open_new('www.linkedin.com.br') 
        c.open_new_tab("www.tryhackme.com")
        c.open_new_tab('www.gmail.com')
        c.open_new_tab('https://eylearning.udemy.com/organization/home/')

    elif resposta=="2":

        c.open_new("https://www.youtube.com/c/DavidBombal")
        c.open_new_tab("https://www.youtube.com/c/KalleHallden")
        c.open_new_tab("https://www.youtube.com/c/FabioAkita1990")  
        c.open_new_tab("https://www.youtube.com/c/FilipeDeschamps")  
        c.open_new_tab("https://www.youtube.com/c/LucasMontano")
        c.open_new_tab("https://www.youtube.com/c/GabrielPato")
        c.open_new_tab("https://www.youtube.com/c/DiolinuxBr")

    elif resposta=="3":

        c.open_new("https://www.kali.org/docs/")
        c.open_new_tab("https://www.kali.org/tools/")
        c.open_new_tab("https://www.kali.org/")

    elif resposta=="4":

        c.open_new("https://www.google.com.br")

    elif resposta=="5":

        c.open_new("www.linkedin.com.br")
        c.open_new_tab("www.tryhackme.com")
        c.open_new_tab("www.gmail.com")
        c.open_new_tab("https://eylearning.udemy.com/organization/home/")
        c.open_new("https://www.youtube.com/c/DavidBombal")
        c.open_new_tab("https://www.youtube.com/c/KalleHallden")
        c.open_new_tab("https://www.youtube.com/c/FabioAkita1990")
        c.open_new_tab("https://www.youtube.com/c/FilipeDeschamps")
        c.open_new_tab("https://www.youtube.com/c/LucasMontano")
        c.open_new_tab("https://www.youtube.com/c/GabrielPato")
        c.open_new_tab("https://www.youtube.com/c/DiolinuxBr")
        c.open_new("https://www.kali.org/docs/")
        c.open_new_tab("https://www.kali.org/tools/")
        c.open_new_tab("https://www.kali.org/")
        c.open_new("https://www.google.com.br")

    elif resposta=="SAIR":

        print("Saindo do programa....")

    else:

        print("Você não digitou um número correto, por favor digite novamente ou 'sair' para SAIR do programa.")
    print("Comando executado com Sucesso!")
    print("\n\n")
    resposta=input("Digite o número desejado para executar o script ou 'sair' para SAIR do programa: ").upper()



