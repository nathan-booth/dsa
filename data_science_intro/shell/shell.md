# Unix Shell

It is useful for interacting with cloud technology, building pipelines, automating computer tasks and replicating tasks.

A note on conventions. Anything enclosed in <> is a placeholder name. Anything enclosed in [] is optional.

## Navigation & Manipulating Files & Directories

How to 'look and move around' in the computer.

### Paths 

Use `pwd`, which means print working directory to find where you are in the file system. `/home/repl` is an absolute path. If you're in `home` and you type something like `ls repl` or `cd repl`, you're using a relative path.

### Common Commands

* `ls` means listing. It allows you to see what is in a directory. `ls /home/repl` reveals the files in the repl directory.
* `cd` means change directory. It allows you to navigate to another directory. `cd ..` moves up to the parent directory. `cd ~` moves to the root directory. `cd /home/repl/seasonal` moves to the seasonal directory.
* `cp` means copy. It allows you to copy a file. `cp <file to copy> <copied file destination>`. `cp <file1> <file2> <destination>` copies two files to some destination directory.
* `mv` means move. Move the file (i.e. cut and paste it) to another directory. `cp <file1> <file2> <destination>` moves two files to some destination directory. Move is used to rename files too. `mv course.txt old-course.txt` moves the contents of `course.txt` to `old-course.txt`.

> Copy and move will overwrite existing files. If, for example, you already have a file called old-course.txt, then the command shown above will replace it with whatever is in course.txt

* `rm` means remove. There is no trash can application in the shell, so removed files are deleted forever. `rm thesis.txt` deletes the file. You will get an error if you try removing a directory without using command options - this is for your own safety.
* `rmdir` removes empty directories. `rmdir <dirname>`
* `mkdir` creates a directory. `mkdir <dirname>`

## Data Manipulation

### File Content

* `cat <file> [<file2> ...]` concatenates file content in the shell output. Can displays the entire file and you can scroll through it.
* `less <file> [<file2> ...]` allows you to page through a file one page at a time. Hit spacebar to navigate to the next page and `q` to quit. If you want to navigate through multiple files in this way, `:n` moves to the next file, `:p` moves to the previous file and `:q` quits the view.
* `head <file>` displays the first 10 lines of the file. The `-n` (n = number of lines) command line flag allows you to specify the number of lines to display.
* As you type, use tab completion to help you type less.

> By convention, place flags before any file names.

* See all nested directories and files by using `ls` with the `-R` (R = recursive). The `-F` flag (F = classify) prints `/` after each directory and `*` after each runnable program. If you want to use multiple flags, then `-RF` or `-FR` will work. Order does not matter. 
* You look up how a command works with `man <cmd>` (man = manual). Of course, nowadays, you can do an Internet search too.
* `head` and `tail` enable file row selection. `cut [-f -d] <file>` (f = fields, d = delimiter) enable column selection. For example, `cut -d , -f 1-3,5 <file.csv>` selects columns 1 through 3 and column 5 and knows to expect the columns are comma-separated. Cut does not handle delimiters that are used within the file well.
* You have several ways to repeat commands. 
    1. Use the up and down arrows on your keyboard. Modify the command using left and right arrays before pressing enter again.
    2. `history` displays all of the commands you have run during this shell session along with an ID number. Run a particular command from the history with `!<CMD ID>` like `!5`.
    3. Run the most recent use of a command with `!<CMD>` like `!head`.
* `grep <pattern>` allows you to select individual lines or files that contain particular data. This has some cool flags associated with it too.
    * `-c` print a count of matching lines
    * `-h` do not print the file names of matching files
    * `-i` ignore the case of the character
    * `-l` print the names of files that contain matches
    * `-n` print line numbers with the matching line
    * `-v` print lines that do not match the pattern.
