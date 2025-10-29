<!DOCTYPE html>
<html>
<head>
    <title>Add Book</title>
</head>
<body>
    <h1>Add New Book</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Add Book</button>
    </form>
    <a href="{% url 'list_books' %}">Back to all books</a>
</body>
</html>
