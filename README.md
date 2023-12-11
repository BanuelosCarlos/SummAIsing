# SummAIsing tool



## Introduction
------------
This tool is intended to help people to summarize and chat to a bot that answers questions about Youtube videos that you provide.
- It retrieves the main topic
- Summarizes the content of the video
- Returns keywords
- Then you can ask questions about the content of the video

## How It Works
------------
This tool work as follows:

1. You provide a Youtube URL (Which audio is smaller than 20 MB)
2. It downloads the audio locally
3. The it uses the OpenAI api to call Whisper-1 and transforms the audio to text
4. The promt to ChatGPT3.5 model to give details of the text
5. Also the extracted text then is splitted in smaller chunks to create a vector store (uses OpenAI embedding)
6. It uses the vector store as a knowledge base to answers questions with ChatGPT3.5 model

## Dependencies and Installation
----------------------------
To install the SummAIsing tool please follow this steps:

1. Clone this repository to your local.

2. Run the makefile in the terminal isnide the project folder (This will install the venv with the python version and the requirements)
   ```commandline
   make
   ```
4. Obtain an API key from OpenAI and add it to the `.env` file in the project directory.
   ```commandline
   OPENAI_API_KEY=your_secrit_api_key
   ```
## Usage
-----
To use the SummAIsing tool you need to:

1. Be sure that you installed the dependencien and set yoy OpenAI api key in the `.env` file

2. Run the `main.py` file using the Streamlit CLI. Execute the following command:
   ```
   streamlit run app.py
   ```

3. The application will launch in your default web browser, displaying the user interface.

4. Copy and paste the Youtube's URL that you want to the box in the interface and press 'Proccess'.

5. Now you recieve the summarization and also you can chat with the bot to know more about the video.

## Aknowledments and references
Thanks for all the AI content creator, to Wizeline Academy for this sprint and all your effort
Based on [YouTube](https://youtu.be/dXxQ0LR-3Hg).


## License

This project is licensed under the MIT License - see the [Licence](./LICENSE.md) file for details.

