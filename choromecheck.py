import subprocess

chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

def openchrome(name, html):
    open(f"{name}.html", "w", encoding="utf-8").write(html)
    subprocess.Popen([chrome, f"{__file__}\\..\\{name}.html"])