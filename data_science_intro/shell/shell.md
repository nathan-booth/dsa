# Unix Shell

It is useful for interacting with cloud technology, building pipelines, automating computer tasks and replicating tasks.

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

