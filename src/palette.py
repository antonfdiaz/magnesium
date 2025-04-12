from PySide6.QtGui import *
#light palette
palette = QPalette()
palette.setColor(QPalette.Window,QColor(220,220,220))
palette.setColor(QPalette.WindowText,QColor(0,0,0))
palette.setColor(QPalette.Base,QColor(220,220,220))
palette.setColor(QPalette.AlternateBase,QColor(200,200,200))
palette.setColor(QPalette.ToolTipBase,QColor(220,220,220))
palette.setColor(QPalette.ToolTipText,QColor(0,0,0))
palette.setColor(QPalette.Text,QColor(0,0,0))
palette.setColor(QPalette.Button,QColor(220,220,220))
palette.setColor(QPalette.ButtonText,QColor(0,0,0))
palette.setColor(QPalette.BrightText,QColor(255,0,0))
palette.setColor(QPalette.Link,QColor(0,0,255))
palette.setColor(QPalette.Highlight,QColor(0,120,215))
palette.setColor(QPalette.HighlightedText,QColor(255,255,255))
#make the url bar placeholder text black
palette.setColor(QPalette.PlaceholderText,QColor(0,0,0,128))