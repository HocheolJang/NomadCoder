from WebScrapping_indeed import get_jobs as get_indeed_jobs
from WebScrapping_StackOverflow import get_jobs as get_so_jobs
from save import save_to_file

# indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()
indeed_jobs = get_indeed_jobs()
jobs = so_jobs + indeed_jobs
save_to_file(jobs)


# from indeed import extract_indeed_pages, extract_indeed_jobs
# max_indeed_pages = extract_indeed_pages()



