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

## Redirection & Chaining

Redirection allows you to save an output anywhere you want. For example, `head -n 5 <file1> > top.csv` saves the out of `head -n 5 <file1>` to a new file called `top.csv`.

Use the `|` (pipe) character to avoid leaving intermediate files around. `head -n 5 seasonal/summer.csv | tail -n 3` uses the output of `head -n 5 seasonal/summer.csv` as the input of `tail -n 3`. Use the pipe character to chain together commands. `cut -d , -f 1 <csv file> | grep -v <column name> | head -n 10` selects the first column of a CSV file, selects all rows but the header, then outputs the top 10 rows of the resulting file.

`wc [-c | -w | -l] <file>` (word count) prints the number of characters, words, or lines in a file.

You can select many files at once or many files of a certain type by using the `*` wildcard. It will match zero or more characters like so:
* `cut -d , f 1 <directory>/*` will get the first comma-separated column of all files in a directory.
* `cut -d , f 1 <directory>/*.csv` will get the first column from every CSV file in the directory.

Other wildcards include:
* `?` which matches a single character. `201?.txt` will match `2019.txt` or `2010.txt` but not `2019-01.txt`.
* `[]` will match any of the characters inside the brackets. `201[89].txt` matches `2018.txt` or `2019.txt` but not `2010.txt`.
* `{}` will match any of the comma-separated patterns inside the braces. `{*.txt, *.csv}` will match any file ending in `.txt` or `.csv` but not `.pdf`. `{singh.pdf, j*.txt}` matches `singh.pdf` and `johel.txt` but not `sandhu.pdf` or `sandhu.txt`.

`sort` orders an output alphabetically by default. Its flags include:
* `-n` to sort numerically 
* `-r` to reverse order
* `-b` to ignore leading blanks
* `-f` to fold case - that is, become case insensitive

`cut -d , -f 2 <dir>/<filename>.csv | grep -v <column> | sort -r` reverse sorts the data from the second column of a CSV.

Use `sort` with `uniq` to remove duplicate data. `cut -d , -f 2 <dir>/<filename>.csv | grep -v <column> | sort | uniq -c` returns a count of unqiue data entries. If you want to save this output, then use redirection at the end to put it in a file like `cut -d , -f 2 <dir>/<filename>.csv | grep -v <column> | sort | uniq -c > unique_counts.txt`.

If you need to stop a command from executing because it is taking too long are you wrote in an error like a redirection in the middle of a pipe chain, then exit with CTRL+C.

## Batch Processing

The shell has environment variables, written in all caps, are always available. Use `set` to see them all but the most common are:
* `HOME` which stores the user's home directory
* `PWD` which stores the present working directory, the same as `pwd`
* `SHELL` which stores the shell program in use
* `USER` which stores the user's ID

To print the value of the variable, use `echo $<VARIABLE>`.

Shell variables are like a programming language's local variables. Create a variable and assign it a value like `<variable>=<value>`, then access its value as above with echo and $.

Loops are used to repeat tasks. Their basic form is `for <variable> in <list>; do <task>; done`. For example, `for filename in <directory/*.csv; do echo $filename; done` lists all the CSV filenames in the directory. It is best practice to store the names of a set of files in a variale, like so `datasets=<directory>/*.csv`, then `for filename in $datasets; do echo $filename; done`. Beginners often forget to use the `$` symbol when they want to refer to the value of a variable. Long-time users usually run into errors by misspelling their variable.

Using chains in the do clause of the loop to run many commands in a single loop, like `for file in <dir>/*.csv; do grep -h <column> $file; done` or `for file in <dir>/*.csv; do head -n 2 $file | tail -n 1; done`.

In general, when working with files via the shell, avoid using spaces in the file name. Otherwise, you must enclose the whole file name in single quotes, like `'July 2019 Data.csv'`. `July 2019 Data.csv` looks like 3 different files to the shell.

## Shell Scripting

*nano* is a popular text editor available in the shell. You might use it for quick and simple file creation and editing. I like using Visual Studio Code.

You can write your command history to a file to record all your previous steps.  For example:
```
cp seasonal/spring.csv seasonal/summer.csv ~/
grep -hv Tooth ~/spring.csv ~/summer.csv > temp.csv
history | tail -n 3 > steps.txt
```
Line 1 copies two csv files to the home directory. Line 2 grabs all rows that don't have "Tooth" in them and redirects (writes or saves) them to a file. Line 3 captures the two previous lines plus the history command and redirects those commands to a text file to record the steps you took.

You can save commands by writing them to a file, like above, then running the file. If the file `cmd_list.sh` has commands in it (called a shell script), then run it by invoking `bash cmd_list.sh`, where bash is the name of the shell program.

You will want to pass in multiple filenames to a script you created. The `$@` symbols allow you to do this. Inside the file called `unique-lines.sh`:

```
sort $@ | uniq
```

Then, in the shell, run:

```
bash unique-lines.sh <file1> <file2> <...>
```

Loops in shell scripts (scripts) look a little different from writing them in the shell. The file might look like this:

```
# Print the first and last data records of each file.
for filename in $@
do
    head -n 2 $filename | tail -n 1
    tail -n 1 $filename
done
```

The indentation isn't necesary but increases code readability. The line that begins with the `#` symbol is a comment. It is a note to the user and does not execute as code.

## Resources

I haven't tried these out yet myself, but I'd like to hear about feedback from people who do. I intend to try them out in the future.

* Steve Parker's [shell scripting tutorial](https://www.shellscript.sh/)
* William Shotts' [shell scripting tutorial](http://linuxcommand.org/lc3_writing_shell_scripts.php)
* GeeksForGeeks [shell scripting tutorial](https://www.geeksforgeeks.org/introduction-linux-shell-shell-scripting/)

## Notes

This is version 1.0 of this document and is based off my notes from the [DataCamp Unix Shell](https://www.datacamp.com/courses/introduction-to-shell-for-data-science) course by [Greg Wilson](https://twitter.com/gvwilson).