# latex-symbol

This terminal script helps you find that pesky LaTeX symbol or command you are looking for, by simply searching for it.
You can currently search either by sign to get command, or keyword to get sign or command.

#### IMPORTANT
To use this script, you have to make sure that your terminal supports unicode. Windows Command Prompt (CMD) does not,
so I would reccomend using either Windows Terminal or Powershell on Windows. If using Linux, - you'll figure it out.

## Installation

### Linux

Clone the repository into desired folder

```bash
git clone https://github.com/eidsheim98/HTTPStatusCode.git
```

Next, add this folder to path, to be able to run the file from anywhere on the computer. 
This line has to be run as administrator

```bash
set PATH=%PATH%;C:/Users/{username}/.cmd
```

After this, change directory into HTTPStatusCode

```bash
cd HTTPStatusCode
```

The last step is to run the setup.py file

```bash
python setup.py
```

If no errors are encountered, you are good to go!

### Windows

Windows installation instructions are on the way

## Usage

You run the script by typing 

```bash
lsym {searchTerm}
```

That means that if the code you got is 404, you should write

```bash
lsym lambda
```

And that should give you this information:

```bash
--------------------BEST FIT--------------------
Symbol    Command                       Comment
⊂         \subset                       subset or is implied by

⋐         \Subset                       DOUBLE SUBSET

Found 28 other matches, show? Y/N: 
```

You can the press either N or Y, depending on if you found the symbol you were looking for or not

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
