<!-- item_details.tpl -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ item['title'] }} Details</title>
</head>
<body>
    <h1>{{ item['title'] }} Details</h1>
    <p>Title: {{ item['title'] }}</p>
    <p>Author: {{ item['author'] }}</p>
    <p>Genre: {{ item['genre'] }}</p>
    <!-- Add ratings or any other details you want to display -->
    <a href="/items/{{ item['id'] }}/update">Update Item</a>
    <a href="/items/{{ item['id'] }}/delete">Delete Item</a>
    <a href="/items">Back to Items</a>
</body>
</html>
