
<!-- item_details.tpl -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ item['Additems'] }} Details</title>
</head>
<body>
    <h1>{{ item['Additems'] }} Details</h1>
    <p>Title: {{ item['book'] }}</p>
    <p>Author: {{ item['pen'] }}</p>
    <p>Genre: {{ item['pencil'] }}</p>
    <!-- Add ratings or any other details you want to display -->
    <a href="/items/{{ item['id'] }}/update">Update Item</a>
    <a href="/items/{{ item['id'] }}/delete">Delete Item</a>
    <a href="/items">Back to Items</a>
</body>
</html>
