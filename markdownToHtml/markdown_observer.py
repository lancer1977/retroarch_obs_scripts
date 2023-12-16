import os
import markdown 
from file_monitor import FileMonitor 
from settings import CurrentSettings

class MarkdownObserver:
    input_folder:str
    input_file:str
    output_file:str
    observer: FileMonitor  

    def update(self, input_file, input_folder, output_file):
        self.input_folder = input_folder
        self.input_file = os.path.join(input_folder, input_file)  # source markdown    
        self.output_file = output_file # target
        
    def updateDirect(self):
        self.update(CurrentSettings.inputFile,CurrentSettings.inputFolder, CurrentSettings.outputFile)
        
    def convert_markdown_to_html(self):
        if(os.path.exists(self.input_file) == False): return;
        with open(self.input_file, 'r', encoding='utf-8', errors='ignore') as file:
            markdown_text = file.read()
        html = markdown.markdown(markdown_text)
                
        if(os.path.exists(self.output_file)): 
            os.remove(self.output_file)
        with open(self.output_file, 'w', encoding='utf-8') as file:
            file.write(html)
            
    def startMonitor(self):
        if(CurrentSettings.verbose):
            print (self.input_file) 
        self.refresh()
        self.observer.folder = self.input_folder
        self.observer.filepath = self.input_file
        self.observer.action = self.convert_markdown_to_html
        self.observer.startMonitor()
        
    def refresh(self):
        self.updateDirect()
        self.convert_markdown_to_html()
        
    def stopMonitor(self):
        self.observer.stop()

    def __init__(self):
        self.observer = FileMonitor()
        self.input_folder = ""
        self.input_file = ""
        self.output_file = ""
        self.refresh()
