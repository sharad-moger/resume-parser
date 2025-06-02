import re

def parse_resume(text):
    skills = ["Python", "Flask", "Django", "Data Structures", "Machine Learning"]
    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_pattern = r'\b\d{10}\b'  

    email = re.findall(email_pattern, text)
    phone = re.findall(phone_pattern, text)

    print("Skills found:", ", ".join(found_skills))
    print("Email found:", email[0] if email else "No email found")
    print("Phone number found:", phone[0] if phone else "No phone number found")

if __name__ == "__main__":
    sample_resume = """
    Name: Sharad Moger
    Email: sharad.moger@gmail.com
    Phone: 9876543210
    Skills: Python, Flask, Web Scraping, Data Structures
    Education: B.E. in Computer Science
    """

    parse_resume(sample_resume)








