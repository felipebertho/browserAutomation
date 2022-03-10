##Script para abertura de abas automáticas no browser.


###Libraries necessárias do Python:

- webbrowser

- Utiulização : import webbrowser.


#### Uso do Script

Dentro do código você verá os campos para editar e personalizar o script de acordo com cada url que queira abrir automaticamente.

Após editar as urls basta executar o script e aproveitar a sua automação =)

####Dicas

Dentro de  " c = webbrowser.get('firefox') ", no lugar de 'firefox', substitua pelo seu browser ou pelo navegador padrão do seu sistema operacional, utilizando = 'windows-default'

###Tabela de sistemas operacionais:


Type Name
	

Class Name
	

Notes

'mozilla'
	

Mozilla('mozilla')
	

'firefox'
	

Mozilla('mozilla')
	

'netscape'
	

Mozilla('netscape')
	

'galeon'
	

Galeon('galeon')
	

'epiphany'
	

Galeon('epiphany')
	

'skipstone'
	

BackgroundBrowser('skipstone')
	

'kfmclient'
	

Konqueror()
	

(1)

'konqueror'
	

Konqueror()
	

(1)

'kfm'
	

Konqueror()
	

(1)

'mosaic'
	

BackgroundBrowser('mosaic')
	

'opera'
	

Opera()
	

'grail'
	

Grail()
	

'links'
	

GenericBrowser('links')
	

'elinks'
	

Elinks('elinks')
	

'lynx'
	

GenericBrowser('lynx')
	

'w3m'
	

GenericBrowser('w3m')
	

'windows-default'
	

WindowsDefault
	

(2)

'macosx'
	

MacOSXOSAScript('default')
	

(3)

'safari'
	

MacOSXOSAScript('safari')
	

(3)

'google-chrome'
	

Chrome('google-chrome')
	

'chrome'
	

Chrome('chrome')
	

'chromium'
	

Chromium('chromium')
	

'chromium-browser'
	

Chromium('chromium-browser')
