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
            I am going to give you a comment and I need you to indicate whether it is a ‘For’ or ‘Against’ comment.
            Give me the answer ‘Comment for’ or ‘Comment against’, without further text.
            """},
            {"role": "user", "content": f"""{comentario}"""}
        ]
    )

    return response.choices[0].message.content


def comentario_generator(api_key, comentario_base):
    # Inicializando el cliente de OpenAI
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        temperature=1,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """
            I am going to give you a commentary on a candidate.
            I need you to generate a new short comment, in popular language, supporting the submitted comment.
            Deliver the result directly, without additional text. Always add at the end of the comment ‘#Salsacia2024’.
            """},
            {"role": "user", "content": f"""Comentario: {comentario_base}"""}
        ]
    )

    return response.choices[0].message.content


# Título WebApp
st.title('Sentiment Analyser')

# Subtítulo
st.subheader("Write what you think about Salsacia's AAA candidate:")

# Ingreso del comentario
comentario = st.text_area("Write your comment here:")

# Generación de la respuesta.
# Agregue un botón "Analizar" a la interfaz de usuario
if st.button('Analyse'):
    with st.spinner('Analysing your comment...'):
        # Procesamiento
        api_key = os.environ['OPENAI_API_KEY']

        tendencia = sentiment_analysis(api_key, comentario)

        # Muestra el resultado del análisis
        st.markdown(tendencia, unsafe_allow_html=True)

        # Genera un nuevo comentario basado en el ingresado
        new_comentario = comentario_generator(api_key, comentario)
        st.markdown(new_comentario, unsafe_allow_html=True)

