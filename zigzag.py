def convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s

    rows = []

    for _ in range(num_rows):
        rows.append([])
    count = 0

    for letter in s:
        if count == 0:
            isDown = True
        elif count == num_rows - 1:
            isDown = False
        rows[count].append(letter)
        if isDown:
            count += 1
        else: count -= 1
    output = ""

    for row in rows:
        output += "".join(row)
    return output