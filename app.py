import streamlit as st
import time
import requests
from datetime import date
from PIL import Image
from io import BytesIO
from datetime import datetime
from constants import *
from utils import get_client

page_bg_img = '''
		<style>
			.stApp,.e8zbici2 {
			background-image: url("https://raw.githubusercontent.com/justray8now/multiapps/main/backgroundweb.png");
			background-size: cover;
			}
			</style>
			'''

st.markdown(page_bg_img, unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

lsp = date.today()
now = datetime.now()

current_time = now.strftime("%I:%M:%S  %p")
with col1:
        st.write(lsp)
with col4:
        st.write(current_time)



option = st.sidebar.selectbox(
    'Pilih Tipe Pencarian',
     ['Trending','Kata Kunci'])

if option=='Trending':
 

    st.title('CABER 📰 ')
    st.markdown("""
    **Baca Berita Sesuai Selera**.
    """)


    country_choice = st.selectbox("Negara 🎌:", options=countries,
                                            index=5,
                                            help='Pilih sumber dari negara mana 👇')
    search_choice = st.radio('Pencarian Melalui : ', options=['Berita Trending'])

    if search_choice == 'Berita Trending':
        Client = get_client()

        category = st.selectbox('Topik:',
                                        options=topics, index=0)

        st.write("## Pencarian Spesifik 🔎")
        time_span = st.text_input("Waktu Rilis: ⏲ ", '7Hari',
                                        help="""
            - h = hours (eg: 12h)
            - d = days (eg: 7d)
            - m = months (eg: 6m)
            - y = years (eg: 1y)
        """)
        article_num = st.number_input("Jumlah Artikel 📚 ", 1, 100, 10)
        lang = st.selectbox("Bahasa 🔠:", options=languages,
                                    index=0,
                                    help='Language of news to be fetched')

        Client.period = time_span
        Client.country = country_choice
        Client.max_results = article_num
        Client.language = lang

        if category == "GENERAL":
            st.write(f'**Berita hangat dari topik** _{category.upper()}_ **!!**')
            # General call of gnews client
            news_ls = Client.get_top_news()

        else:
            st.write(f'**Berita hangat dari topik** _{category.upper()}_ **!!**')
            # Topic call of gnews client
            news_ls = Client.get_news_by_topic(category.upper())

    for i in range(len(news_ls)):
        try:
            article = Client.get_full_article(news_ls[i]['url'])
            st.title(article.title)
            st.image(article.top_image)
            st.write(f"###### Waktu Publikasi: {news_ls[i]['published date']}")
            st.write(f"###### Sumber: {news_ls[i]['publisher']['title']}")
            with st.expander("Baca Artikel📖 "):
                st.write(article.text)
            st.write(f"[Link Artikel]({news_ls[i]['url']})")
        except Exception as err:
            print(err)

    
    
    
    
    
import requests
title = []

if option=='Kata Kunci':

    st.title('CABER 📰')
    intro = 'Baca Berita Sesuai Selera'
    st.header(intro) 

    user = st.text_input('Masukkan Kata Kunci', '...', )
    user = user.lower()
    news = st.button('Cari Berita 🔎')

    
    response = requests.get('https://raw.githubusercontent.com/justray8now/screamlit/main/sumber.png')
    image = Image.open(BytesIO(response.content))
    st.image(image, caption='By REY Media - rahmatagengyuwana@gmail.com', output_format='PNG')

    if news:
        if len(user) !=0 and user!='israel':
            global j
            j=0
            url = 'https://newsapi.org/v2/everything?q={}&apiKey=5c4c90af744949d4a935e12b9c07c52c'.format(user,lang="id")
            req = requests.get(url).json()
            impdata = req['articles']
            imageurl = [] 
            media = []
            title = []
            description = []
            url = []
            author = [] 
            dates = []

            Newspackets = []

            for i in impdata:
                imageurl.append(i['urlToImage'])
                media.append(i['source']['name'])
                title.append(i['title'])
                description.append(i['description'])
                url.append(i['url'])
                author.append(i['author'])
                dates.append(i['publishedAt'].split('T')[0])

            for i in range(len(url)):
                Newspackets.append([imageurl[j], media[j], title[j], description[j], url[j], author[j], dates[j]])
                j+=1
            for i in Newspackets:
                    response = requests.get(i[0])
                    img = Image.open(BytesIO(response.content))
                    st.image(img, 'Referensi', width=500)
                    st.write("Sumber : ", i[1])
                    st.subheader(i[2])
                    st.write(i[3])
                    st.write('Link Artikel : ', i[4])
                    st.write("Penulis : ", i[5])
                    st.write('Artikel Terbit : ', i[6])
                    st.text('')
                    st.text('')
                    st.text('')
                    st.text('')
                    st.write('')
            st.subheader("-----------------")
            st.subheader("Terima Kasih")

        elif len(user) == 0:
            st.write('Enter Something...')

        else:
            st.write('Sorry We Have Nothing To Show On This')
