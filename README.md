# dddir

dddir creates directory structures from "blueprint"-files

## Example

A blueprint-file is a txt-file, that contains a representation of a directory-tree. Like this:

```
folder1
    file1.txt
folder2
    folder2-1
        file2.txt
        file3.txt
        folder2-1-1
            file4.txt
folder3
    file5.txt
```

## Usage
```
$ python /path/to/dddir/setup.py install
```
```
$ dddir -f /path/to/blueprint.txt
```
