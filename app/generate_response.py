



import openai
import pandas as pd
import numpy as np

from openai.embeddings_utils import get_embedding, cosine_similarity

openai.api_key = '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'
COMPLETIONS_MODEL = "text-davinci-002"


def question_embeddings(question):
    embedding = get_embedding(
        question,
        engine="text-embedding-ada-002"
    )
    return embedding


def create_context(question, context):
    query = "Q: " + question + " A: "
    prompt = """You are a product management expert. Answer the question in detail using the provided context, and if the answer is not contained in the text above then answer it how you normally would. Explain things in a lot of detail.   \n"""
    return prompt + context + query


def get_answer(question, context):
    prompt = create_context(question, context)
    response = openai.Completion.create(
        prompt=prompt,
        temperature=0,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model=COMPLETIONS_MODEL
    )["choices"][0]["text"].strip(" \n")
    return response


def get_context():
    context = None

def get_content():
    input_datapath = 'file path.csv'  # to save space, we provide a pre-filtered dataset
    df = pd.read_csv(input_datapath, index_col=0)
    return df


def get_similarity(df, embeddingpm):
    df["similarities"] = df.embeddings.apply(lambda x: np.dot(np.array(embeddingpm), np.array(x)))
    df = df.sort_values(by=['similarities'], ascending=False)
    df = df.reset_index(drop=True)
    return df

def generate_response(question):
    
    #get question embeddings
    questionem = question_embeddings(question)

    #get embedded content
    content = get_content()

    #get similarity


    #get top 5 most similar


    #get context


    #get answer











