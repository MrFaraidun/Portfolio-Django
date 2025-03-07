from django.http import HttpResponse

def portfolio(request):
    html_content = """
    <html>
    <head>
        <title>My Portfolio</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            header {
                background-color: #333;
                color: white;
                padding: 20px 0;
                text-align: center;
            }
            .profile {
                text-align: center;
                margin-top: 20px;
            }
            .profile img {
                width: 150px;
                height: 150px;
                border-radius: 50%;
                object-fit: cover;
            }
            section {
                padding: 20px;
            }
            table {
                width: 80%;
                margin: 20px auto;
                border-collapse: collapse;
            }
            table, th, td {
                border: 1px solid #ddd;
                text-align: left;
                padding: 8px;
            }
            th {
                background-color: #333;
                color: white;
            }
            footer {
                background-color: #333;
                color: white;
                text-align: center;
                padding: 10px 0;
                width: 100%;
                bottom: 0;
            }
            .contact {
                text-align: center;
                margin-top: 20px;
            }
            .contact p {
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to My Portfolio</h1>
            <p>Here you can find my work and contact details.</p>
        </header>

        <!-- Profile Section -->
        <div class="profile">
            <h2>Faraidun Bahaden</h2>
            <p>Web Developer | Programmer </p>
        </div>

        <!-- Project Table -->
        <section>
            <h2>My Projects</h2>
            <table>
                <tr>
                    <th>Project Name</th>
                    <th>Description</th>
                </tr>
                <tr>
                    <td>Flashcard App</td>
                    <td>A web application for creating and reviewing flashcards to improve learning.</td>
                </tr>
                <tr>
                    <td>To-Do List</td>
                    <td>A simple app for managing daily tasks, allowing you to add, edit, and delete tasks.</td>
                </tr>
                <tr>
                    <td>Car Shop</td>
                    <td>An online store for buying and selling cars, with options to filter by type, price, and brand.</td>
                </tr>
            </table>
        </section>

        <!-- Contact Section -->
        <div class="contact">
            <h3>Contact Me</h3>
            <p>Email: faraidun@gmail.com</p>
            <p>Phone: 964+ 0770 255 6650</p>
        </div>

        <footer>
            <p>&copy; 2025 My Portfolio</p>
        </footer>
    </body>
</html>
    """
    return HttpResponse(html_content)