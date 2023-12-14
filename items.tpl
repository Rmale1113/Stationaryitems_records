<!-- books.tpl -->
<!DOCTYPE html>
<html>
<head>
    <title>items</title>
</head>
<body>
    <h1>items</h1>
    <ul>
        % for book in items:
            <li>
                <a href="/items/{{ item['pen'] }}">{{ item['book'] }}</a>
            </li>
        % end
    </ul>
    <a href="/books/add">Add a item</a>
</body>
</html>
