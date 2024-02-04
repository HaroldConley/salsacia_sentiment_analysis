import os
import streamlit as st

from openai import OpenAI


def sentiment_analysis(api_key, comentario):
    # Inicializando el cliente de OpenAI
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        temperature=0,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """
            Te voy a entregar un comentario y necesito que me indiques si es un comentario "A favor" o "En contra".
            Dame la respuesta "Comentario a favor" o "Comentario en contra", sin más texto.
            """},
            {"role": "user", "content": f"""{comentario}"""}
        ]
    )

    return response.choices[0].message.content


# Título WebApp
st.title('Analizador de Sentimientos')

# Subtítulo
st.subheader('Escribe que opinas sobre el candidato AAA de Salsacia:')

# Ingreso del comentario
comentario = st.text_area("Escribe tu comentario aquí:")

# Generación de la respuesta.
# Agregue un botón "Analizar" a la interfaz de usuario
if st.button('Analizar'):
    with st.spinner('Analizando tu comentario...'):
        # Procesamiento
        api_key = os.environ['OPENAI_API_KEY']
        response = sentiment_analysis(api_key, comentario)

        # Muestra de la respuesta
        st.markdown(response, unsafe_allow_html=True)
