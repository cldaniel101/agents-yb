# Agents-YB

Este repositório contém uma coleção de agentes de conversação desenvolvidos com o Google ADK (Agent Development Kit). O objetivo principal deste projeto é o aprendizado e a exploração das capacidades do Google ADK, com todos os agentes sendo baseados nas aulas e exemplos do canal [Sandeco no YouTube](https://www.youtube.com/playlist?list=PLbmt8d_ueDMWHIv-HgdM532MLFSju6W2D).

## Agentes

Aqui está uma lista dos agentes disponíveis neste repositório:

  * **c3po**: Um agente que simula o droide C-3PO da saga Star Wars, sendo formal, um pouco dramático e medroso.
  * **deepseek**: Um agente que atua como um jogador de futebol do Vasco da Gama, que é um eterno reserva, mas se considera o melhor do time. Ele é irônico, sarcástico e adora contar vantagem sobre suas habilidades em campo (mesmo nunca tendo jogado).
  * **my\_tool\_agent**: Um agente utilitário que pode fornecer a hora atual e o dia da semana.
  * **search**: Um agente simples que utiliza a ferramenta de busca do Google para encontrar informações.

## Como Rodar

Para executar esses agentes, você precisará ter o Google ADK instalado e configurado em sua máquina.

### Pré-requisitos

  * Python 3.12
  * Google ADK

### Instalação

1.  **Clone o repositório:**

    ```bash
    git clone [<URL_DO_REPOSITORIO>](https://github.com/cldaniel101/agents-yb.git)
    cd agents-yb
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Para Linux/macOS
    .venv\Scripts\activate  # Para Windows
    ```

3.  **Configure as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API do Google:

    ```
    GOOGLE_API_KEY="SUA_CHAVE_DE_API_AQUI"
    ```

### Executando com a Interface Web

1.  **Inicie o servidor web do ADK:** No diretório raiz do projeto, execute o seguinte comando:

    ```bash
    adk web
    ```

2.  **Acesse a interface:** Abra seu navegador e acesse o endereço fornecido no terminal (geralmente `http://127.0.0.1:8000`).

3.  **Interaja com os agentes:** Na interface web, você verá uma lista dos agentes disponíveis. Selecione o agente com o qual deseja conversar e comece a interagir\!
