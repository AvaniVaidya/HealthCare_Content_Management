import streamlit as st
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
import nltk
nltk.download('stopwords')
nltk.download('punkt')
stop_words=stopwords.words('english')


class ExtractiveSummarizer:
    
    def _init_(self):
        return
    
    
    def sentence_similarity(self, sent1, sent2, stopwords=None):
        if stopwords is None:
            stopwords = []

        sent1 = sent1.split(" ")
        sent2= sent2.split(" ")
        
        sent1 = [w.lower() for w in sent1]
        sent2 = [w.lower() for w in sent2]

        all_words = list(set(sent1 + sent2))

        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)

        # build the vector for the first sentence
        for w in sent1:
            if w in stopwords:
                continue
            vector1[all_words.index(w)] += 1

        # build the vector for the second sentence
        for w in sent2:
            if w in stopwords:
                continue
            vector2[all_words.index(w)] += 1

        return (1 - cosine_distance(vector1, vector2))
    
    
    def build_similarity_matrix(self, sentences, stop_words):

        # Create an empty similarity matrix
        similarity_matrix = np.zeros((len(sentences), len(sentences)))

        for idx1 in range(len(sentences)):

            for idx2 in range(len(sentences)):

                if idx1 == idx2: #ignore if both are same sentences
                    continue 
                similarity_matrix[idx1][idx2] = self.sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

        return similarity_matrix
    
    
    def generate_summary(self, sentences):

        # fileobj = open(r"C:\Users\Tanmayee\Desktop\bTECH_Project\Final Year Project App\sample.txt","r")
        # sentences = fileobj.readlines()
        conversation = sentences.split(".")
        conversation.pop()

        top_n = len(conversation)//2
        stop_words = stopwords.words('english')
        print(conversation)
        summarize_text = []
        summary_ex = ""
        sentence_similarity_martix = self.build_similarity_matrix(conversation,stop_words)

        # Step 3 - Rank sentences in similarity martix

        sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)

        scores = nx.pagerank(sentence_similarity_graph)

        # Step 4 - Sort the rank and pick top sentences

        ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(conversation)), reverse=True)    

        print("Indexes of top ranked_sentence order are ", ranked_sentence)    

        for i in range(top_n):

          summarize_text.append("".join(ranked_sentence[i][1]))
          summary_ex = summary_ex + ranked_sentence[i][1]+"."

        # Step 5 - Offcourse, output the summarize texr
       
        print("\n\n\nSummarize Text: \n", ".".join(summarize_text))
        return summary_ex