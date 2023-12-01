import os
import markdown 
from file_monitor import FileMonitor
class MarkdownObserver:
    input_folder:str
    input_file:str
    output_file:str
    observer: FileMonitor()
    
    def updateFilesFromSettings(self):
        self.input_file = os.path.join(CurrentSettings.inputFolder, CurrentSettings.inputFile)  # source markdown    
        self.output_file = CurrentSettings.outputFile  # target
    def convert_markdown_to_html(self):
        with open(self.input_file, 'r', encoding='utf-8', errors='ignore') as file:
            markdown_text = file.read()
        html = markdown.markdown(markdown_text)
        
        if(os.path.exists(self.output_file)):
            if(CurrentSettings.verbose):
                print("deleting output file")
            os.remove(self.output_file)
        with open(self.output_file, 'w', encoding='utf-8') as file:
            file.write(html)
    def startMonitor(self): 
        self.fileMonitor.folder = self.input_file
        self.fileMonitor.filepath = self.input_file
        print (self.fileMonitor.filepath)
        self.fileMonitor.action = self.convert_markdown_to_html
        self.fileMonitor.startMonitor()
        
Current: MarkdownObserver = MarkdownObserver() 