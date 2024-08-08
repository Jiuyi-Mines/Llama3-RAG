## Llama3 - RAG
This project includes a simple example of Llama3's RAG.

### Environment Configuration
```
# python=3.9
pip install requirements.txt

# install docker and keep it running
# run the following commands in the terminal
docker pull phidata/pgvector:16
docker volume create pgvolume
docker run -itd -e POSTGRES_DB=ai -e POSTGRES_USER=ai -e POSTGRES_PASSWORD=ai -e PGDATA=/var/lib/postgresql/data/pgdata -v pgvolume:/var/lib/postgresql/data -p 5532:5432 --name pgvector phidata/pgvector:16

# install ollama (free) for Knowledge Base Embedding (You can also try openai's model but it is expensive)
ollama run nomic-embed-text

# configure your own GROQ_API_KEY

# run the RAG
streamlit run app.py
```
