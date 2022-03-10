## Automatização do seu navegador


### Libraries necessárias do Python:

- webbrowser

- Utilização no Python : import webbrowser.

## Instalação Python v3.10

#### Usuários Windows

- Faça o download da última versão do python pelo link : https://www.python.org/downloads/
- Após o python instalado, seu sistema vai estar apto a executar o script em .py

#### Usuários Linux

- Basta executar o comnado em seu terminal linux : sudo apt-get install python3
- YUM se necessário, execute o comando : yum -y install python3-pip


#### Uso do Script e edição

- Dentro do código você verá os campos para editar e personalizar o script de acordo com cada url que queira abrir automaticamente.
- Você pode editar as URL's utilizando qualquer editor de sua preferência.

- Após editar as urls basta executar o script e aproveitar a sua automação =)

#### Configuração do Browser

Dentro de  " c = webbrowser.get('firefox') ", no lugar de 'firefox', substitua pelo seu browser ou pelo navegador padrão do seu sistema operacional, utilizando = 'windows-default'

## Tabela de sistemas operacionais:


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
