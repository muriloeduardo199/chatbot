# chatbot
Automatização de Envio de Mensagens no WhatsApp usando Python
Este é um projeto de automação desenvolvido em Python que permite enviar mensagens para contatos do WhatsApp utilizando o WhatsApp Web.

Requisitos
Certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

Python 3.x
Bibliotecas Python: pyautogui, webbrowser, time, pandas
Como usar
Clone o repositório para o seu ambiente local:

bash
Copy code
git clone https://github.com/seu-usuario/nome-do-repositorio.git
Certifique-se de ter um arquivo CSV válido contendo a lista de contatos e mensagens a serem enviadas. O arquivo CSV deve ter duas colunas com os cabeçalhos "Celular" e "texto", representando o número do celular e a mensagem, respectivamente.

Abra o arquivo automatizar_whatsapp.py em um editor de texto e atualize o caminho do arquivo CSV na linha correspondente:

python
Copy code
data = pd.read_csv("caminho/para/o/arquivo.csv")
Execute o script Python:

Copy code
python automatizar_whatsapp.py
O script irá percorrer a lista de contatos e enviar as mensagens correspondentes usando o WhatsApp Web.

Notas importantes
Este script foi desenvolvido apenas para fins educacionais e de demonstração. Certifique-se de usar essa automação com responsabilidade e respeitar as diretrizes e políticas do WhatsApp em relação ao envio de mensagens. Evite enviar mensagens indesejadas ou spam para os destinatários.

Seja cauteloso ao fornecer informações pessoais ou confidenciais no código fonte ou nos arquivos CSV.

Certifique-se de atualizar o caminho do arquivo CSV de acordo com a localização correta do arquivo em seu sistema.

Contribuição
Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões para melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.