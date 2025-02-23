from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Jenkins CI/CD App</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #f8f9fa;
            }
            h1 {
                color: #343a40;
            }
            .footer {
                position: fixed;
                width: 100%;
                bottom: 0;
            }
        </style>
    </head>
    <body>

        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Jenkins CI/CD</a>
            </div>
        </nav>

        <div class="container mt-5 text-center">
            <h1 class="display-4">Hello, Jenkins CI/CD Pipeline - Enhanced!</h1>
            <p class="lead">This Flask app is now more dynamic and clean!</p>
            <button class="btn btn-primary mt-3" onclick="refreshPage()">Refresh</button>
        </div>

        <footer class="footer bg-dark text-white text-center py-3">
            © 2025 Jenkins CI/CD Demo | Built with Flask & Bootstrap
        </footer>

        <script>
            function refreshPage() {
                location.reload();
            }
        </script>

    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

