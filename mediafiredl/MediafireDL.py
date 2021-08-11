from bs4 import BeautifulSoup
import requests, os, sys

def GetName(url: str):
    return url.split('/')[-2]

def GetFileLink(url: str):
    content = requests.get(url).content
    soup = BeautifulSoup(content, "html.parser")
    
    try: 
        link = soup.find(id="downloadButton").get("href")
        return link
    except Exception as e: 
        print(e)
        return e

def GetFileSize(url: str):
    with requests.get(GetFileLink(url), stream=True) as r:
        return int(r.headers.get('content-length'))

def AsMegabytes(bytes: int):
    return round(bytes/1024/1024, 2)

def BulkDownload(urls: list):
    total_files = len(urls)
    
    print("[Bulk downloading files]")
    print(f"Total files: {total_files}.")

    sys.stdout.write("Total size: Analyzing...")
    total_bulk_size = 0
    for url in urls:
        total_bulk_size += GetFileSize(url)
        sys.stdout.write(f"\x1b[2K\rTotal size: {AsMegabytes(total_bulk_size)}mb.")
        sys.stdout.flush()
    sys.stdout.write("\n")

    for url in urls:
        Download(url)

def Download(url: str, output = "", filename = ""):
    if not(filename): 
        filename = GetName(url)

    url = GetFileLink(url)
    if not(output):
        output = os.path.dirname(os.path.realpath(__file__))

    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(f"{output}/{filename}", "wb") as f:
                total_length = r.headers.get('content-length')
                total_length = int(total_length)
                download_progress = 0
                for chunk in r.iter_content(chunk_size=1024):
                    download_progress += len(chunk)

                    f.write(chunk)

                    percentage = int(100 * download_progress/total_length)
                    mb_progress = round(download_progress/1024/1024, 2)
                    mb_total_progress = round(total_length/1024/1024, 2)
                    sys.stdout.write(f"\r[Downloading {filename}] Progress: {percentage}% ({mb_progress}mb/{mb_total_progress}mb)")
                    sys.stdout.flush()
        sys.stdout.write("\n")
        return f"{output}/{filename}"
    except Exception as e:
        print(e)
        return e