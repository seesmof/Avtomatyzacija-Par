import webbrowser
import pyperclip
from library import speak_text


def class_фп():
    speak_text("Starting Physical Education class")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/4225643406?pwd=UENrZE9SckhzQ25XS01qMGhxdnI3dz09"
    )


def class_фі():
    speak_text("Starting Philosophy class")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/7423010976?pwd=MDBKRTVDbHZ0MDVwbStmdElodUxiZz09%20"
    )


def class_ооп():
    speak_text("Starting Object-Oriented Programming class")
    webbrowser.open_new_tab("https://us02web.zoom.us/j/85793432609")
    pyperclip.copy("2023")


def class_кдм_пр():
    speak_text("Starting Computer Discrete Maths lab")
    webbrowser.open_new_tab("https://meet.google.com/hke-ztgv-wxg")


def class_кдм_лк():
    speak_text("Starting Computer Discrete Maths lecture")
    webbrowser.open_new_tab("https://meet.google.com/arg-syjc-vcz")


def class_вмма_пр():
    speak_text("Starting Calculus lab")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/3815612002?pwd=VW03dHdFQzk1Qnk4M0dlL2RMMlIxQT09")


def class_вмма_лк():
    speak_text("Starting Calculus lecture")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/4344130497?pwd=Z05oUnB4RDJGTGRWeEFaNlRsVDlBZz09")


def class_ам():
    speak_text("Starting English class")
    webbrowser.open_new_tab(
        "https://us02web.zoom.us/j/88030483350?pwd=YXFQYU9URVIwd1FRbkxqVFBxd2ZJdz09")


def class_нп_пр():
    speak_text("Starting Low Level Programming lab")
    pyperclip.copy("152334")
    webbrowser.open_new_tab(
        "https://us02web.zoom.us/j/5151534723"
    )


def class_нп_лк():
    speak_text("Starting Low Level Programming lecture")
    webbrowser.open_new_tab(
        "https://us04web.zoom.us/j/7594080934?pwd=RlBDYW9OMzNGeXkwQjBGQzNKNnF4QT09"
    )


def class_сс_лк():
    speak_text("Starting Soft Skills lecture")
    webbrowser.open_new_tab(
        "https://us04web.zoom.us/j/76026382394?pwd=wcmYLJnXS7RVbz7ZFu624OeGozRwgs"
    )


def class_сс_пр():
    speak_text("Starting Soft Skills lab")
    webbrowser.open_new_tab(
        "https://meet.google.com/sor-axaz-zxk"
    )
