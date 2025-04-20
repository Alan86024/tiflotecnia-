# Documentação das Vozes Tiflotecnia para NVDA

## Boas-vindas

Obrigado por escolher as Vozes Tiflotecnia para as suas necessidades de conversão de texto em voz. Está prestes a experimentar o melhor em síntese de fala de alta qualidade, multilingual, responsiva e natural. Esta documentação vai familiarizá-lo com todas as funcionalidades que este extra oferece.

## Requisitos do Sistema

Este extra funciona com as seguintes configurações:
* Windows 10 ou superior.
* Memória RAM e espaço em disco suficientes para todas as vozes que deseja instalar. A quantidade de espaço necessário depende das vozes em questão, mas aqui estão alguns pontos gerais a considerar:
	* As variantes de baixa qualidade ocupam apenas alguns megabytes e, portanto, requerem menos RAM.
	* Quanto maior a qualidade, maior a necessidade de espaço e RAM. Embora o tamanho real dependa da voz utilizada, uma única voz na mais alta qualidade geralmente não excede 300MB.
* NVDA 2023.1.0 ou superior.

## Instalação e Licenciamento

### Instalar o extra

Para instalar o extra, basta clicar no ficheiro e permitir que o NVDA o instale. O extra será apresentado assim que o NVDA reiniciar.

### Licenciamento

Na primeira vez que o extra for iniciado, será solicitado que introduza o seu código de activação. Se não tiver um, pode seleccionar  a opção "Quero experimentar o produto por 7 dias", pressionando seta para baixo até ser anunciado. Neste momento, pressionar a tecla tab levará ao botão "Experimentar o produto por 7 dias", que gerará uma licença de teste após activação. Esta licença permitirá aceder a todas as funcionalidades do extra durante 7 dias a partir da data de activação.

#### Activação via Internet

A ativação via internet é a forma mais rápida de licenciar o produto e é recomendada para a maioria dos utilizadores. Para ativar via internet:
1. Quando o écran de registo aparecer, pressione enter.
1. Cole o código de activação que recebeu aquando da compra e, em seguida, pressione enter.
1. Se  o código de activação for válido, será informado de que a ativação foi bem-sucedida.

#### Ativação sem ligação à Internet

Se estiver numa máquina com firewall ou sem acesso regular à internet, poderá activar o produto através de um método offline. Para ativar sem ligação à internet, siga o procedimento abaixo:
1. Quando o écran de registo aparecer, use a seta para baixo até chegar à opção "Activação offline (para locais sem conexão à internet)", e pressione enter.
1. Cole o código de activação que recebeu aquando da compra, e depois pressione enter.
1. Será apresentado um diálogo de guardar ficheiros, onde poderá guardar um ficheiro de identificação da máquina. Escolha o directório onde deseja guardar o ficheiro e guarde-o.
1. Aceda ao [portal de ativação offline](https://activate.accessmind.net) para gerar um ficheiro de chave de activação offline. Para isso, carregue o ficheiro de identificação da máquina que recebeu do extra.
1. Uma vez que o ficheiro de chave tenha sido descarregado, volte ao écran de Activação Offline e ative o botão "Ativar licença".
1. Localize e selecione o ficheiro da chave de licença. Se o ficheiro de chave for válido, será informado de que a activação do produto foi bem-sucedida.

### Instalar Vozes

Antes de poder utilizar o sintetizador, precisará de instalar pelo menos uma voz. As vozes podem ser instaladas através do Gestor de vozes incorporado. Ser-lhe-á perguntado se deseja executar o Gestor de vozes aquando da activação inicial da licença, caso não existam vozes presentes. Também pode aceder a este gestor a partir do novo submenu "Vozes Tiflotecnia para o NVDA" no menu do NVDA (*Insert ou Capslock+N*). Uma vez neste menu, localize e ative a opção "Getor de vozes...".

Dentro do gestor de vozes, será primeiramente apresentado um menu Idiomas. Seleccione o idioma para o qual deseja instalar vozes, utilizando as setas para cima e para baixo para percorrer a lista, ou pressionando a primeira letra do idioma que está a procurar. Pressionando tab, encontrará o menu Qualidades. Aqui, pode selecionar a qualidade da voz para obter uma listagem de vozes. Por predefinição, todas as qualidades estão disponíveis. As qualidades disponíveis são as seguintes:
* Mais baixa: pequeno tamanho, ideal para instalações com pouca RAM.
    * Quem estiver familiarizado com distribuições anteriores do Vocalizer pode conhecer estas como variantes compactas.
* Intermediária: Opção intermédia que equilibra boa qualidade com um tamanho de memória relativamente pequeno.
    * Quem estiver familiarizado com distribuições anteriores do Vocalizer pode conhecer estas como variantes standard (Automotive) ou plus (Expressive).
* Melhorada: Para a maioria das vozes, esta opção apresenta a mais alta qualidade, mas também exige mais memória.
    * Quem estiver familiarizado com distribuições anteriores do Vocalizer pode conhecer estas como variantes premium ou premium high.

Se não quiser filtrar pela qualidade da voz, pode simplesmente passar à frente deste controlo. Em qualquer caso, será apresentado com uma lista de vozes. Estes itens são caixas de verificação, permitindo que selecione várias vozes ao mesmo tempo. Uma vez que tenha selecionado as vozes que deseja instalar, pressione tab até ao botão Instalar e active-o. O botão indicará o número de vozes que estão seleccionadas para instalação. Após activar o botão, os downloads começarão. Cada voz será instalada uma de cada vez, mas não é necessária mais nenhuma interação do utilizador. Assim, pode deixar o instalador a funcionar sem supervisão. Quando a instalação das vozes estiver concluída, poderá selecionar a nova opção "Vozes Tiflotecnia para o NVDA" no diálogo do sintetizador.

#### Nota

Embora seja possível descarregar vozes enquanto o sintetizador está a funcionar, a fala será interrompida por um breve momento após a instalação de cada voz. Isso pode dificultar a leitura contínua, caso esteja a instalar várias vozes ao mesmo tempo. Portanto, recomendamos que mude de sintetizador durante uma instalação em lote. O Gestor de vozes continuará a notificá-lo sobre o estado das instalações.

## Mudança Automática de Idioma para Texto em Árabe

Se tiver pelo menos uma voz em Árabe, Hebraico ou Cirílico instalada, poderá aproveitar a nossa capacidade exclusiva de mudança automática de idioma para alternar entre textos em caracteres latinos e não-latinos. A nova secção no painel de configurações do NVDA, "Vozes Tiflotecnia para o NVDA", permitirá que selecione uma voz a ser utilizada para textos latinos, assim como uma voz para textos não-latinos. Além disso, a nova opção "Mudar automaticamente de idioma com base nos caracteres Unicode" nas Definições de Voz do NVDA permitirá activar ou desactivar esta funcionalidade.

