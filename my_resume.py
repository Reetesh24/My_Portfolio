import streamlit as st
st.set_page_config(page_title= 'My Resume', page_icon= ":prince:", layout= "wide")
my_image = './Assests/Reetesh.jpeg'
img1 = "./Assests/Where Love Begins (A Movie Poster).jpg"
img2 = "./Assests/Horror Movie Poster (Night Full Of Mystery).png"
img3 = "./Assests/Thumbnail For Youtube.png"
img4 = "./Assests/I WIsh I Could Tell Her Main file.png"
img5 = "./Assests/Wish We HAd Never Met Each Other 4.jpg"
col1, col2 = st.columns(2)
# with col1:
#     st.image(my_image, width= 100)
# with col2:
#     st.header(":blue[Reetesh Kumar Shukla]")
with st.sidebar:
    col1, col2 = st.columns([1,2])
    with col1:
        st.image(my_image, width=200)
    with col2:
        st.subheader('''Reetesh Kumar Shukla''')
        st.markdown('''### Shukla Ji''')
    st.write("\n")
    st.subheader(":green[Contact Info]")
    st.write(":email: Email ID: "'[reeteshsnshukla@gmail.com](https://mail.google.com/mail/u/0/#inbox?compose=DmwnWrRmTNmrFqSHksCBpvTxMpQVXlRcWDgBpfJBJsfpflRTZFXDPvqtnKrCBqpfgnjRXmbDmScl)')
    st.write("📞 Phone No.: 966790xxxx")
    st.markdown('‍🎨 Behance Profile: ''[Click Here](https://www.behance.net/reeteshshukla1)')

st.header(":blue[Reetesh Kumar Shukla :crown:]", divider="gray")
st.write("Welcome to my profile here you can see my Adobe Photoshop works.")
st.write("\n")
st.write("View My Work")

col_1, col_2, col_3 = st.columns([1,1,1])
with col_1:
    with st.expander("**Where Love Begins**"):
        st.image(img1)
with col_2:
    with st.expander("**Night Full Of Mystery**"):
        st.image(img2)
with col_3:
    with st.expander("**Broken YouTube Thumbnail**"):
        st.image(img3)
col_4, col_5, col_6 = st.columns([1,1,1])
with col_4:
    with st.expander("**I WIsh I Could Tell Her**"):
        st.image(img4)
with col_5:
    with st.expander("**Wish We Had Never Met Each Other**"):
        st.image(img5)
