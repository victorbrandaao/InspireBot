# 📢 InspireBot: Bot Motivacional para Bluesky

O InspireBot é uma aplicação web baseada em Flask que publica frases motivacionais e interage com os usuários na plataforma Bluesky. Ele responde a menções, fornece citações motivacionais diárias e possui uma API interativa.

## 🚀 Funcionalidades

- **Motivação Diária**: Publica automaticamente frases motivacionais sob demanda.
- **Integração com Bluesky**: Monitora menções no Bluesky e responde com frases quando mencionado com comandos específicos (por exemplo, `#quote`).
- **API Interativa**: Permite adicionar novas frases motivacionais através de uma API.


### Instruções de Uso

- **Clone o repositório** para o seu ambiente local.
- **Configure** as variáveis de ambiente necessárias.
- **Execute** a aplicação localmente ou em um servidor de produção.
- **Atualize** as frases motivacionais conforme necessário.
- **Contribua** para o projeto se desejar.

🛠️ **Configuração do Scheduler**

A aplicação usa o APScheduler para verificar menções a cada minuto. Certifique-se de que o scheduler está configurado corretamente para o ambiente de produção.

**🔄 Atualizando Frases**

As frases motivacionais são armazenadas em um arquivo quotes.txt. Para adicionar novas frases, edite esse arquivo e adicione uma frase por linha.

**📄 Documentação da API**

GET /
Retorna uma frase motivacional aleatória.
POST /add_quote
Permite adicionar uma nova frase motivacional. (Implementação ainda não disponível)
🤝
**Contribuindo**

Se você quiser contribuir para o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request. Certifique-se de seguir as boas práticas de codificação e teste suas alterações antes de enviá-las.

**📜 Licença**

Este projeto está licenciado sob a Licença MIT.

**Contato**

Victor Brandão - @victorbrandaao
E-mail: victorbrandaotech@gmail.com



   
