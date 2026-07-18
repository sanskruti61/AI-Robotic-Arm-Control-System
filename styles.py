# ui/styles.py

STYLE = """
/* ===========================
   Main Window
=========================== */

QMainWindow {
    background-color: #1E1E1E;
}

QWidget {
    background-color: #1E1E1E;
    color: white;
    font-family: "Segoe UI";
    font-size: 12px;
}


/* ===========================
   Sidebar
=========================== */

QFrame#sidebar {
    background-color: #252526;
    border-right: 1px solid #3A3A3A;
}

QLabel#logoLabel {
    color: #00BFFF;
    font-size: 22px;
    font-weight: bold;
    padding: 15px;
}


/* ===========================
   Buttons
=========================== */

QPushButton {
    background-color: #007ACC;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px;
    font-size: 13px;
    text-align: left;
}

QPushButton:hover {
    background-color: #0099FF;
}

QPushButton:pressed {
    background-color: #005A9E;
}


/* ===========================
   Camera Frame
=========================== */

QFrame#cameraFrame {
    background-color: #111111;
    border: 2px solid #444444;
    border-radius: 12px;
}

QLabel#cameraLabel {
    color: white;
    font-size: 20px;
}


/* ===========================
   Right Info Panel
=========================== */

QFrame#infoPanel {
    background-color: #2B2B2B;
    border-radius: 12px;
}

QLabel#panelTitle {
    font-size: 18px;
    font-weight: bold;
    color: #00BFFF;
}

QLabel#valueLabel {
    background-color: #383838;
    padding: 8px;
    border-radius: 8px;
}


/* ===========================
   Console
=========================== */

QTextEdit {
    background-color: #111111;
    color: #00FF66;
    border-radius: 10px;
    font-family: Consolas;
}


/* ===========================
   Status Bar
=========================== */

QStatusBar {
    background-color: #252526;
    color: white;
}


/* ===========================
   Combo Box
=========================== */

QComboBox {
    background-color: #383838;
    color: white;
    border-radius: 8px;
    padding: 5px;
}
"""