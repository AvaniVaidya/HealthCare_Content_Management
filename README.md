# **Healthcare Content Summarization Tool**
This Python-based tool provides summarizations of healthcare texts using both extractive and abstractive methods. The extractive summarizer uses NLTK for text processing and NetworkX for sentence ranking based on similarity, while the abstractive summarizer leverages the powerful BART model from Hugging Face's transformers library.

## **Features**
Extractive Summarization: Generates a summary by identifying the most relevant sentences in the text. \
Abstractive Summarization: Creates a concise paraphrase of the original text that captures its meaning using advanced NLP models.

## **Installation**
Before running the application, you must install the required Python libraries. This project requires Python 3.6+.

1. Clone the Repository
   ```
    git clone https://github.com/AvaniVaidya/HealthCare_Content_Management.git
   ```
   ```
    cd HealthCare_Content_Management
   ```
   ```
    cd HealthCareManagement
   ```

3. Set up a Python Virtual Environment (Recommended - MacOS)
   ```
    python -m venv <env_name>
    source <env_name>/bin/activate
   ```
   
5. Install Required Libraries
   ```
    pip install streamlit nltk networkx transformers
   ```

## **Usage**
Run the Streamlit application using the following command:
```
streamlit run app.py
```
After running the command, Streamlit will start the server and provide a local URL, usually http://localhost:8501, which you can open in your web browser to interact with the application.

## **Files Description**
app.py: The main Python script with Streamlit interface setup.\
extractive_summarizer.py: Contains the ExtractiveSummarizer class used for extractive summarization.\
abstractive_summarizer.py: Contains the AbstractiveSummarizer class which utilizes the transformers library for abstractive summarization.

## **Contributing**
Contributions are welcome.
