import os

def getOpenFileName(default = None):
    return getFromPrompt(default, "Enter a file to load from")

def getSaveFileName(default = None):
    filename = getFromPrompt(default, "Enter a file to save to")
    
    if os.path.exists(filename):
        print("The file %s already exists" % filename)
        prompt = "Overwrite (o), enter another name (f), or cancel (c)"

        check = input(prompt)
        while check != "o" and check != "f" and check != "c":
            check = input(prompt)

        if check == "o":
            return filename
        elif check == "f":
            return getSaveFileName(default)
        elif check == "c":
            return None

    return filename

def getDelimeter(default=None):
    return getFromPrompt(default, "Enter the delimeter")

def getDataType(default=None):
    return getFromPrompt(default, "Enter the data type")

def getComparissonFunction(default=None):
    return getFromPrompt(default, "Enter the comparisson function")

def getFromPrompt(default=None, prompt=""):
    if default is not None:
        prompt += (" (default: %s)" % default)
    prompt += ": "

    result = input(prompt)
    if result == "" and not (default is None):
        result = default
    
    return result

