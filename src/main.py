from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import QPixmap, QFont, QIcon
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QLabel, 
                               QMainWindow, QPushButton, QSpinBox, QTabWidget, QWidget, 
                               QFileDialog,QMessageBox)

from ui import Ui_MainWindow
from pathlib import Path
from PIL import Image, ImageDraw
from io import BytesIO

import os, sys, freetype, logging
import generator


# Logging
log_file_path = "atlas_generator.log"
logging.basicConfig(level=logging.INFO,
                    filename=log_file_path,
                    format="{asctime} - {levelname} - {message}",
                    style="{",
                    datefmt="%Y-%m-%d %H:%M:%S",           
)

# Setting up icon for the application
basedir = os.path.dirname(__file__)

try:
    from ctypes import windll
    myappid = 'font.atlas.generator'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

class MainWindow(QMainWindow):
    # Main Window Class
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.selected_font = str()
        self.generated_image = None
        self.generated_mapping = None
        
        # Connecting buttons to functions
        self.ui.SelectFontButton.clicked.connect(self.open_file_dialog)
        self.ui.GenerateButton.clicked.connect(self.generate_atlas)
        self.ui.ExportButton.clicked.connect(self.export_atlas)
        self.ui.OpenOutputFolderButton.clicked.connect(self.open_output_folder)
        self.ui.ExitButton.clicked.connect(self.exit_application)
        
        # Define and create output folder if it doesn't exist
        self.output_folder = "outputs\\"
        self.output = Path(self.output_folder)
        self.output.mkdir(parents=True, exist_ok=True)
        logging.info(f"Checking/Creating output folder: {self.output}.")
        
        # Define and create font folder if it doesn't exist
        self.fonts_folder = "fonts\\"
        self.fonts_folder = Path(self.fonts_folder)
        self.fonts_folder.mkdir(parents=True, exist_ok=True)
        logging.info(f"Checking/Creating font folder: {self.fonts_folder}.")
    
    # Function to exit the application
    def exit_application(self):
        logging.info("Application Closed.")
        QCoreApplication.instance().quit()
    
    # Function to open file dialog
    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Font Files (*.ttf *.otf)")
        if file_dialog.exec():
            self.selected_font = file_dialog.selectedFiles()
            file_names = [Path(file_path).stem for file_path in self.selected_font]
            font_selected_text = ", ".join(file_names)
            self.ui.SelectFontButton.setText(font_selected_text)
            logging.info(f"Font files selected: {self.selected_font}")
    
    # Function to generate atlas and mapping
    def generate_atlas(self):
        warning_box = QMessageBox()
        warning_box.setIcon(QMessageBox.Information)
        if self.selected_font:
            logging.info(f"Generating atlas for font: {self.selected_font}.")
            
            # Generate the atlas and mapping, saved to memory
            generated_atlas, generated_mapping = generator.process_fonts(self.selected_font, font_size=self.ui.FontSize.value(), character_padding=self.ui.FontPaddingSize.value())
            if generated_atlas and generated_mapping:
                self.generated_image = generated_atlas
                self.generated_mapping = generated_mapping
                
                # Load the generated atlas from memory to preview
                preview_atlas = QPixmap()
                preview_atlas.loadFromData(generated_atlas.read())
                self.ui.Preview.setPixmap(preview_atlas)
                self.ui.Preview.setText("")
                
                logging.info("Atlas Generated Successfully.")
                warning_box.setText("Atlas Generated Successfully")
                warning_box.exec()
            else:
                logging.error("Error Generating Atlas. Processing Fonts Failed.")
                warning_box.setIcon(QMessageBox.Warning)
                warning_box.setText("Error Generating Atlas")
                warning_box.exec()
        else:
            logging.error("Font File Not Selected.")
            warning_box.setText("Please Select Font File")
            warning_box.exec()

    # Function to export generated atlas
    def export_atlas(self):
        warning_box = QMessageBox()
        warning_box.setIcon(QMessageBox.Information)
        if self.generated_image and self.generated_mapping:
            logging.info("Exporting Atlas to output folder...")
            
            # Determine the font file name to use as the output file name
            for font_path in self.selected_font:
                font_file_name = Path(font_path).stem
                atlas_output = self.output / f"{font_file_name}.png"
                mapping_output = self.output / f"{font_file_name}.ini"
            
            # Save the generated atlas and mapping to disk
            with open(atlas_output, "wb") as f:
                f.write(self.generated_image.getbuffer())
            logging.info(f"Saved atlas: {atlas_output}.")
            with open(mapping_output, "wb") as f:
                f.write(self.generated_mapping.getbuffer())
            logging.info(f"Saved character mapping: {mapping_output}.")
            
            # Close the generated atlas and mapping
            self.generated_image.close()
            self.generated_mapping.close()
            
            logging.info("Atlas Exported Successfully.")
            warning_box.setText("Atlas Exported Successfully")
            warning_box.exec()
        else:
            logging.error("No Generated Atlas To Export.")
            warning_box.setText("No Generated Atlas To Export!")
            warning_box.exec()

    # Function to open output folder
    def open_output_folder(self):
        os.startfile(self.output)
        logging.info(f"Opening output folder...")

if __name__== "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Font Atlas Generator")
    window.setWindowIcon(QIcon(os.path.join(basedir, "Icon.ico")))
    window.show()
    logging.info("Application Started.")
    sys.exit(app.exec())
        