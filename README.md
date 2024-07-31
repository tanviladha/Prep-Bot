# Prep-Bot
# Overview <br/>
PrepBot is a personal project with the help of online tutorials aimed at gaining experience  with natural language processing techniques and chatbpts. This project was developed in three iterations, each with progressing complexity and effectiveness. PrepBot specializes in offering interview advice for those entering the field of computer science. <br/>
# Project Iterations <br/>
<br/>
**Iteration 1: Basic Chatbot with difflib** <br/>
In the first iteration, PrepBot was created using the built-in Python library difflib. This version of the chatbot saved user prompts in a json file so it could learn over time. This simple approach allowed for basic string matching and provided a foundation for further development with NLP. This project was created from the tutorial found here: https://www.youtube.com/watch?v=CkkjXTER2KE <br/>
<br/>
Key Features: <br/>
&emsp Utilized difflib for string matching 
&emsp Offered user to help teach chatbot. Saved all prompts in a question/answer style json file for basic learning. <br/>
**Iteration 2: Chatbot with NLP** <br/>
The second version introduced natural language processing capabilities through the NLTK library. I fed the bot articles from the web. The tutorial I followed used a count vectorizer but I chose to improve the effectiveness by using a TF-IDF vectorizer, though a better method may have been word embeddings. Cosine similarity was employed to generate more accurate and contextually relevant responses. This project was created with help from the tutorial found here: https://www.youtube.com/watch?v=9KZwRBg4-P0 <br/>
Key Features: <br/>
&emsp Implemented TF-IDF vectorizer for text processing.
&emsp Used cosine similarity to measure the relevance of responses.
&emsp Enhanced response accuracy with web-sourced articles. <br/>
**Iteration 3: Chatbot with OpenAI APIs** <br/>
The third version used OpenAI's APIs, resulting in the most effective chatbot of the three versions. This version leveraged the advanced capabilities of OpenAI's language models to provide high-quality and more accurate responses. Resources used: **INSERT RESOURCES HERE** <br/>
Key Features: <br/>
&emsp Integrated OpenAI APIs <br/>
<br/>
**Acknowledgments**
Thanks to the contributors of difflib, scikit-learn, and OpenAI for their tools and libraries as well as the online tutorials that helped teach me. 





