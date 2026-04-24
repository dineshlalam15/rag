from langchain_community.document_loaders import (
    CSVLoader, 
    PyPDFLoader, 
    UnstructuredHTMLLoader, 
    UnstructuredMarkdownLoader, 
    WikipediaLoader
)

csv_loader = CSVLoader(file_path='/Users/dineshlalam15/Desktop/Exercise/rag_test_data.csv')
pdf_loader = PyPDFLoader(file_path='/Users/dineshlalam15/Desktop/Exercise/rag_loading_test.pdf')
html_loader = UnstructuredHTMLLoader(file_path='/Users/dineshlalam15/Desktop/Exercise/rag_test_data.html')
md_loader = UnstructuredMarkdownLoader(file_path='/Users/dineshlalam15/Desktop/Exercise/rag_test_md.md')
wiki_loader = WikipediaLoader()

data = md_loader.load()
print(data)
print(data[0])