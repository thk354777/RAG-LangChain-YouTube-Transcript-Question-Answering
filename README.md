# LangChain YouTube Transcript Question Answering (RAG Framework)

This application demonstrates how to use LangChain in a Retrieval-Augmented Generation (RAG) framework to process YouTube video transcripts, store them in a FAISS vector database, and query them using a locally hosted LLM. The app uses **React** as the frontend for a simple and interactive user interface.

![alt text](langchain_llm_url (2).png "Code GPT Screenshot")

## Table of Contents

- [Installation](#installation)
- [Acknowledgements](#acknowledgements)
- [Features](#Features)
- [Workflow](#Workflow)
  
## Features
- **Transcript Processing**: Extracts and splits YouTube video transcripts into manageable chunks.
- **Embedding Creation**: Embeds transcript chunks using HuggingFace Sentence Transformers (all-MiniLM-L6-v2).
- **Vector Store**: Stores embeddings in a FAISS vector database for similarity search.
- **Query Response with RAG**: Retrieves the most relevant transcript chunks and uses a local LLM to answer user queries based on these chunks.
- **Interactive UI**: Built with **React** for easy input and output interaction.

### Future Enhancements:
- **Timestamp in Video**: Display timestamp in the video for each relevant query result.
- **Integration with ChromaDB**: For improved vector store management.
- **Support for Videos Without Subtitles**: Expand the application to handle videos without subtitles.

## Workflow
1. **Extract Transcript**: Load the YouTube video's transcript using `YoutubeLoader`.
2. **Text Splitting**: Split the transcript into smaller chunks using `RecursiveCharacterTextSplitter` to handle long documents.
3. **Embedding**: Embed the text chunks with `HuggingFaceEmbeddings`.
4. **Vector Store**: Save the embeddings in a FAISS vector database.
5. **RAG Query Response**: Retrieve the top k relevant chunks and use the LLM (`llama-3.2-1b-instruct`) to generate answers based on these chunks.

<font color="red">⚠️**WARNING**</font>: I use my LLM (locally hosted model).

## Installation

Include instructions on how to install your project. You can include the following:

- Prerequisites
1. Clone this repo
2. Create the python virtual environment inside the cloned directory
```console
conda create..
```

3. Install the pre-requisite 
WARNING: Will take considerable time to install all the dependent packages.

```console
pip install -r requirements.txt
```

- How to run the project
```console
streamlit run app.py
```

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)



## Acknowledgements

Most of the code is borrowed from the following
https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/recursive_text_splitter/
https://api.python.langchain.com/en/latest/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html
