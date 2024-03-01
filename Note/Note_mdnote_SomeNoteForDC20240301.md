## Git+Github

一个用于协作、跨设备跨平台联动的工具：Git+Github YYDS

教程直接用这个就行：https://www.liaoxuefeng.com/wiki/896043488029600/896827951938304

以下注意点。

这里面演示用的是macbook，因此关于windows当中有一些要注意的：

最开始的下载直接在官网下载；

然后安装时最好注意一下安装在哪。

接下来跟着教程打开git bash，注意不要用windows自己的命令行。

然后跟着走就行。

接着要注意的是这些操作都是Linux的，因此需要了解一些Linux的命令，推荐使用以下命令切到桌面后再创建learngit文件夹：

cd ～/c/Users/yangshuyun/Desktop

你可以找自己桌面位置，但是格式一定和上面一致；此外，cd的意思是换到这个文件夹；然后再补充一个ls命令，输入ls后显示当前文件夹有哪些文件。

其它问题可以线下交流（手动狗头）。

最后是编辑如readme.txt文件，你当然可以手动打开编辑，但是如果后面要让你编辑ssh密钥你又该如何应对呢（手动狗头）。

因此推荐使用：

vim readme.txt

vim的使用方法在下面 。

## Vim

启动Vim:

在终端中输入以下命令启动Vim：
   
vim

或者指定要编辑的文件：
   
vim 文件名

模式（Mode）:

Vim有不同的模式，主要包括两个常用的模式：

- 普通模式（Normal Mode）：
这是默认模式，用于移动光标、删除文本等操作。按 Esc 键可以进入普通模式。

- 插入模式（Insert Mode）：
在普通模式下按 i 键可以进入插入模式，可以输入文本。

移动光标：
在普通模式下，可以使用以下键来移动光标：

- h：向左移动

- j：向下移动

- k：向上移动

- l：向右移动


插入文本：
进入插入模式后，可以输入文本。按 Esc 键返回普通模式。

保存和退出：
在普通模式下，可以使用以下命令保存和退出：

- :w：保存文件
  
- :q：退出Vim
  
- :wq：保存并退出

6. 删除文本：
在普通模式下，可以使用以下命令删除文本：

x：删除光标所在位置的字符

dd：删除整行

撤销和重做：
在普通模式下，可以使用以下命令进行撤销和重做：

u：撤销

Ctrl + r：重做

复制和粘贴：
在普通模式下，可以使用以下命令复制和粘贴：

yy：复制当前行

p：粘贴

搜索和替换：
在普通模式下，可以使用以下命令搜索和替换：

/关键字：向下搜索

?关键字：向上搜索

:s/旧文本/新文本/g：替换文本

退出Vim：
在普通模式下，可以使用以下命令退出Vim：

:q!：强制退出，不保存修改


## 其它
Summary
Here is a summary of the commands we just went over for your reference:
- ls: lists all files in the current directory
- cd <path to directory>: change into the specified directory
- mkdir <directory name>: make a new directory with the given name
- mv <source path> <destination path>: move the file at the given source to the given destination
Finally, you're ready to start editing the lab files! Don't worry if this seems complicated—it will get much easier over time. Just keep practicing! You can also take a look at our UNIX tutorial for a more detailed explanation of terminal commands.

要在macOS上使用命令行创建一个新的txt文件，您可以使用以下命令：
touch newfile.txt
这将在当前目录下创建一个名为newfile.txt的空文本文件。如果您想要在特定目录下创建文件，可以使用以下命令：
touch /path/to/directory/newfile.txt
如果您想要创建一个包含文本的文件，可以使用以下命令：
echo "Hello, World!"newfile.txt
这将在当前目录下创建一个名为newfile.txt的文本文件，并将Hello, World!写入该文件。如果您想要在特定目录下创建文件，可以使用以下命令：
echo "Hello, World!"/path/to/directory/newfile.txt
希望这可以帮助您！
