import webbrowser


c = webbrowser.get('firefox')

#URL para iniciar a abertura das páginas

c.open_new('www.google.com.br')
c.open_new_tab("www.linkedin.com.br")

#teste se abrirá outra aba 

c.open_new('www.yahoo.com.br')
c.open_new_tab('www.google.com.br')

#teste incremento de tabs 
c.open_new('www.youtube.com')
c.open_new_tab('www.globo.com')

#abertuira de nova janela 



#fim 

