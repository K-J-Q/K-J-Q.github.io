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
    with open(experiences_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    out.write("\nExperiences:\n")
    jobs_container = soup.find('ul', {'id': 'job'})
    if jobs_container:
        jobs = jobs_container.find_all('li', class_='list-group-item')
        for job in jobs:
            title = job.find('h4', class_='card-title').text.strip()
            description = job.find('h5', class_='card-subtitle mb-2 text-muted').text.strip()
            out.write(f"{title}\n - {description}\n")
        return

    experiences_section = soup.find('section', {'id': 'experience'})
    if not experiences_section:
        raise ValueError(f"Unable to find experience content in {experiences_path}.")

    experience_cards = experiences_section.find_all('div', class_='exp-card')
    if not experience_cards:
        raise ValueError(f"Unable to find experience cards in {experiences_path}.")

    for card in experience_cards:
        title_node = card.find(['h3', 'h4'])
        company_node = card.find('p', class_='company')
        role_node = card.find('p', class_='role-desc')

        title = title_node.get_text(strip=True) if title_node else "Unknown Role"
        details = [node.get_text(strip=True) for node in [company_node, role_node] if node]
        description = " — ".join(details) if details else "No description available."
        out.write(f"{title}\n - {description}\n")

def retrieve_testimonials(out):
    with open(testimonials_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    testimonials_div = soup.find('div', class_='mx-auto w-75')
    testimonials = testimonials_div.find_all('h2')

    out.write("\nTestimonials:\n")
    for testimonial in testimonials:
        out.write(f"{testimonial.text}\n")

def retrieve_projects(out):
    with open(projects_path, "r", encoding="utf-8") as file:
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
    with open(education_path, "r", encoding="utf-8") as f:
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
    with open("summary.txt", "w", encoding="utf-8") as out:
        retrieve_experiences(out)
        retrieve_testimonials(out)
        retrieve_projects(out)
        retrieve_certificates(out)
        retrieve_education(out)


if __name__ == "__main__":
    main()
