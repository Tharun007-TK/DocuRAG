# 📚 DocuChat - Intelligent Document Assistant

**DocuChat** is a powerful Retrieval-Augmented Generation (RAG) system that transforms your documents into interactive conversations. Upload any document and start chatting with your data using advanced AI technology powered by Ollama, LangChain, and ChromaDB.

## 🌟 What Makes DocuChat Special?

Transform static documents into dynamic conversations. Whether it's research papers, business reports, or personal notes, DocuChat makes your information instantly searchable and conversational.

## 🚀 Key Features

- **📤 Multi-Format Support** - Upload PDFs, Word docs, text files, spreadsheets, presentations, and images
- **🔍 Smart Search** - Vector-based semantic search finds relevant content even with different wording
- **💬 Natural Conversations** - Chat with your documents like you're talking to a knowledgeable assistant
- **🧠 Context Memory** - Maintains conversation history for coherent, multi-turn discussions
- **🖼️ OCR Integration** - Extract and chat with text from images using Tesseract OCR
- **⚡ Real-time Processing** - Fast document indexing and retrieval

### Supported File Types
- **Documents**: `.pdf`, `.txt`, `.docx`, `.csv`, `.pptx`
- **Images**: `.png`, `.jpg`, `.jpeg` (with OCR)

## 🛠️ Technology Stack

- **🦜 LangChain** - Document processing and chain orchestration
- **🦙 Ollama** - Local LLM inference and embeddings
- **🗄️ ChromaDB** - Vector database for semantic search
- **🎨 Streamlit** - Interactive web interface
- **👁️ Tesseract OCR** - Optical character recognition

## 📦 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/docuchat.git
cd docuchat
```

### 2. Set Up Environment
```bash
# Create virtual environment
python -m venv docuchat-env
source docuchat-env/bin/activate  # Linux/macOS
# or
docuchat-env\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Install Tesseract OCR
- **Windows**: Download from [GitHub Tesseract releases](https://github.com/tesseract-ocr/tesseract)
- **macOS**: `brew install tesseract`
- **Linux**: `sudo apt install tesseract-ocr`

### 4. Set Up Ollama Models
```bash
# Install required models
ollama pull llama3.2:latest
ollama pull mxbai-embed-large
```

### 5. Launch DocuChat
```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` and start chatting with your documents! 🎉

## 📋 Dependencies (requirements.txt)

```txt
streamlit>=1.28.0
pandas>=2.0.0
python-docx>=0.8.11
python-pptx>=0.6.21
PyMuPDF>=1.23.0
pytesseract>=0.3.10
pillow>=10.0.0
langchain>=0.1.0
langchain-ollama>=0.1.0
langchain-chroma>=0.1.0
langchain-community>=0.0.10
chromadb>=0.4.0
```

## 🏗️ Project Architecture

```
docuchat/
├── app.py                    # Streamlit web interface
├── vector.py                 # Document processing & vector operations
├── requirements.txt          # Python dependencies
├── chrome_langchain_db/      # ChromaDB storage (auto-created)
└── README.md                # This file
```

## 🔧 Configuration

### Ollama Setup
Ensure Ollama is running locally with these models:
- **LLM**: `llama3.2:instruct` (for chat responses)
- **Embeddings**: `mxbai-embed-large` (for document vectorization)

### Tesseract Configuration
For Windows users, you may need to set the Tesseract path:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## 💡 Usage Tips

1. **Optimal File Sizes**: Keep documents under 50MB for best performance
2. **Image Quality**: Higher resolution images provide better OCR results
3. **Question Formulation**: Ask specific questions for more accurate responses
4. **Context Awareness**: Reference previous parts of the conversation for follow-up questions

## 🎯 Roadmap

### Coming Soon
- **🔄 Response Streaming** - Real-time response generation
- **📝 Document Summarization** - Auto-generate document summaries
- **💾 Chat Export** - Download conversation history
- **🎨 Enhanced UI** - Drag-and-drop file uploads
- **🔐 Authentication** - User accounts and document management
- **🌐 Cloud Deployment** - Deploy to cloud platforms

### Future Enhancements
- Multi-language support
- Document comparison features
- Advanced analytics dashboard
- API endpoints for integration

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangChain Team** - For the incredible document processing framework
- **Ollama Community** - For making local LLMs accessible
- **Streamlit** - For the amazing web app framework
- **ChromaDB** - For efficient vector storage and retrieval

## 📞 Support

Having issues? Here's how to get help:
- 🐛 [Report bugs](https://github.com/Tharun007-TK/docuchat/issues)
- 💡 [Request features](https://github.com/Tharun007-TK/docuchat/issues)
- 📧 Email: support@docuchat.dev

---

**Made with ❤️ by the DocuChat Team**

*Transform your documents. Elevate your conversations.*
