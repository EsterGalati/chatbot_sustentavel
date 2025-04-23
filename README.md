### 📄 `README.md`

```markdown
# 🌱 EcoBot – Chatbot Educativo de Sustentabilidade

Bem-vindo ao **EcoBot**, um chatbot inteligente que responde perguntas sobre **meio ambiente**, **sustentabilidade**, **consumo consciente** e muito mais!  
Feito com ❤️ em Python, o EcoBot é ideal para projetos educativos voltados a crianças, adolescentes e curiosos de todas as idades.



## 💡 O que é o EcoBot?

O **EcoBot** é um chatbot que:
- Responde perguntas sobre sustentabilidade de forma clara e amigável.
- Prioriza respostas de uma **base local** (`perguntas_respostas.json`).
- Usa **Inteligência Artificial com GPT-4**, caso a pergunta não esteja na base.
- É simples de rodar e pode ser usado até em sala de aula!


## 🧠 Tecnologias utilizadas

- [Python 3.11+](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – para a interface web
- [OpenAI GPT-4 API](https://platform.openai.com/)
- `.env` para segurança da chave da API
- JSON como base de conhecimento local

## 📦 Instalação

```bash
git clone https://github.com/EsterGalati/chatbot_sustentavel.git
cd chatbot_sustentavel
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```



## 🔐 Configuração

Crie um arquivo chamado `.env` na raiz do projeto com sua chave da OpenAI:

```env
OPENAI_API_KEY=sua_chave_aqui
```

> **⚠️ Sua chave está segura!** O arquivo `.env` está no `.gitignore` e não vai pro GitHub 😉


## ▶️ Como rodar o EcoBot

```bash
streamlit run app.py
```

Abra seu navegador e acesse o endereço local que o Streamlit mostrar (ex: http://localhost:8501)


## 🎯 Exemplos de perguntas

- O que é sustentabilidade?
- Como economizar água?
- Quais são os 3 R's?
- O que é compostagem?
- Por que reciclar é importante?


## 📚 Aplicações educativas

O EcoBot é uma ferramenta excelente para:

- 🌿 **Escolas** que querem ensinar educação ambiental de forma interativa
- 🧒 **Crianças e adolescentes** que aprendem melhor conversando
- 👨‍🏫 **Professores** que desejam incluir tecnologia nas aulas
- 🧪 **Feiras de ciência e projetos escolares**


## 🚀 Futuras melhorias

- Suporte a imagens com IA generativa
- Base local com mais perguntas e categorias
- Interface personalizável com temas visuais
- Exportar histórico de perguntas/respostas em PDF

## 🤝 Contribua!

Quer sugerir melhorias ou novas perguntas para a base?  
Sinta-se à vontade para enviar um **pull request** ou abrir uma **issue** ✨


## 🧑‍💻 Autor(a)

Desenvolvido por **Ester Luiza**  
Estudante de Ciência da Computação – UCB  
🔗 [LinkedIn](https://www.linkedin.com/in/estergalati/) 


## 📜 Licença

Este projeto é livre para fins educacionais e não possui fins comerciais.  
Sinta-se à vontade para adaptar e compartilhar com sua escola, ONG ou comunidade! 💚
