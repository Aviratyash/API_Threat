import gradio as gr
import joblib
import hashlib

sql_vectorizer = joblib.load("tfidf_vectorizer.pkl")
sql_model = joblib.load("SQLi_Detection_Model.pkl")
xss_vectorizer = joblib.load("tfidf_vectorizer2.pkl")
xss_model = joblib.load("XSS_Detection_Model.pkl")


user_database = {}


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def detect_injection(text):
    sql_flag = sql_model.predict(sql_vectorizer.transform([text]))[0]
    xss_flag = xss_model.predict(xss_vectorizer.transform([text]))[0]
    return sql_flag, xss_flag


def handle_register(username, password):
    if username in user_database:
        return "❌ Username already exists!"

    sql_flag, xss_flag = detect_injection(username + " " + password)

    if sql_flag:
        return "🚨 SQL Injection Detected in Registration"
    if xss_flag:
        return "🚨 XSS Attack Detected in Registration"

    user_database[username] = hash_password(password)
    return "✅ User Registered Successfully"


def handle_login(username, password):
    sql_flag, xss_flag = detect_injection(username + " " + password)

    if sql_flag:
        return "🚨 SQL Injection Detected in Login"
    if xss_flag:
        return "🚨 XSS Attack Detected in Login"

    hashed_pw = hash_password(password)
    if username in user_database and user_database[username] == hashed_pw:
        return "✅ Login Successful!"
    else:
        return "❌ Invalid username or password"

with gr.Blocks() as demo:
    gr.Markdown("## 🛡️ Secure Login System with SQL/XSS Detection (Simulated FastAPI Backend)")

    with gr.Tab("🔐 Register"):
        reg_user = gr.Textbox(label="Username")
        reg_pass = gr.Textbox(label="Password", type="password")
        reg_btn = gr.Button("Register")
        reg_out = gr.Textbox(label="Registration Response")
        reg_btn.click(handle_register, inputs=[reg_user, reg_pass], outputs=reg_out)

    with gr.Tab("🔑 Login"):
        login_user = gr.Textbox(label="Username")
        login_pass = gr.Textbox(label="Password", type="password")
        login_btn = gr.Button("Login")
        login_out = gr.Textbox(label="Login Response")
        login_btn.click(handle_login, inputs=[login_user, login_pass], outputs=login_out)


gr.close_all()

# Launch
demo.launch(share=True)
