import subprocess as sp

def getDate(text_widget):
    text_widget.delete(1.0, tk.END)
    byteoutput=sp.run(["powershell", "-command", "Get-Date"], capture_output=True)
    strout=byteoutput.stdout.decode("utf-8")
    text_widget.insert(tk.END, strout[2:-1])

def getComputerInfo(text_widget):
    text_widget.delete(1.0, tk.END)
    byteoutput=sp.run(["powershell", "-command", "Get-ComputerInfo"], capture_output=True)
    strout=byteoutput.stdout.decode("utf-8")
    length=len("WindowsRegisteredOwner")
    strstart=strout.find("WindowsRegisteredOwner")
    i=length+strstart
    while strout[i]==" ":
        i+=1
    i+=2
    j=i
    a=strout.find("\n")
    while strout[j]!="\n":
        j+=1
    text_to_display="System owned by "+strout[i:j]
    text_widget.insert(tk.END, text_to_display)
