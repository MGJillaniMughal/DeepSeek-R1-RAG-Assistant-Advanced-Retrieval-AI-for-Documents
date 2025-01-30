# DeepSeek-R1 RAG Assistant – Advanced Retrieval AI for Documents

## 🚀 Overview
**DeepSeek-R1 RAG Assistant** is a cutting-edge **Retrieval-Augmented Generation (RAG) system** that enables users to upload PDFs, process their content, and interact with them through conversational queries. The system leverages **Groq's deepseek-r1-distill-llama-70b LLM model**, combined with **FAISS vector search** and **OpenAI embeddings**, to efficiently deliver accurate and contextual responses.

---

## ✨ Key Features
- 📂 **PDF Upload & Processing**: Extracts text from multiple PDF documents and stores it in a FAISS vector database.
- 🔍 **Advanced RAG Workflow**: Ensures reliable and context-aware responses by combining retrieval with generative capabilities.
- 💬 **Conversational Querying**: Engage in a dynamic question-answering session based on document content.
- ✅ **Accurate & Trustworthy Responses**: The AI assistant follows structured reasoning, avoiding hallucinations and ensuring factual accuracy.
- 🖥️ **User-Friendly Streamlit Interface**: Interactive, lightweight UI for seamless document interaction.
- 🛠️ **Robust Backend**: Powered by **LangChain**, **FAISS**, **OpenAI Embeddings**, and **Groq LLM**.

---

## 🏗️ Technology Stack

### Backend
- **LangChain** – Framework for LLM-based workflows.
- **FAISS** – High-performance vector database for fast similarity search.
- **OpenAI Embeddings** – Converts extracted text into meaningful embeddings.
- **Groq deepseek-r1-distill-llama-70b** – Powers conversational AI.

### Frontend
- **Streamlit** – Simplified dashboard for document interaction.

### Deployment
- **Environment Management** via `.env` variables.

---

## 🔧 Installation & Setup

### Prerequisites
Ensure you have the following installed:
- **Python 3.9+**
- **pip**
- **Groq API Key** (Required for LLM functionality)

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/MGJillaniMughal/DeepSeek-R1-RAG-Assistant-Advanced-Retrieval-AI-for-Documents.git
   cd DeepSeek-R1-RAG-Assistant-Advanced-Retrieval-AI-for-Documents
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Create a `.env` file in the root directory.
   - Add your Groq API key:
     ```env
     GROQ_API_KEY=your-groq-api-key
     ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

---

## 📘 Usage

### 1️⃣ Uploading and Processing PDFs
- Use the **sidebar** to upload PDF documents.
- Click **Process Documents** to extract and index content into FAISS.
- Wait for the **success message**, indicating the PDFs have been processed.

### 2️⃣ Conversational Querying
- Type your question into the chat input field.
- The AI assistant retrieves relevant context and provides accurate answers.

---

## 📁 Project Structure
```
.
├── app.py                     # Main Streamlit application
├── requirements.txt           # Required Python libraries
├── .env                       # Environment variables (Groq API key)
├── faiss_index/               # Folder containing the FAISS vector store
└── README.md                  # Project documentation
```

---

## 🔥 Example Use Cases

### 📄 Research Assistance
Upload research papers and ask for summarized insights.
**Example:** _"What are the key takeaways from page 5?"_

### ⚖️ Legal Document Parsing
Extract important clauses from contracts and agreements.
**Example:** _"What is the non-disclosure clause in this contract?"_

### 📚 Educational Support
Interact with textbooks or study materials for better comprehension.
**Example:** _"Explain the concept of retrieval-augmented generation."_

---

## 🎯 Future Enhancements
- 📝 **Multi-File Support**: Handle Word, Excel, and plain text files.
- 🛠️ **Customizable Chunking**: User-configurable text chunking for better indexing.
- ☁️ **Cloud Storage Integration**: Save processed data for large-scale applications.
- 🖼️ **Multimodal Support**: Include image and diagram-based document processing.

---

## 🤝 Acknowledgments
- **Groq** – For the deepseek-r1-distill-llama-70b model powering conversational capabilities.
- **LangChain** – For building structured LLM workflows.
- **FAISS** – For efficient similarity search and retrieval.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 📞 Contact
For inquiries or collaboration opportunities:
- **👤 Name**: Muhammad Ghulam Jillani (Jillani SoftTech)
- **📧 Email**: m.g.jillani123@gmail.com
- **📌 LinkedIn**: [Jillani SoftTech](https://www.linkedin.com/in/jillanisofttech/)
- **🐙 GitHub**: [MGJillaniMughal](https://github.com/MGJillaniMughal)

🚀 **Empowering AI solutions with Jillani SoftTech!**
