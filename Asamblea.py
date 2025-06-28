import requests
from bs4 import BeautifulSoup
import Utils
import re
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs


def extract_youtube_id(url):
    parsed = urlparse(url)

    # For standard YouTube URL
    if 'youtube.com' in parsed.netloc:
        query = parse_qs(parsed.query)
        return query.get('v', [None])[0]

    # For short YouTube URL
    if 'youtu.be' in parsed.netloc:
        return parsed.path.lstrip('/')

    return None  # fallback


url = 'https://www.asamblea.go.cr/p/SitePages/Noticias.aspx'
response = Utils.obtener_contenido_link(url)
soup = BeautifulSoup(response)
from bs4 import BeautifulSoup

tables = soup.select("table.ms-listviewtable")

rows = tables[0]

results = []

for row in rows:
    cols = row.find_all("td")

    if len(cols) < 6:
        continue
    
    created = cols[5].get_text(strip=True)
    if(created == "16/5/2025"):
        break


    description_div = cols[3].find("div", class_="ms-rtestate-field")
    description = description_div.get_text(separator="\n", strip=True) if description_div else ""
    
    detail_div = cols[4].find("div", class_="ms-rtestate-field")
    detail = detail_div.get_text(strip=True) if detail_div else ""

    if("📹Asamblea Legislativa Noticias📹" in description or "📹Asamblea Legislativa Noticias📹" in detail):
        continue

    all_links = re.findall(pattern='https?://[^\s<>"]+', string=description)

    description = [link for link in all_links if "youtube" in link or "youtu.be" in link]

    all_links = re.findall(pattern='https?://[^\s<>"📌]+', string=detail)
    
    detail = [link for link in all_links if "youtube" in link or "youtu.be" in link]
    
    if(len(description) == 0):
        description = detail 

    transcripts = []
    for link in description: 
        video_id = extract_youtube_id(link)
        try:
            transcripts.append(YouTubeTranscriptApi.get_transcript(video_id, languages=['es']))
        except:
            transcripts.append("")

    results.append({
        "links": description,
        "created": created,
        "transcripts": transcripts
    })

    for item in results:
        print(item)


