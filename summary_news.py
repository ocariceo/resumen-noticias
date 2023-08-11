import streamlit as st
st.set_page_config(
        page_title="Resume Noticias",
        page_icon=":newspaper:",
        #layout="wide",
    )
import newspaper
import nltk
nltk.download('punkt')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
"""

#st.markdown('<style> .css-1v0mbdj {margin:0 auto; width:100%; </style>', hide_st_style, unsafe_allow_html=True)

st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Resumen de noticias')


st.subheader('Esta aplicación permite resumir el contenido de una noticia o artículo.')

url = st.text_input('', placeholder='Pega la directamente la URL del artículo que quieres resumir y presiona Enter')



if url:
    try:
        article = newspaper.Article(url)

        article.download()
        # article.html
        article.parse()

        img = article.top_image
        st.image(img)
        

        title = article.title
        st.subheader(title)
        

        authors = article.authors
        st.text(','.join(authors))
        
        article.nlp()
        

        
        #keywords = article.keywords
        #st.subheader('Keywords:')
        #st.write(', '.join(keywords))
        
        
        
        tab1, tab2= st.tabs(["Texto completo", "Resumen"])
        with tab1:
            txt = article.text
            txt = txt.replace('Advertisement', '')
            st.write(txt)
        
        with tab2:
            st.subheader('Resumen')
            summary = article.summary
            summary = summary.replace('Advertisement', '')
            st.write(summary)
        
        
    except:
        st.error('Por favor intenta pegar la dirección de la noticia nuevamente')
        
