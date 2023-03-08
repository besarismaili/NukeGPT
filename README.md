# **NukeGPT - Generating Python code with OpenAI's API**

NukeGPT is a simple Nuke toolset that allows you to generate code using OpenAI's models. The toolset is easy to use and can be added to your Nuke workflow in just a few simple steps.

## **Getting Started**

## **Installing Python and Requests module**

1. Go to the official Python website and download the latest version of Python: **[https://www.python.org/downloads/](https://www.python.org/downloads/)**
2. Run the Python installer and follow the installation wizard to install Python on your system. Make sure to select the option to add Python to your system PATH during installation.
3. Open a command prompt or terminal and type the following command to install the Requests module: **`pip install requests`**
4. Wait for the installation to complete.

## **Adding the Python path to init.py file**

1. Under the path  **`C:\Users\{USER}\.nuke`,**  **`{USER}`** is your Windows username.
2. Open the file called **`init.py`**  in a text editor.
3. Type the following line in the **`init.py`** file, replacing the path with the path to your Python executable, mine looks like this:
    
    ```
    nuke.pluginAddPath("C:/Users/{USER}/AppData/Local/Programs/Python/Python311/Lib/site-packages")
    ```
    
4. Save the **`init.py`** 
5. Close and reopen Nuke for the changes to take effect.

That's it! You should now be able to use the Requests module in Nuke. If you encounter any issues, make sure to double-check the paths in the **`init.py`** file and the path your Python modules are installed.

### **Creating an OpenAI Account**

Before you can start using NukeGPT, you need to create an account with OpenAI and obtain an API key. Here's how to do it:

1. Go to the OpenAI website (**[https://openai.com/](https://openai.com/)**) and click on the "Sign up" button at the top right corner of the screen.
2. Follow the on-screen instructions to create an account. You will be asked to provide your name, email address, and password.
3. Once you have created your account, go to the API tab on your dashboard.
4. Click on the "Generate API key" button to obtain your API key. (*Make sure you copy the key as soon as it is shown because after it’s hidden you can’t view the key again and have to generate a new one.)*

### **Using NukeGPT**

Now that you have your API key, you can start using NukeGPT in your Nuke workflow. Here's how to do it:

1. Download the file NukeGPT.nk
2. Navigate to the location where you downloaded the NukeGPT toolset and select the "NukeGPT.nk" file. Click "Open".
3. The NukeGPT node will appear in your Node Graph. Double-click on the node to open it.
4. Paste your OpenAI API key into the "API Key" field on the "API" tab.
5. Save it as Toolset for easy access.

### **Saving NukeGPT as a Toolset**

If you plan on using NukeGPT frequently, you can save it as a toolset so that it's easily accessible from your toolbar. Here's how to do it:

1. Right-click on the NukeGPT node and select “Toolset” and "Create".
2. Enter a name for the toolset and click "OK".
3. The toolset will now be accessible from your toolbar. To use it, simply press ‘Tab’ and type the name.

## **Conclusion**

NukeGPT is a powerful tool that allows you to generate code using OpenAI's models directly within Nuke. By following the steps outlined in this readme, you can easily integrate it into your Nuke workflow and start generating python scripts with just a few clicks.
