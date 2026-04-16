import streamlit as st
from PIL import Image
from api_call import call_to_api

# sidebar
with st.sidebar:
    st.header('Controls')

    uploaded_images = st.file_uploader(label="Upload here...",type=['jpg','png','jpeg'],accept_multiple_files=True)

    if uploaded_images:
        st.markdown('Your Uploaded Images')
        st.image(uploaded_images)

    st.divider()
    
    selected_option = st.selectbox(label='Choose an option',options=['Hints','Solution With Code'],index=None)
    if selected_option:
        st.markdown(f"You Choose : {selected_option}")
    debug_button = st.button(label='Debug Code',type='primary')

#main page
st.title('AI Code Debuger',text_alignment='center')
st.write("It's a most populer AI code debuger app. Here you can find soluton of code error easily. Just upload an image of error & select an option of solution type. Finally click on Debug Code.")
st.divider()

if debug_button:
    try:
        if selected_option == None or len(uploaded_images)==0:
            raise Exception('Please upload images & select an option to debug code !')
    except Exception as e:
        st.error(e)
    else:
        # deal with api
        emb_images = []
        for img in uploaded_images:
            emb_images.append(Image.open(img))
            
        with st.container(border=True):
            with st.spinner('Generating your solution...'):
                generative_result = call_to_api(emb_images,selected_option)
                st.markdown(generative_result)