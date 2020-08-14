import requests
from bs4 import BeautifulSoup

URL = f"http://stackoverflow.com/jobs?q=python&sort=i"


# 해야할 것
# step1. 페이지 가져오기
# step2. request 만들기
# step3. Job 가져오기

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_pages = pages[-2].get_text(strip=True)
    return int(last_pages)


# def extract_job(html):
#     # 수업시간 작성한 코드
#     title = html.find("h2", {"class": "fs-body3"}).find("h2").find("a")["title"]
#     # 어떤 분이 댓글 알려주신 코드
#     # title = html.find("h2").text.strip()
#     company, location = html.find("div", {"class": "-company"}).find_all("span", recursive=False)
#     company = company.get_text(strip=True).strip("\n")
#     location = company.get_text(strip=True).strip("-").strip("\n").strip(" \r")  # ("\n")과 (" \r") 둘 다 같은 뜻이다.
#     return {'title': title, 'company': company, 'location': location}

def extract_job(html):
    title = html.find("h2").text.strip()
    company, location = html.find("h3", {"class": "fc-black-700"}).find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html('data-jobid')
    return {'title': title, 'company': company, 'location': location,
            "apply_link": f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping StackOverflow: Page: {page}")
        result = requests.get(f"{URL}&pg={page + 1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "s-link"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
