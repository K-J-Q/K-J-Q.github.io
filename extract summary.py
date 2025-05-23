import glob
import os
import re
from bs4 import BeautifulSoup

certs_folder = "certs\\"
experiences_path = "idx.html"
testimonials_path = "testimonials.html"
projects_path = "projects.html"
education_path = "education.html"


def retrieve_experiences(out):
    with open(experiences_path, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    jobs = soup.find('ul', {'id': 'job'}).find_all('li', class_='list-group-item')

    out.write("\nExperiences:\n")
    for job in jobs:
        title = job.find('h4', class_='card-title').text.strip()
        description = job.find('h5', class_='card-subtitle mb-2 text-muted').text.strip()
        out.write(f"{title}\n - {description}\n")

def retrieve_testimonials(out):
    with open(testimonials_path, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    testimonials_div = soup.find('div', class_='mx-auto w-75')
    testimonials = testimonials_div.find_all('h2')

    out.write("\nTestimonials:\n")
    for testimonial in testimonials:
        out.write(f"{testimonial.text}\n")

def retrieve_projects(out):
    with open(projects_path, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    projects_ul = soup.find('ul', {'id': 'projects'})
    projects = projects_ul.find_all('li', class_='list-group-item')

    current_year = None
    for project in projects:
        if 'active' in project['class']:
            current_year = project.text
            out.write(f"\n{current_year}\n")
        else:
            title = project.find('h4').text
            descriptions = project.find_all('li')
            description_text = '\n'.join([" - "+ re.sub(r'\s+', ' ', desc.text.strip()) for desc in descriptions])
            out.write(f"{title}\n{description_text}\n")

def retrieve_certificates(out):
    file_format = (".pdf", ".jpg", ".jpeg", ".png")
    certs = glob.glob(certs_folder + "**", recursive=True)
    
    out.write("\nCertificates: \n")

    l = len(certs_folder)

    for cert in certs:
        if cert.endswith(file_format):
            filename = os.path.basename(cert)
            filename_without_ext = os.path.splitext(filename)[0]
            out.write(f" - {filename_without_ext}\n")
        elif os.path.isdir(cert) and cert != certs_folder:
            out.write(f"{cert[l:]}\n")

def retrieve_education(out):
    with open(education_path, 'r') as f:
        contents = f.read()
        
    soup = BeautifulSoup(contents, 'html.parser')

    container = soup.find('body').find('div', {'class': 'container'})

    out.write("\nEducation:\n")

    for li in container.find_all('li', {'class': ['school', 'timeline-inverted school']}):
        school = li.find('h4', {'class': 'timeline-title'}).text
        out.write(school + "\n")

        achievements = li.find('div', {'class': 'timeline-body'}).find('ul')
        if achievements:
            for achievement in achievements.find_all('li'):
                out.write(f" - {achievement.text}\n")
    
def main():
    out = open("summary.txt", "w")
    retrieve_experiences(out)
    retrieve_testimonials(out)
    retrieve_projects(out)
    retrieve_certificates(out)
    retrieve_education(out)
    out.close()


if __name__ == "__main__":
    main()