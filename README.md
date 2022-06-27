# Diario de Bordo - LABirintos

<h2>Equipe</h2>

- Anderson Poiani Lopes Mendes (LME)
- Andrea Pinheiro Felix (CNPG)
- Diogo Cesar Borges Silva (LME)
- Fabrício Gonçalves Torres (LME)
- Felipe Santiago Apolinario (LME)
- Flavio Sergio Jorge de Freitas (ACC)

<h2>Problema</h2>

Os visitantes do IPT (transportadoras, clientes, entre outros) têm dificuldades em acessar os prédios do Instituto.

Causas:

- Sinalização física ainda é insuficiente;
- Os visitantes têm dificuldade em entender o mapa físico (em papel) da portaria;
- Os funcionários da portaria não conhecem todo o IPT para auxiliar os visitantes adequadamente;
- O fluxo alto de pessoas na portaria não permite maior atenção para o auxílio ao cliente no que diz respeito à localização dos prédios.

<h2>Diagnóstico</h2>

A equipe decidiu visitar a portaria e conversar com os funcionários, inclusive a Cláudia dos Santos, que, atualmente, é a coordenadora administrativa da área.

A conversa com a Cláudia e com o pessoal da portaria demonstrou que o deslocamento dos visitantes dentro do IPT é um problema, e todos corroboraram com o fato de que há necessidade de uma solução eficaz para tal.

À partir da visita na portaria, foi possível constatar pessoalmente o problema. Segue relato de Fabrício:

No período de 15 minutos que ficamos na portaria, conseguimos evidenciar e diagnosticar o problema, já que um dos casos que vimos, o visitante chegou ao IPT e, após a liberação de acesso, o funcionário perguntou a ele se conhecia o laboratório (Prédio 36). O cliente disse que não e, mesmo após explicação verbal e com o mapa, pelo funicionário, o cliente não compreendeu. O funcionário, percebendo isso, pediu a ele que conversasse com o guarda da outra portaria, que fica perto do prédio 56. Ficou claro que qualquer outro prédio localizado numa área mais escondida, faria com que o visitante ficasse bastante perdido no Instituto.

<h2>Solução</h2>

Disponibilizar um site de busca responsivo, ou seja, que funcione em um desktop ou em um celular, que pudesse apresentar o link para o **Google Maps**, com o trajeto entre a portaria do IPT e o prédio de destino. O link seria disponibilizado via um QR_Code, gerado pelo site.

O site deveria buscar o prédio a partir do:
- número do prédio;
- nome do laboratório;
- sigla do laboratório;
- ramal;
- nome do contato.

Foi realizado brainstorm para identificar o melhor meio de apresentar o link do trajeto ao visitante.

<img src="https://github.com/Github2diogo/labirintus/blob/main/ImagensReadme/Brainstorm.png" alt="Brainstorm" width="800"/>

<h2>Desenvolvimento do protótipo</h2>

O protótipo foi desenvolvido, e pode ser acessado via link a seguir, ou QR-Code abaixo:

Todo o código-fonte está disponível neste projeto do Github.

<img src="https://github.com/Github2diogo/labirintus/blob/main/ImagensReadme/QR_Code.png" alt="QR-Code" width="400"/>

[Site do LABrintos](https://tinyurl.com/iptTD2022)

<h2>Validação</h2>

No dia 24.06.2022, Apolinário e Fabrício foram para a portaria realizar o teste do aplicativo.
Fabrício ficou dentro da sala de recepção, enquanto o Apolinário ficou na cancela, junto com os guardas.
Fabrício instruiu as meninas da recepção e o Pascoal, apresentando o site do Labirintos, que teve um bom feedback de todos.
A Cristiane do CAD também recebeu o link do aplicativo.

No decorrer do teste, Fabrício identificou que havia muita gente que não conhecia o IPT ou o prédio de destino. Nestes casos, que foram 6, ele interviu no momento que o visitante era liberado. O visitante foi questionado sobre o uso do Google Maps e da leitura do QR-Code. Todos eles não tiveram problemas em obter a rota, e saíram da recepção com o trajeto do prédio nos seus respectivos celulares. Fabrício obteve feedback de dois visitantes, que retornaram para a recepção. Ambos informaram que não tiveram problemas ao achar o prédio através do aplicativo.

Com o Apolinário, ele relatou que houve dois problemas: o primeiro, foi um que não coiseguiu ler o QR-Code devido ao celular do visitante ser antigo. O outro foi devido ao prédio de destino não estar cadastrado no aplicativo, sendo que este, foi imediatamente resolvido.

Ficou claro para a equipe do Labirintos que o site no celular do funcionário ou em um tablet que ele tenha acesso é a melhor solução. Nos momentos de pico, eles têm que agir rapidamente para liberar o acesso. Um totem físico, por exemplo, não parece uma boa solução, já que há risco do cliente ficar mais perdido ainda, atrapalhando o fluxo da portaria.

<img src="https://github.com/Github2diogo/labirintus/blob/main/ImagensReadme/Visita_1.jpg" alt="Validação do app_1" width="200"/>

<img src="https://github.com/Github2diogo/labirintus/blob/main/ImagensReadme/Visita_2.jpg" alt="Validação do app_1" width="200"/>

<img src="https://github.com/Github2diogo/labirintus/blob/main/ImagensReadme/Visita_3.jpg" alt="Validação do app_1" width="200"/>

<img src="https://github.com/Github2diogo/labirintus/blob/main/ImagensReadme/Visita_4.jpg" alt="Validação do app_1" width="200"/>

<h2>Conclusão</h2>

Concluímos que a nossa solução tem potencial e é muito fácil de ser implementada. Mesmo as meninas da recepção estarem no IPT há pouco tempo, ainda assim conseguiram usar o aplicativo sem problemas. Entretanto, ainda pode haver uma pequena barreira, já que o pessoal (principalmente os mais antigos) está acostumado em tentar explicar o destino verbalmente. E, por outro lado, o visitante não explicita se compreendeu ou não o que foi dito. Tanto do lado do funcionário quanto do visitante, há uma questão cultural e automática de como procedemos para se localizar e seguir a um destino.

Além do ganho com a experiência do cliente, percebemos também que o cadastro dos laboratórios no Google Maps têm potencial adicional com relação à divulgação dos serviços prestados pelo IPT.

Temos como exemplo o LME, que possui cadastro no Google Maps, e que mantém um pequeno gerenciamento da página na Web. Segue alguns dados:
- 50 mil visualizações;
- 5,6 mil pesquisas;
- 15 avaliações (todas com 5 estrelas).

<img src="https://github.com/Github2diogo/labirintus/blob/main/ImagensReadme/Google_LME_1.JPG" alt="Insights Google_1" width="800"/>

<img src="https://github.com/Github2diogo/labirintus/blob/main/ImagensReadme/Google_LME_1.JPG" alt="Insights Google_2" width="800"/>

<img src="https://github.com/Github2diogo/labirintus/blob/main/ImagensReadme/Google_LME_1.JPG" alt="Insights Google_3" width="800"/>
