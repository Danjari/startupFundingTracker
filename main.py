# import pandas as pd
# from sentence_transformers import SentenceTransformer
# import faiss
# import numpy as np
# import time
# import sys
# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# os.environ["TOKENIZERS_PARALLELISM"] = "false"

# # Load environment variables from .env file
# load_dotenv()

# # Initialize OpenAI client
# client = OpenAI()
# client.api_key = os.getenv("OPENAI_API_KEY")
# systemPrompt = '''You are tasked with summarizing articles by extracting the key information only.
#  Keep the content concise, clear, and engaging to drive curiosity and encourage the reader to click the provided link for full details. 
#  No introductions or filler—just focus on the core points.'''

# # Load CSV
# df = pd.read_csv('techcrunch.csv')
# df['Content'] = df['Content'].fillna('')  # Handle missing content if any
# combined_texts = df['Content'].tolist()

# # Load pre-trained transformer model
# model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# # Create embeddings for each article's content
# embeddings = model.encode(combined_texts)

# # Create a FAISS index
# d = embeddings.shape[1]  # Embedding dimension
# index = faiss.IndexFlatL2(d)  # L2 distance for similarity

# # Convert embeddings to a NumPy array and add them to the index
# embeddings_np = np.array(embeddings).astype('float32')
# index.add(embeddings_np)

# # Check the number of vectors in the index
# print(f"Total articles indexed: {index.ntotal}")

# def loading_animation(message, duration=3):
#     """ Simulates a loading animation for visual feedback """
#     for i in range(duration):
#         sys.stdout.write(f'\r{message}{"." * (i % 4)}')
#         sys.stdout.flush()
#         time.sleep(1)
#     print("\r" + " " * len(message) + "\r")  # Clear the line after loading

# def search_articles(query, top_n=5):
#     """ Search for top_n articles related to the query """
#     loading_animation("Searching for the best articles", 3)
    
#     # Embed the query
#     query_embedding = model.encode([query])

#     # Search the FAISS index
#     distances, indices = index.search(np.array(query_embedding).astype('float32'), top_n)

#     # Return the results
#     results = []
#     for idx in indices[0]:
#         result = {
#             'Title': df.iloc[idx]['Title'],
#             'Author': df.iloc[idx]['Author'],
#             'URL': df.iloc[idx]['URL'],
#             'Content': df.iloc[idx]['Content']
#         }
#         results.append(result)
    
#     return results

# def enhance_with_gpt(articles):
#     """ Enhance the search results with GPT responses """
#     enhanced_results = []
#     loading_animation("Enhancing results with AI", 2)
    
#     for article in articles:
#         # Format content for GPT
#         prompt = f"Please summarize the following using {systemPrompt} guidelines:\n\n"
#         prompt += f"Title: {article['Title']}\n"
#         prompt += f"Author: {article['Author']}\n"
#         prompt += f"Content Snippet: {article['Content'][:500]}\n\n"
       
        
#         # Use OpenAI to enhance content
#         response = client.chat.completions.create(
#             model="gpt-4o-mini",  
#             messages=[
#                 {"role": "system", "content": systemPrompt},
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=200,
#             temperature=0.7,
#         )
        
#         # Extract the response content
#         enhanced_content = response.choices[0].message.content
        
#         # Append enhanced content to the result
#         enhanced_results.append({
#             'Title': article['Title'],
#             'Main points': enhanced_content,
#             'Author': article['Author'],
#             'URL': article['URL'],
            
#         })
        
#     return enhanced_results
# first  = True
# # Main loop for user interaction
# while True:
#     if first == True:
#         query = input("\nHow can I help you today? (Type 'exit' to quit): ")
#     else: 
#         query = input("\nAnything else you'd like to know?:  ")
#     first = False
#     if query.lower() == "exit":
#         print("Goodbye! Have a great day!")
#         break
    
#     # Perform the FAISS search
#     faiss_results = search_articles(query)

#     # Enhance with GPT
#     enhanced_results = enhance_with_gpt(faiss_results)

#     # Display the enhanced results
#     for res in enhanced_results:
#         print(f"\nTitle: {res['Title']}\n ------------------------------------------------------------------\nMain points: {res['Main points']}\n ------------------------------------------------------------------\nAuthor: {res['Author']}\n ------------------------------------------------------------------\n URL: {res['URL']}\n")
#         print("##########################################################################")

import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import time
import sys
import os
from dotenv import load_dotenv
from openai import OpenAI

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")
systemPrompt = '''You are tasked with summarizing articles by extracting the key information only.
 Keep the content concise, clear, and engaging to drive curiosity and encourage the reader to click the provided link for full details. 
 No introductions or filler—just focus on the core points. please don't use any formater (NO * No nothing just the main points in concise sentences)'''

# Load CSV
df = pd.read_csv('techcrunch.csv')
df['Content'] = df['Content'].fillna('')  # Handle missing content if any
combined_texts = df['Content'].tolist()

# Load pre-trained transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Create embeddings for each article's content
embeddings = model.encode(combined_texts)

# Create a FAISS index
d = embeddings.shape[1]  # Embedding dimension
index = faiss.IndexFlatL2(d)  # L2 distance for similarity

# Convert embeddings to a NumPy array and add them to the index
embeddings_np = np.array(embeddings).astype('float32')
index.add(embeddings_np)

# Check the number of vectors in the index
print(f"Total articles indexed: {index.ntotal}")

def clear_terminal():
    """ Clear the terminal screen """
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(message, duration=3):
    """ Simulates a loading animation for visual feedback """
    for i in range(duration):
        sys.stdout.write(f'\r{message}{"." * (i % 4)}')
        sys.stdout.flush()
        time.sleep(1)
    print("\r" + " " * len(message) + "\r")  # Clear the line after loading

def search_articles(query, top_n=3):
    """ Search for top_n articles related to the query """
    loading_animation("Searching for the best articles", 3)
    
    # Embed the query
    query_embedding = model.encode([query])

    # Search the FAISS index
    distances, indices = index.search(np.array(query_embedding).astype('float32'), top_n)

    # Return the results
    results = []
    for idx in indices[0]:
        result = {
            'Title': df.iloc[idx]['Title'],
            'Author': df.iloc[idx]['Author'],
            'URL': df.iloc[idx]['URL'],
            'Content': df.iloc[idx]['Content']
        }
        results.append(result)
    
    return results

def enhance_with_gpt(articles):
    """ Enhance the search results with GPT responses """
    enhanced_results = []
    loading_animation("Enhancing results with AI", 2)
    
    for article in articles:
        # Format content for GPT
        prompt = f"Please summarize the following using {systemPrompt} guidelines:\n\n"
        prompt += f"Title: {article['Title']}\n"
        prompt += f"Author: {article['Author']}\n"
        prompt += f"Content Snippet: {article['Content'][:500]}\n\n"
       
        
        # Use OpenAI to enhance content
        response = client.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "system", "content": systemPrompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7,
        )
        
        # Extract the response content
        enhanced_content = response.choices[0].message.content
        
        # Append enhanced content to the result
        enhanced_results.append({
            'Title': article['Title'],
            'Main points': enhanced_content,
            'Author': article['Author'],
            'URL': article['URL'],
            
        })
        
    return enhanced_results

first = True
# Main loop for user interaction
while True:
    
    if first:
        clear_terminal()  # Clear the terminal before each interaction
        print("🔍 Hey nice to have you here! ")
        print("This helps you find and summarize the most relevant articles in tech kinda quickly.")
        print("\n💡 Example questions you can ask:")
        print("   1. Who raised funding in tech lately?")
        print("   2. What's new in the world of AI?")
        query = input("\nHow can I help you today? (Type 'exit' to quit): ")
    else: 
        clear_terminal() 
        query = input("\nAnything else you'd like to know?:  ")
         
    first = False
    if query.lower() == "exit":
        print("Goodbye! Have a great day!")
        break
    
    # Perform the FAISS search
    faiss_results = search_articles(query)

    # Enhance with GPT
    enhanced_results = enhance_with_gpt(faiss_results)
    for res in enhanced_results:
        print("\n" + "="*70)
        print(f"📘  Title: \033[1m{res['Title']}\033[0m")  # Bold title
        print("="*70)
        print("\n🔑  Main points: \n" + "-"*70)
        print(f"{res['Main points']}")
        print("-"*70)
        print(f"\n🖊️  Author: {res['Author']}")
        print(f"\n🔗  URL: \033[4m{res['URL']}\033[0m")  # Underline the URL
        print("\n" + "="*70)
        print("✨" + " " * 5 + "End of article" + " " * 5 + "✨")
        print("##########################################################################\n")
    input("Press ENTER to ask another question... ")