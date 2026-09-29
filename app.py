import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Consulta de Ocorrências",
    page_icon="🌧️"
)

st.title("🌧️ Consulta de Ocorrências")
st.write("Informe o local e o período para gerar sua consulta.")

# Lista de estados
estados = [
    "Acre",
    "Alagoas",
    "Amapá",
    "Amazonas",
    "Bahia",
    "Ceará",
    "Distrito Federal",
    "Espírito Santo",
    "Goiás",
    "Maranhão",
    "Mato Grosso",
    "Mato Grosso do Sul",
    "Minas Gerais",
    "Pará",
    "Paraíba",
    "Paraná",
    "Pernambuco",
    "Piauí",
    "Rio de Janeiro",
    "Rio Grande do Norte",
    "Rio Grande do Sul",
    "Rondônia",
    "Roraima",
    "Santa Catarina",
    "São Paulo",
    "Sergipe",
    "Tocantins"
]

# Estado
estado = st.selectbox(
    "Estado",
    estados
)

# Cidade
cidade = st.text_input(
    "Cidade",
    placeholder="Ex.: São José dos Campos"
)

# Datas
col1, col2 = st.columns(2)

with col1:
    data_inicial = st.date_input("Data inicial")

with col2:
    data_final = st.date_input("Data final")


if st.button("🔎 Gerar consulta"):

    if not cidade:
        st.warning("Informe uma cidade.")

    elif data_inicial > data_final:
        st.warning(
            "A data inicial não pode ser maior que a data final."
        )

    else:

        prompt = (
            f"Busque ocorrências relacionadas a alagamentos, "
            f"enxurradas, deslizamentos de terra para a cidade "
            f"{cidade}, no estado {estado} do Brasil entre os dias "
            f"{data_inicial.strftime('%d/%m/%Y')} e "
            f"{data_final.strftime('%d/%m/%Y')}."
        )

        st.session_state["prompt"] = prompt


# Mostrar resultado somente depois de gerar
if "prompt" in st.session_state:

    prompt = st.session_state["prompt"]

    st.subheader("Prompt gerado")

    st.text_area(
        "Consulta",
        value=prompt,
        height=130
    )

    # Botões
    col1, col2 = st.columns(2)

    # Botão copiar
    with col1:

        components.html(
            f"""
            <button
                onclick="copiarPrompt()"
                style="
                    width:100%;
                    padding:10px;
                    border:none;
                    border-radius:8px;
                    background:#f0f2f6;
                    cursor:pointer;
                    font-size:16px;
                "
            >
                📋 Copiar prompt
            </button>

            <script>
            function copiarPrompt() {{

                const prompt = {prompt!r};

                navigator.clipboard.writeText(prompt)
                    .then(() => {{
                        alert("Prompt copiado!");
                    }})
                    .catch(() => {{
                        alert("Não foi possível copiar automaticamente.");
                    }});
            }}
            </script>
            """,
            height=55
        )

    # Botão copiar + abrir ChatGPT
    with col2:

        components.html(
            f"""
            <button
                onclick="copiarEAbrir()"
                style="
                    width:100%;
                    padding:10px;
                    border:none;
                    border-radius:8px;
                    background:#10a37f;
                    color:white;
                    cursor:pointer;
                    font-size:16px;
                "
            >
                🤖 Copiar e abrir ChatGPT
            </button>

            <script>
            function copiarEAbrir() {{

                const prompt = {prompt!r};

                navigator.clipboard.writeText(prompt)
                    .then(() => {{
                        window.open(
                            "https://chatgpt.com/",
                            "_blank"
                        );
                    }})
                    .catch(() => {{
                        alert("Não foi possível copiar automaticamente.");
                    }});
            }}
            </script>
            """,
            height=55
        )

    st.info(
        "Ao abrir o ChatGPT, o prompt estará copiado. "
        "Basta colar no campo de mensagem e enviar."
    )