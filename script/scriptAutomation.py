import webbrowser


c = webbrowser.get('firefox') #Substituir pelo nome do seu browser ou utilizar = 'windows-defauilt' para abrir com seu navegador padrão.

#URL para iniciar a abertura das páginas = 'open_new'
#URLs podem ser substituidas para de sua preferência.

c.open_new('www.linkedin.com.br') 
c.open_new_tab("www.tryhackme.com")
c.open_new_tab('www.gmail.com')
c.open_new_tab('https://eylearning.udemy.com/organization/home/')


#Se necessário abrir outra janela com abas embutidas, somente executar os proximos comandos, usando o 'c.open_new' para abrir outra janela do navegador.

#c.open_new('www.yahoo.com.br')
#c.open_new_tab('www.google.com.br')


#fim 

