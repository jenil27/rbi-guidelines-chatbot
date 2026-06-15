import gradio as gr
from rag_pipeline import build_qa_chain

qa_chain = None

def process_pdf(pdf_file):
    global qa_chain
    if pdf_file is None:
        return "⚠️ Please upload a PDF first."
    with open(pdf_file.name, "rb") as f:
        pdf_bytes = f.read()
    qa_chain = build_qa_chain(pdf_bytes)
    return "✅ PDF processed! You can now ask questions."

def chat(user_input, chat_history):
    global qa_chain
    if chat_history is None:
        chat_history = []
    if qa_chain is None:
        chat_history = chat_history + [{"role": "user", "content": user_input}, {"role": "assistant", "content": "⚠️ Please upload and process a PDF first."}]
        return "", chat_history
    if not user_input.strip():
        return "", chat_history
    try:
        response = qa_chain({"question": user_input})
        answer = response["answer"]
    except Exception as e:
        answer = f"❌ Error: {str(e)}"
    chat_history = chat_history + [{"role": "user", "content": user_input}, {"role": "assistant", "content": answer}]
    return "", chat_history

def clear_chat():
    global qa_chain
    qa_chain = None
    return [], "🗑️ Cleared. Upload a new PDF to start again."

def clear_chat():
    global qa_chain
    qa_chain = None
    return [], "🗑️ Cleared. Upload a new PDF to start again."

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 📄 RBI Guidelines Chatbot")
    gr.Markdown("Upload any RBI PDF and ask questions about it.")

    with gr.Row():
        with gr.Column(scale=1):
            pdf_input = gr.File(
                label="Upload PDF",
                file_types=[".pdf"]
            )
            upload_btn = gr.Button("Process PDF", variant="primary")
            status = gr.Textbox(label="Status", interactive=False)
            clear_btn = gr.Button("Clear Chat", variant="secondary")

        with gr.Column(scale=2):
            chatbot = gr.Chatbot(height=500)
            msg = gr.Textbox(
                label="Ask a question",
                placeholder="e.g. What is NBFC?"
            )

    upload_btn.click(fn=process_pdf, inputs=[pdf_input], outputs=[status])
    msg.submit(fn=chat, inputs=[msg, chatbot], outputs=[msg, chatbot])
    clear_btn.click(fn=clear_chat, outputs=[chatbot, status])

demo.launch()