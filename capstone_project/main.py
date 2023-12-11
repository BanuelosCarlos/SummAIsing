
#  %% Main
from dotenv import load_dotenv
import streamlit as st
import synapse_module as sm
from TemplatesHTML import css

def main():
    
    load_dotenv()
    #client = openai.OpenAI()
    st.set_page_config(
        page_title='Answer your questios from a Youtube video',
        page_icon=':tv:')
    
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.header("Answer your questions from a Youtube video :robot_face: :")
    user_question = st.text_input("Ask a question about the video:")
    if user_question:
        sm.handle_userinput(user_question)

    with st.sidebar:
        st.subheader("The video")
        video_to_process = st.text_input("Paste your Youtube URL and click on 'Process'")
        if st.button("Process"):
            with st.spinner("Processing"):
                file_name, string_ = sm.download_audio(video_to_process)
                st.write(string_)
                text = str(sm.mp3_to_text(file_name))
                st.session_state.summarization = sm.summarize_text(text)
                st.write(st.session_state.summarization)

                # get the text chunks
                text_chunks = sm.get_text_chunks(text)

                # create vector store
                vectorstore = sm.get_vectorstore(text_chunks)

                # create conversation chain
                st.session_state.conversation = \
                    sm.get_conversation_chain(vectorstore)

                



# %%
if __name__ == '__main__':
    main()