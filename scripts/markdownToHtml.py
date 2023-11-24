# Use with https://obsproject.com/forum/resources/xobsbrowserautorefresh-timed-automatic-browser-source-refreshing.1677/

import markdown
import time
import os
def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
        markdown_text = file.read()

    html = markdown.markdown(markdown_text)
    if(os.path.exists(output_file)):
        print("deleting output file")
        os.remove(output_file)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html)

if __name__ == "__main__":
    input_file = "C:\\Users\\lance\\SynologyDrive\\obsidian\\Projects\\API\\Learning\\Goals.md"  # source markdown
    output_file = "D:\\obs_assets\\goals.html"  # target
    while True:
        try:
            convert_markdown_to_html(input_file, output_file)
        except:
            print("Error converting markdown to html")
        print("sleeping 1 seconds")
        time.sleep(1)
    
    