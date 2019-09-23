# Importing Modules

import sys 
import os
import subprocess
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import time
import mammoth
# Main Class
import speech_recognition as sr
msg= """Hello User! \n This is simple text editor app made by Ryan Antony in Association \n with CID An Education Hub
            and Team
            We Hope You are enjoying the app.\n For any help you can visit our facebook page - fb.me/cideduhub\n
            or on youtube - https://www.youtube.com/c/cidaneducationhub """ # You can edit it

# Inheriting the QMAINWINDOW class form QTGUI

class Window(QtGui.QMainWindow):
    
    def __init__(self):

        super(Window, self).__init__()

        # Defining Properties of Editor

        self.setWindowIcon(QtGui.QIcon("icons/text-editor.png"))
        self.setWindowTitle('TypeIt Mini Text Editor')
        self.statusbar= self.statusBar()
        self.statusbar.setStyleSheet("QStatusBar{background:#C71585;color:white}")
        self.statusbar.showMessage("Qt Mini text Editor Application Launched!!")
        
        self.setGeometry(50, 50, 640, 300)
        self.filename = ""
        self.wrap_mode = False
        self.saved_data = ""
        self.changesSaved = True

        self.menu()
        self.home()
        self.show()

    def menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        edit = mainMenu.addMenu('Edit')
        insertMenu = mainMenu.addMenu('Insert')
        view = mainMenu.addMenu('View')
        formatMenu = mainMenu.addMenu('Format')
        helpMenu = mainMenu.addMenu('Help')




        newFileAction = QtGui.QAction(QtGui.QIcon("icons/new.png"),'New', self)
        newFileAction.triggered.connect(self.new_file)
        newFileAction.setShortcut('Ctrl+N')
        newFileAction.setStatusTip('Open a File')

        openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"),"Open ",self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open a File')
        openAction.triggered.connect(self.open_File)

        saveFileAction = QtGui.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
        saveFileAction.setStatusTip("Save document")
        saveFileAction.setShortcut("Ctrl+S")
        saveFileAction.triggered.connect(self.File_save)

        saveAsFileAction = QtGui.QAction(QtGui.QIcon("icons/Save-as.png"),"Save As...",self)
        saveAsFileAction.setStatusTip("Save document")
        saveAsFileAction.setShortcut("Ctrl+Shift+S")
        saveAsFileAction.triggered.connect(self.File_save_as)
#image insert
        imageAction = QtGui.QAction(QtGui.QIcon("icons/image.png"),"Insert image",self)
        imageAction.setStatusTip("Insert image")
        imageAction.setShortcut("Ctrl+Shift+I")
        imageAction.triggered.connect(self.insertImage)
#insert from voice
        voiceAction = QtGui.QAction(QtGui.QIcon("icons/mike.png"),"Speech2Text",self)
        voiceAction.setStatusTip("Insert from voice")
        voiceAction.setShortcut("Ctrl+Shift+v")
        voiceAction.triggered.connect(self.Mic)


        exitAction = QtGui.QAction(QtGui.QIcon('icons/Exit.png'), 'Exit', self)
        exitAction.triggered.connect(self.exit_fuction)
        exitAction.setShortcut('Ctrl+Q')
        
        printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"),"Print document",self)
        printAction.setStatusTip("Print document")
        printAction.setShortcut("Ctrl+P")
        printAction.triggered.connect(self.Print)
 
        dateAction = QtGui.QAction(QtGui.QIcon("icons/Calender.png"),"Date",self)
        dateAction.setStatusTip("Insert date")
        dateAction.setShortcut("Ctrl+d")
        dateAction.triggered.connect(self.date)

        timeAction = QtGui.QAction(QtGui.QIcon("icons/Date_and_time.png"),"Time",self)
        timeAction.setStatusTip("Insert time")
        timeAction.setShortcut("Ctrl+t")
        timeAction.triggered.connect(self.time)


       
       

        cutAction = QtGui.QAction(QtGui.QIcon("icons/cut.png"),"Cut to clipboard",self)
        cutAction.setStatusTip("Delete and copy text to clipboard")
        cutAction.setShortcut("Ctrl+X")
        cutAction.triggered.connect(self.Cut)
       
        copyAction = QtGui.QAction(QtGui.QIcon("icons/copy.png"),"Copy to clipboard",self)
        copyAction.setStatusTip("Copy text to clipboard")
        copyAction.setShortcut("Ctrl+C")
        copyAction.triggered.connect(self.Copy)
 
        pasteAction = QtGui.QAction(QtGui.QIcon("icons/paste.png"),"Paste from clipboard",self)
        pasteAction.setStatusTip("Paste text from clipboard")
        pasteAction.setShortcut("Ctrl+V")
        pasteAction.triggered.connect(self.Paste)
 
        undoAction = QtGui.QAction(QtGui.QIcon("icons/undo.png"),"Undo last action",self)
        undoAction.setStatusTip("Undo last action")
        undoAction.setShortcut("Ctrl+Z")
        undoAction.triggered.connect(self.Undo)

        redoAction = QtGui.QAction(QtGui.QIcon("icons/redo.png"),"Redo last undone thing",self)
        redoAction.setStatusTip("Redo last undone thing")
        redoAction.setShortcut("Ctrl+Y")
        redoAction.triggered.connect(self.Redo)

        previewAction = QtGui.QAction(QtGui.QIcon("icons/if_Preview_.png"),"Page view",self)
        previewAction.setStatusTip("Preview page before printing")
        previewAction.setShortcut("Ctrl+Shift+P")
        previewAction.triggered.connect(self.PageView)

        pdfAction = QtGui.QAction(QtGui.QIcon("icons/ACP_PDF.png"),"Save To PDF File",self)
        pdfAction.setStatusTip("Save PDF to Document")
        pdfAction.triggered.connect(self.SavetoPDF)
        
        self.wrapAction = QtGui.QAction("WordWrap",self)  
        self.wrapAction.triggered.connect(self.word_wrap)

        fontAction = QtGui.QAction(QtGui.QIcon("icons/Font.png"),'Font', self)
        fontAction.triggered.connect(self.font_dialog)
        fontAction.setStatusTip('SetTextTont')

        colorAction = QtGui.QAction(QtGui.QIcon("icons/Color.png"),'Color', self)
        colorAction.triggered.connect(self.colorDialog)
        colorAction.setStatusTip('SetTextColor')
        
        numberedAction = QtGui.QAction(QtGui.QIcon("icons/number.png"),"Insert numbered List",self)
        numberedAction.setStatusTip("Insert numbered list")
        numberedAction.setShortcut("Ctrl+Shift+L")
        numberedAction.triggered.connect(self.numberList)

        boldAction = QtGui.QAction(QtGui.QIcon("icons/bold.png"),"Bold",self)
        boldAction.triggered.connect(self.bold)

        italicAction = QtGui.QAction(QtGui.QIcon("icons/italic.png"),"Italic",self)
        italicAction.triggered.connect(self.italic)

        underlAction = QtGui.QAction(QtGui.QIcon("icons/underline.png"),"Underline",self)
        underlAction.triggered.connect(self.underline)

        alignLeft = QtGui.QAction(QtGui.QIcon("icons/align-left.png."),"Align left",self)
        alignLeft.triggered.connect(self.alignLeft)
 
        alignCenter = QtGui.QAction(QtGui.QIcon("icons/align-center.png"),"Align center",self)
        alignCenter.triggered.connect(self.alignCenter)
 
        alignRight = QtGui.QAction(QtGui.QIcon("icons/align-right.png"),"Align right",self)
        alignRight.triggered.connect(self.alignRight)
 
        alignJustify = QtGui.QAction(QtGui.QIcon("icons/align-justify.png"),"Align justify",self)
        alignJustify.triggered.connect(self.alignJustify)

        bulletAction = QtGui.QAction(QtGui.QIcon("icons/bullet.png"),"Insert Bullet List",self)
        bulletAction.triggered.connect(self.BulletList) 

        helpAction = QtGui.QAction(QtGui.QIcon("icons/about.png"),"More Info",self)
        helpAction.triggered.connect(self.help_menu) 


        self.toolbar2Height = 20 # added by Patrick
        self.fontFamily = QtGui.QFontComboBox(self)
        self.fontFamily.setMinimumHeight(self.toolbar2Height) # added by Patrick
        self.fontFamily.currentFontChanged.connect(self.FontFamily)
 
        self.fontSize = QtGui.QComboBox(self)
        self.fontSize.setMinimumHeight(self.toolbar2Height)
        self.fontSize.setEditable(True)
        self.fontSize.setMinimumContentsLength(3)
        self.fontSize.activated.connect(self.FontSize)
        flist = [6,7,8,9,10,11,12,13,14,15,16,18,20,22,24,26,28,32,36,40,44,48,
                 54,60,66,72,80,88,96]
         
        for i in flist:
            self.fontSize.addItem(str(i))
        
        
        self.toolbar = self.addToolBar("Options")
        # self.toolbar.setMaximumWidth(500)
        self.toolbar.setFloatable(False)
        self.toolbar.setMovable(False)
        self.toolbar.addSeparator()
        self.toolbar.setIconSize(QSize(16,16))
        self.toolbar.addAction(newFileAction)
        self.toolbar.addAction(openAction)
        self.toolbar.addAction(saveFileAction)
        self.toolbar.addAction(saveAsFileAction)
       
        self.toolbar.addAction(pdfAction)
        self.toolbar.addAction(printAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(undoAction)
        self.toolbar.addAction(redoAction)
        self.toolbar.addAction(cutAction)
        self.toolbar.addAction(copyAction)
        self.toolbar.addAction(pasteAction)
        
        self.toolbar.addAction(boldAction)
        self.toolbar.addAction(italicAction)
        self.toolbar.addAction(underlAction)
        self.toolbar.addAction(alignLeft)
        self.toolbar.addAction(alignCenter)
        self.toolbar.addAction(alignRight)
        self.toolbar.addAction(alignJustify)
        self.toolbar.addAction(bulletAction)
        self.toolbar.addSeparator()
        
        self.addToolBarBreak()
        # by Patrick. I broke up the toolbar and created a second tool bar
        self.toolbar2 = self.addToolBar('FontToolbar')
        self.toolbar2.setFloatable(False)
        self.toolbar2.setMovable(False)
        self.toolbar2.setMinimumHeight(self.toolbar2Height)
        self.toolbar2.addSeparator()
        self.toolbar2.addWidget(self.fontFamily)
        self.toolbar2.addWidget(self.fontSize)
        self.toolbar2.addSeparator()
        self.toolbar2.addAction(imageAction)
        self.toolbar2.addAction(voiceAction) #voice action in toolbar
        self.toolbar2.addSeparator()



        fileMenu.addAction(newFileAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveFileAction)
        fileMenu.addAction(saveAsFileAction)
        fileMenu.addAction(printAction)
        fileMenu.addAction(previewAction)
        fileMenu.addAction(pdfAction)
        fileMenu.addAction(exitAction)


        insertMenu.addAction(dateAction)
        insertMenu.addAction(timeAction)
        insertMenu.addAction(imageAction)
        insertMenu.addAction(voiceAction) #voice recognizer action
        edit.addSeparator()
        edit.addAction(undoAction)
        edit.addAction(redoAction)
        edit.addAction(cutAction)
        edit.addAction(copyAction)
        edit.addAction(pasteAction)
        view.addAction(self.wrapAction)
        view.addAction(numberedAction)

        formatMenu.addAction(fontAction)
        formatMenu.addAction(colorAction)
        formatMenu.addAction(boldAction)
        formatMenu.addAction(italicAction)
        formatMenu.addAction(underlAction)
        formatMenu.addAction(alignLeft)
        formatMenu.addAction(alignCenter)
        formatMenu.addAction(alignRight)
        formatMenu.addAction(alignJustify)
        formatMenu.addAction(bulletAction)
        formatMenu.addAction(fontAction)
        formatMenu.addAction(colorAction)
        helpMenu.addAction(helpAction)


    
    def home(self):

        self.tab = QtGui.QTabWidget(self)
        self.tab.setTabsClosable(True)
        self.tab.tabCloseRequested.connect(self.closeTab)
        self.tab.setTabShape(QtGui.QTabWidget.Triangular)

        self.textEdit = QtGui.QTextEdit()
        self.textEdit.setUndoRedoEnabled(True)
        self.textEdit.setAcceptRichText(False)
        self.setStyleSheet("QTextEdit{background-color: #ffffff}")
        self.textEdit.setStyleSheet("QTextEdit{font-size:20px;color: #000000}")
        self.textEdit.setWordWrapMode(QtGui.QTextOption.NoWrap) 
        self.textFont = QtGui.QFont("Consolas",15,) 
        self.textEdit.setTabStopWidth(12)
        self.textEdit.setFont(self.textFont)
        # self.setCentralWidget(self.textEdit)

        self.setCentralWidget(self.tab)
        self.tab.addTab(self.textEdit, "New Tab")

    def closeTab(self):
        widget = self.tab.currentWidget()
        if widget:
            widget.deleteLater()
        self.tab.removeTab(self.tab.currentIndex())
       

        #if self.tab.count() ==0: # CLose Application if all the tabs are closed!
          #  sys.exit()             #uncomment if u want to close when tabs are NULL


    def new_file(self):
        self.textEdit = QtGui.QTextEdit()
        self.textEdit.setUndoRedoEnabled(True)
        self.textEdit.setAcceptRichText(False)
        self.setStyleSheet("QTextEdit{background-color: #ffffff}")
        self.textEdit.setStyleSheet("QTextEdit{font-size:20px;color:#000000}")
        self.textEdit.setWordWrapMode(QtGui.QTextOption.NoWrap)
        self.textFont = QtGui.QFont("Consolas",15,)
        self.textEdit.setTabStopWidth(12)
        self.textEdit.setFont(self.textFont)
        self.tab.addTab(self.textEdit, "New Tab")
        self.tab.setCurrentIndex(self.tab.count()-1)
        
        
        
    def open_File(self):
        # Change textEdit to QWebview
        # Read contents of the pdf file
        # SetContent() of the pdf to the QWebView

        name = QtGui.QFileDialog.getOpenFileName(self,'Open File', os.getenv('HOME'),
                                                 "All files(*.*);;(*.pdf);;txt(*.txt);;;writer(*.writer)")
        if os.path.splitext(name)[1] == ".pdf":
            
            
            # This below line opens our pdfViewer.exe file which is selected from PopUp file picker
            subprocess.check_call([r"pdf complete\pdfvista.exe", name])

            
        else:
            if name:
                with open(name, 'r') as stream:
                    if self.tab.count() ==0:
                        self.new_file()
                    self.opendFileText = stream.read()
                    self.textEdit.setText(self.opendFileText)
                self.current_save_file_path = name

       
        self.setWindowTitle(name + "Qt Mini text Editor")

    def File_save(self):

         #Only open dialog if there is no filename yet
        if not self.filename:
        
            self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', "",
                                                "All Files(*.*);;txt(*.txt);;;pdf(*.pdf);;writer(*.writer)")

# commented this section for just testing All files to work fine==============================
        elif self.filename:
            if str(self.filename).endswith(".writer"):       
                with open(self.filename,"wt") as file:
                    file.write(self.textEdit.toHtml())     #modified here too

                self.changesSaved = True
            # icons for the files.
            # We just store the contents of the text file along with the
            # format in html, which Qt does in a very nice way for us
            else:
            # Checking whether there is an Extension or not
                try:
                # If there is any Extension, Save it in its extension (Simply write the Content)
                    extension = self.filename.split(".")[1]

                    with open(self.filename,"wt") as file:
                        file.write(self.textEdit.toPlainText())
                    self.changesSaved = True
                except:
                    print("Write any extension")
    def File_save_as(self):
         #Only open dialog if there is no filename yet
        self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save as', "",
                                                "All Files(*.*);;pdf(*.pdf);;txt(*.txt);;;writer(*.writer)")

        if str(self.filename).endswith(".writer"):       
            with open(self.filename,"wt") as file:
                file.write(self.textEdit.toHtml())     #modified here too
            self.changesSaved = True
            
        elif self.filename:
            # Checking whether there is an Extension or not
            try:
                # If there is any Extension, Save it in its extension (Simply write the Content)
                extension = self.filename.split(".")[1]

                with open(self.filename,"wt") as file:
                    file.write(self.textEdit.toPlainText())
                self.changesSaved = True
            except:
                print("Write any extension ")
                
                
    def Cut(self):
        self.textEdit.cut()

    def Undo(self):
        self.textEdit.undo()
 
    def Redo(self):
        self.textEdit.redo()
 
     
    def Copy(self):
        self.textEdit.copy()
 
    def Paste(self):
        self.textEdit.paste()

    def Print(self):
        dialog = QtGui.QPrintDialog()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.text.document().print(dialog.printer())


    def PageView(self):
        preview = QtGui.QPrintPreviewDialog()
        preview.paintRequested.connect(self.PaintPageView)
        preview.exec_() 

    def PaintPageView(self, printer):
        self.textEdit.print_(printer) 

    
   
    def SavetoPDF(self):
        name = QtGui.QFileDialog.getSaveFileName(self,'Save to PDF','Untitled','documents(*.PDF)')
        if name:
            printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
            printer.setPageSize(QtGui.QPrinter.A4)
            printer.setColorMode(QtGui.QPrinter.Color)
            printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
            printer.setOutputFileName(name)
            self.textEdit.document().print_(printer)
 # CHANGING HERE   
    def word_wrap(self):
      if self.wrap_mode == False: #wrap mode on
         
        self.wrap_mode = True
        self.statusBar().showMessage("wrap mode on") # One more function here
        self.wrapAction.setIcon(QtGui.QIcon('icons/True.png'))
        self.textEdit.setWordWrapMode(QtGui.QTextOption.WrapAtWordBoundaryOrAnywhere)

      elif self.wrap_mode == True: #Wrap mode off
        self.wrap_mode = False
        self.statusBar().showMessage("wrap mode off") # One more function here
        self.wrapAction.setIcon(QtGui.QIcon('icons/False.png'))
        self.textEdit.setWordWrapMode(QtGui.QTextOption.NoWrap)  

   

    def font_dialog(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

        else:
            font = QtGui.QFont("Consolas")
            self.textEdit.setCurrentFont(font)

    def FontFamily(self,font):
        font = QtGui.QFont(self.fontFamily.currentFont())
        self.textEdit.setCurrentFont(font)
       
 
    def FontSize(self, fsize):
        size = (int(fsize))
        self.textEdit.setFontPointSize(size)


    def colorDialog(self):
        color = QtGui.QColorDialog.getColor()
        self.textEdit.setTextColor(color)


    def numberList(self):

        cursor = self.textEdit.textCursor()

        # Insert list with numbers
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)

    def bold(self):

        if self.textEdit.fontWeight() == QtGui.QFont.Bold:

            self.textEdit.setFontWeight(QtGui.QFont.Normal)

        else:

            self.textEdit.setFontWeight(QtGui.QFont.Bold)

    def italic(self):

        state = self.textEdit.fontItalic()

        self.textEdit.setFontItalic(not state)
    


    def underline(self):

        state = self.textEdit.fontUnderline()

        self.textEdit.setFontUnderline(not state)


    def alignLeft(self):
        self.textEdit.setAlignment(Qt.AlignLeft)
 
    def alignRight(self):
        self.textEdit.setAlignment(Qt.AlignRight)
 
    def alignCenter(self):
        self.textEdit.setAlignment(Qt.AlignCenter)
 
    def alignJustify(self):
        self.textEdit.setAlignment(Qt.AlignJustify)

    def BulletList(self):
        cursor = self.textEdit.textCursor()
        text = cursor.selectedText() 
        cursor.insertList(QTextListFormat.ListDecimal)  
        cursor.insertText(text)
        
    
    def date(self):
        #print(time.strftime("%d/%m/%Y %I:%M:%S"))
        self.textEdit.insertHtml(time.strftime("%d/%m/%Y"))

    def time(self):
        #print(time.strftime("%d/%m/%Y %I:%M:%S"))
        self.textEdit.insertHtml(time.strftime("%I:%M:%p"))

    def insertImage(self):   # for insertion of image in textEdit box

        # Get image file name
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Insert image',".","Images (*.png *.xpm *.jpg *.bmp *.gif)")

        if filename:
            
            # Create image object
            image = QtGui.QImage(filename)
            
            # Error if unloadable
            if image.isNull():

                popup = QtGui.QMessageBox(QtGui.QMessageBox.Critical,
                                          "Image load error",
                                          "Could not load image file!",
                                          QtGui.QMessageBox.Ok,
                                          self)
                popup.show()
            else:

                cursor = self.textEdit.textCursor()

                cursor.insertImage(image,filename)

    #voice recognition
    def Mic(self):
     r = sr.Recognizer()
     with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            print("got It.. now recognising...")
            text = r.recognize_google(audio, language="en-US")
            print("You said : {}".format(text))
            self.textEdit.append(text)
            
        except:
            print("Sorry could not recognize what you said")
            self.textEdit.append("Sorry could not recognize what you said")

    def help_menu(self):
        
        self.helpwindow = QtGui.QDialog()
        self.helpwindow.setWindowTitle('Type it....')
        self.helpwindow.setWindowIcon(QtGui.QIcon("icons/text-editor.png"))
        self.helpwindow.setFixedSize(400,200)
        self.helpwindow.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        Lbl = QtGui.QLabel(msg,self.helpwindow) #========================== edited help menu
        #pixmap = QtGui.QPixmap("icons/windows1.jpg")
        MY_Btn = QtGui.QPushButton('quit',self.helpwindow)
        MY_Btn.move(350,160)
        MY_Btn.resize(30,30)
        MY_Btn.clicked.connect(self.helpwindow_close)
        #Lbl.setPixmap(pixmap)
        self.helpwindow.exec_() 
       
    

    def helpwindow_close(self):
        self.helpwindow.hide()
        self.helpwindow.exec_() 
        

 
    def closeEvent(self, event):
     #   msgbox = QMessageBox;
      #  msgbox.setText("The Document has been Modified.")
      #  msgbox.setInformativeText("Do you Want To save changes?")
      #  msgbox.setStanderdButtons(QMessageBox.Save |QMessageBox.Discard|QMessageBox.Cancel)
      #  msgbox.setDefaultButton(QMessageBox.Save)
        if self.saved_data == self.textEdit.toPlainText():
            event.accept()
        else:
             choice = QtGui.QMessageBox.question(self,'You have changes!','Do you want to save before Exit?',
                       QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard|QtGui.QMessageBox.Cancel)
             
             if choice == QtGui.QMessageBox.Save:
                self.File_save()
                event.accept()
             elif choice ==QtGui.QMessageBox.Discard:
                event.accept()
             else:
                 event.ignore()

    def exit_fuction(self):
        if self.textEdit.toPlainText() == self.saved_data:
            sys.exit()
          #self.textEdit.setText("")

        else:
            choice = QtGui.QMessageBox.question(self,'You have changes!','Do you want to Save File?',
                       QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if choice == QtGui.QMessageBox.Yes:
                 self.File_save()
                 sys.exit()
            else:
                sys.exit()




def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet('QMainWindow{background-color: #ffffff;border: 2px solid black;}')
    app.setWindowIcon(QtGui.QIcon('text-editor.png'))
    Gui = Window()
    app.exec_()

if __name__ == '__main__':
    main()
