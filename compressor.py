from chat import chat
from load import base_retriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.multi_query import MultiQueryRetriever

base_compressor = LLMChainExtractor.from_llm(llm=chat)
mq_retriever = MultiQueryRetriever.from_llm(retriever=base_retriever, llm=chat)

compression_retriever = ContextualCompressionRetriever(retriever=base_retriever, compressor=base_compressor)
matched_docs = compression_retriever.get_docs(query=query)






