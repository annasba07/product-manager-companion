

openai.api_key = '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'



from openai.embeddings_utils import get_embedding, cosine_similarity


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

question = "what is the future of product management? \n"
query = "Q: " + question + " A: "



df["similarities"] = df.embeddings.apply(lambda x: np.dot(np.array(embeddingpm), np.array(x)))
df = df.sort_values(by=['similarities'], ascending=False)
df = df.reset_index(drop=True)


context = df.combined[0]
#+ df.combined[1] 
#+ df.combined[2]  + df.combined[3]
len(context)




prompt = """You are a product management expert. Answer the question in detail using the provided context, and if the answer is not contained in the text above then answer it how you normally would. Explain things in a lot of detail.   \n""" + context + query

openai.Completion.create(
    prompt=prompt,
    temperature=0,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    model=COMPLETIONS_MODEL
)["choices"][0]["text"].strip(" \n")


