# dddir

dddir creates directory structures from "blueprint"-files. dddir can create files and folders.

## Example

A blueprint-file is a txt-file, that contains a representation of a directory-tree. Like this:

```
folder1
    file1.txt
folder2
    folder3
        file2.txt
        file3.txt
        folder4
            file4.txt
folder5
    file5.txt
```

## Usage

Install dddir with the following command:

```
$ python /path/to/dddir/setup.py install
```

You're now able to use dddir from your commandline:

```
$ dddir -f /path/to/blueprint.txt
```

dddir now goes to work and creates a folder "dddir-output" in your home directory. This folder contains your directory.
