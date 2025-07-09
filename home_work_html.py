import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    text = ''
    inside_tag = False

    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            text += char

    lines = text.splitlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    cleaned_text = '\n'.join(non_empty_lines)


    with codecs.open(result_file, 'w', 'utf-8') as out:
        out.write(cleaned_text)


delete_html_tags('draft.html')