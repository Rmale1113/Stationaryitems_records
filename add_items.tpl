
<!DOCTYPE html>
<html>
<head>
    <title>Add items</title>
</head>
<body>
    <h1>Add items</h1>
    <form action="/items/add" method="post">
        <label for="title">Title:</label>
        <input type="text" id="book" name="book" required><br>

        <label for="author">Author:</label>
        <input type="text" id="pen" name="pen" required><br>

        <label for="genre">Genre:</label>
        <input type="text" id="pencil" name="pencil" required><br>

        <input type="submit" value="Add items">
    </form>
    <a href="/books">Back to items</a>
</body>
</html>
