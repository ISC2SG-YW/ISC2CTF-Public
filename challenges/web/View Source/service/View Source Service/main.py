from flask import Flask, request, render_template , redirect, url_for,render_template_string
import os 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/view', methods = ["GET"])
def view():
    file_name = request.args.get('file_name')
    if not file_name:
        return redirect(url_for('index'))
    if not file_name.endswith('.py'):
        return render_template('error.html')
    
    file_path = f"{file_name.split('.')[0]}.py"
    
    if not os.path.exists(file_path):
        return render_template('error.html')
    
    with open(file_path, "r") as f:
        content = f.read()
    template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>View File for {file_name}</title>
        <link rel="stylesheet" href="/static/style.css">
        <link rel="stylesheet" href="/static/view.css">
    </head>
    <body>
        <h1>Code Preview</h1>
        <pre class = "code_preview">{content}</pre>
    </body>
    </html>
    """
    return render_template_string(template)

if __name__ == '__main__':
    app.run()