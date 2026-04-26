from langchain_community.document_loaders import (
    CSVLoader, 
    PyPDFLoader, 
    UnstructuredHTMLLoader, 
    UnstructuredMarkdownLoader, 
    WikipediaLoader,
    ArxivLoader,
    WebBaseLoader,
    PlaywrightURLLoader
)

"""
- file_path: file_path will be a path of file located.
- for CSVLoader, PyPDFLoader, UnstructuredHTMLLoader, UnstructuredMarkDownLoader for loading different types of documents. 
- for WikipediaLoader, in query you can just give a topic name and deep under uses Wikipedia Search API to find the most relevant articles
    with the name of "Quatum Computing". 
- load_max_docs - loads that number of top matching documents that are matching the query name. 
- for ArxivLoader - official arXiv API, query = name/arxiv id which uses to fetch all the details of that page. 


"""

csv_loader = CSVLoader(file_path='/Users/dineshlalam15/Desktop/Exercise/rag_test_data.csv')
pdf_loader = PyPDFLoader(file_path='/Users/dineshlalam15/Desktop/Exercise/rag_loading_test.pdf')
html_loader = UnstructuredHTMLLoader(file_path='/Users/dineshlalam15/Desktop/Exercise/rag_test_data.html')
md_loader = UnstructuredMarkdownLoader(file_path='/Users/dineshlalam15/Desktop/Exercise/rag_test_md.md')
wiki_loader = WikipediaLoader(query="Quantum Computing", load_max_docs=2)
arxiv_loader = ArxivLoader(query="2312.10997", load_max_docs=2)

user_urls = ["https://www.rottentomatoes.com/m/they_call_him_og", "https://www.rottentomatoes.com/m/guntur_kaaram"]
webbase_loader = WebBaseLoader(user_urls)
play_wright_loader = PlaywrightURLLoader(urls=user_urls, remove_selectors=["header","footer"])

data = webbase_loader.load()
print(data)
print(data[0].metadata)