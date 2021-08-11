# MediafireDL

MediafireDL is an automation tool to download files from mediafire without having to do any extra steps, which allows you to retrieve data from any mediafire link.

I designed this to make it work on a python console application, multi threading is not supported for now, but my goal is to make it easy to download and show progress trough GUI frameworks like kivy or pyqt5.

You can use the following file as a test, however it will be removed soon. <br>
[Go to test file.](https://www.mediafire.com/file/ipnyzofjcwri357/test-10mb.bin/file)

## What can it do?
MediafireDL allows you to: <br>
* Get file size. <br>
* Get file name. <br>
* Get true file link. <br>
* Download a file. <br>
* Bulk download files. <br>

directly from a single URL.

## Requirements
This module uses `beautifulsoup4` and `requests`, if you do not have these modules installed, they will install automatically.

## Installation
```bash
pip install mediafiredl
```

## Importing
```python
from mediafiredl import MediafireDL
```

## Available functions
```python
from mediafiredl import MediafireDL as MF

url = "https://www.mediafire.com/file/ipnyzofjcwri357/test-10mb.bin/file"

# Returns a string with the file name, including its extension.
file_name = MF.GetName(url)

# Returns true file link
file_link = MF.GetFileLink(url)

# Returns file size in bytes
file_size = MF.GetFileSize(url)

# Returns the conversion from bytes to megabytes
file_size_mb = MF.AsMegabytes(file_size)

# Downloads a file to local directory and returns its download path. A second argument can be used to assign the output directory, it must not end with a "\".
file_result = MF.Download(url)
# Custom output example:
file_result = MF.Download(url, "C:\\Users\\User\\Desktop")
#or
file_result = MF.Download(url, output="C:\\Users\\User\\Desktop")


# Bulk file downloads
bulk_urls = [
    "url1",
    "url2",
    "url3",
    "url4"
]

# Displays how many files you will be downloading and the total size.
# After displaying this information, it will start downloading the files one by one.
MF.BulkDownload(bulk_urls)


```