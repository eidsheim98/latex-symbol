# latex-symbol

This terminal script helps you find that pesky LaTeX symbol or command you are looking for, by simply searching for it.
You can currently search either by sign to get command, or keyword to get sign or command.

#### IMPORTANT
To use this script, you have to make sure that your terminal supports unicode. Windows Command Prompt (CMD) does not,
so I would recommend using either Windows Terminal or Powershell on Windows. If using Linux, - you'll figure it out.

## Installation

### Linux

Clone the repository into desired folder

```bash
git clone https://github.com/eidsheim98/latex-symbol.git
```

After this, change directory into latex-symbol folder

```bash
cd latex-symbol
```

The last step is to run the setup.py file

```bash
python3 setup.py
```

If no errors are encountered, you are good to go!

### Windows

Start by cloning this repository into a desired folder. To run the program from anywhere in the terminal,
I would recommend creating a specific folder i an easy-to-remember location you would not need administrative
rights to edit. This could for instance be in a folder called

```bash
C:/Users/{username}/.cmd
```

Go into this directory using the command

```bash
cd C:/Users/{username}/.cmd
```

Then run the command for cloning the repository

```bash
git clone https://github.com/eidsheim98/latex-symbol.git
```

Next, add this folder to path, to be able to run the file from anywhere on the computer.
This line has to be run as administrator

```bash
set PATH=%PATH%;C:/Users/{username}/.cmd
```

After this, change directory into latex-symbol

```bash
cd latex-symbol
```

The last step is to run the setup.py file

```bash
python setup.py
```

If no errors are encountered, you are good to go!

## Usage

You run the script by typing 

```bash
lsym {searchTerm}
```

That means if you want the lambda sign you type

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

### Other usage
You can also search using a symbol, or a keyword in the comment text. More search capabilities are underway.
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
